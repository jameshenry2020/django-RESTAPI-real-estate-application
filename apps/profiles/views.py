from multiprocessing import context
from rest_framework import generics, permissions, status
from uritemplate import partial
from .serializers import ProfileSerializer, UpdateProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .exceptions import ProfileNotFound, NotYourProfile
from .renderers import ProfileJSONRenderer
from .models import Profile
# Create your views here.



class GetUserProfile(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]
    
    def get(self, request):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        serializer = self.serializer_class(profile, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateUserProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def patch(self, request, user_id):
        try:
            Profile.objects.get(user__id=user_id)
        except Profile.DoesNotExist:
            raise ProfileNotFound

        user =request.user
        if user.id !=user_id:
            raise NotYourProfile

        data = request.data
        serializer = UpdateProfileSerializer(instance=user.profile, data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


