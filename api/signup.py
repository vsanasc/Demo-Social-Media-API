from django.contrib.auth.models import User
from django import forms

from rest_framework.views import APIView
from rest_framework.response import Response


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    password_confirm = forms.CharField(widget=forms.PasswordInput(), required=True)
    birthdate = forms.DateField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            self.add_error('password_confirm', "Password does not match")

        if User.objects.filter(username=cleaned_data.get('email')).first():
            self.add_error('email', "Email is already used")

        return cleaned_data


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
            response['message'] = 'User created successfully'
        else:
            response['errors'] = form.errors

        return Response(response)