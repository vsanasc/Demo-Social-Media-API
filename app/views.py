from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from .serializers import UserSerializer, ProfileSerializer

class MyProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        userData = UserSerializer(request.user).data
        profileData = ProfileSerializer(request.user.profile).data
        return Response(
            {**userData, **profileData}
        )