
from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Profile, Post, Comment, Attachment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('birthdate','bio',)

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('file','is_image',)

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'text', 'attachments', 'created_at', 'modified_at',)