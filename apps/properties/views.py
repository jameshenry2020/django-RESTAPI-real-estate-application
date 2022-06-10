import logging
from multiprocessing import context
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status, generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from apps.profiles.models import HostAgent
from .serializers import PropertySerializer, PropertyCreateSerializer, PropertyViewSerializer
from .paginations import PropertyPagination
from .models import Property, PropertyView
from .exceptions import PropertyNotFound
from .exceptions import NotAnAgent

logger = logging.getLogger(__name__)

class PropertyFilter(django_filters.FilterSet):
    advert_type = django_filters.CharFilter(
        field_name="advert_type", lookup_expr="iexact"
    )
    property_type = django_filters.CharFilter(
        field_name="property_type", lookup_expr="iexact"
    )
    price = django_filters.NumberFilter()
    price__gt=django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price__lt=django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Property
        fields = ["advert_type","property_type","price"]


class PropertyListView(generics.ListAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all().order_by("-created_at")
    pagination_class = PropertyPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class= PropertyFilter
    search_fields = ["country", "city"]
    ordering_fields = ["created_at"]

#get the list of properties hosted by a particular agent by the agent
class AgentPropertyListView(APIView):
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PropertyPagination
    ordering_fields = ["created_at"]

    def get(self, request, agent_id):
        agent=HostAgent.objects.get(id=agent_id)
        user=agent.profile.user
        properties=Property.objects.filter(hosted_by=user)
        serializer=self.serializer_class(properties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

class PropertyDetailView(APIView):

    def get(self, request, slug):
        property=Property.objects.get(slug=slug)
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        if not PropertyView.objects.filter(property=property, ip_addr=ip).exists():
            PropertyView.objects.create(ip_addr=ip, property=property)
            property.views +=1
            property.save()
        
        serializer=PropertySerializer(property, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class PropertyUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, slug):
        try:
            property=Property.objects.get(slug=slug)

        except Property.DoesNotExist:
            raise PropertyNotFound

        if request.user != property.hosted_by:
            return Response({"error":"you can't update property that you didn't create"}, status=status.HTTP_400_BAD_REQUEST)
        serializer=PropertyCreateSerializer(instance=property, data=request.data)
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)


class PropertyCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, *args, **kwargs):    
        if request.user.profile.is_agent:
            serializer=PropertyCreateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(hosted_by=self.request.user)
                logger.info(f"property {serializer.data.get('title')} is created")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'error':'you are not an agent please register as an agent first'}, status=status.HTTP_401_UNAUTHORIZED)

       
        

class UploadPropertyImages(APIView):
    permission_classes= [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request):
        property_id=request.data["id"]
        try:
            property=Property.objects.get(id=property_id)
            if request.user == property.hosted_by:
                property.cover_photo=request.data.get('cover_photo', '')
                property.photo1=request.data.get('photo1')
                property.photo2=request.data.get('photo2')
                property.photo3=request.data.get('photo3')
                property.photo4=request.data.get('photo4')
                property.photo5=request.data.get('photo5')
                property.save()
                return Response('Image upload successful')
            return Response({'error':'you are not allowed to upload to someone else property'}, status=status.HTTP_403_FORBIDDEN)

        except Property.DoesNotExist:
            raise PropertyNotFound


class PropertyDeleteApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, slug):
        try:
            property=Property.objects.get(slug=slug)
            if self.request.user !=property.hosted_by:
                return Response({'error':'you are not authorized to perform this action'}, status=status.HTTP_403_FORBIDDEN)
            delete_operation = property.delete()
            data={}
            if delete_operation:
                data['message']='property deleted successfully'
            else:
                data['message'] = 'property delete failed'
            return Response(data)

        except Property.DoesNotExist:
            raise PropertyNotFound



        
        



