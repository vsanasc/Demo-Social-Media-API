from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer, ProfileSerializer

from .forms import SignUpForm

class SignupAPI(APIView):

    def post(self, request, format=None):
        form = SignUpForm(request.POST)

        response = {
            'success': False
        }

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data.get('email'),
                email=data.get('email'),
                password=data.get('password')
            )
            user.first_name = data.get('first_name')
            user.last_name = data.get('last_name')
            user.profile.birthdate = data.get('birthdate')
            user.save()

            userData = UserSerializer(user).data
            profileData = ProfileSerializer(user.profile).data
            data = {**userData, **profileData}

            response['success'] = True
            response['data'] = data
        else:
            response['errors'] = form.errors

        return Response(response)



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