from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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


class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id, format=None):
        user = get_object_or_404(User, pk=id)
        userData = UserSerializer(user).data
        profileData = ProfileSerializer(user.profile).data
        response = {**userData, **profileData}
        response['photos'] = '0'
        response['likes'] = '0'
        response['followers'] = '0'
        response['following'] = '0'
        return Response(response)
