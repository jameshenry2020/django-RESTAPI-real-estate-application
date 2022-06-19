from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import NotYourProfile, ProfileNotFound
from .models import HostAgent, Profile
from .renderers import ProfileJSONRenderer
from .serializers import (AgentCreateSerializer, AgentProfileSerializer,
                          ProfileSerializer, UpdateProfileSerializer)

# Create your views here.


class BecomeAnAgent(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        agent = Profile.objects.get(user=request.user)
        serializer = AgentCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save(profile=agent)
            agent.is_agent = True
            agent.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AgentListView(generics.ListAPIView):
    serializer_class = AgentProfileSerializer
    queryset = HostAgent.objects.all()


class GetAgentProfileDetail(APIView):
    serializer_class = AgentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request, business_name):
        agent = HostAgent.objects.get(brand_name=business_name)
        serializer = self.serializer_class(agent, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUserProfile(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        serializer = self.serializer_class(profile, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateUserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def patch(self, request, user_id):
        try:
            Profile.objects.get(user__id=user_id)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        user = request.user
        if user.id != user_id:
            raise NotYourProfile

        data = request.data
        serializer = UpdateProfileSerializer(
            instance=user.profile, data=data, partial=True
        )
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
