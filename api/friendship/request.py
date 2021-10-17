from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django import forms

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from friendship.models import Friend, FriendshipRequest
from friendship.exceptions import AlreadyExistsError, AlreadyFriendsError


class RequestFriendForm(forms.Form):
    user = forms.IntegerField(required=True)
    message = forms.CharField(max_length=200)

    def clean(self):
        cleaned_data = super().clean()
        userData = cleaned_data.get("user")
        user = User.objects.filter(pk=userData).first()
        if not user:
            self.add_error('user', "User not found")

        cleaned_data['user'] = user

        return cleaned_data

class RequestFriendsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        
        form = RequestFriendForm(request.POST)
        response = {
            'success': False
        }
        if form.is_valid():
            data = form.cleaned_data
            try:
                Friend.objects.add_friend(request.user, data.get('user'), message=data.get('message'))
                
                response['success'] = True
                response['message'] = 'Request friend was created successfully'

            except AlreadyExistsError:
                response['message'] = 'You already requested friendship from this user'
            except AlreadyFriendsError:
                response['message'] = 'Users are already friends'
            
        else:
            response['errors'] = form.errors

        return Response(response)


class AcceptRequestForm(forms.Form):
    user = forms.IntegerField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        userData = cleaned_data.get("user")
        user = User.objects.filter(pk=userData).first()
        if not user:
            self.add_error('user', "User not found")

        cleaned_data['user'] = user

        return cleaned_data


class AcceptRequestAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        
        form = AcceptRequestForm(request.POST)
        response = {
            'success': False
        }
        if form.is_valid():
            data = form.cleaned_data
            request = get_object_or_404(FriendshipRequest, from_user=request.user, to_user=data.get('user'))
            request.accept()

            response['success'] = True
            response['message'] = 'Friendship request was accepted successfully'

        else:
            response['errors'] = form.errors

        return Response(response)