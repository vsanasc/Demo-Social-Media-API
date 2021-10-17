
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from friendship.models import Friend

from api.serializers import UserSerializer



class MyFriendsAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        friends = Friend.objects.friends(request.user)
        return Response(
            {
                'results': UserSerializer(friends, many=True).data
            }
        )

