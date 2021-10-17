
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from friendship.models import Friend

from api.serializers import UserSerializer, PostSerializer

from app.models import Post


class FeedAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        friends = Friend.objects.friends(request.user)
        friends_id = [u.id for u in friends]

        posts = Post.objects.filter(user__in=friends_id, status=Post.ACTIVE)

        return Response(
            {
                'results': PostSerializer(posts, many=True).data
            }
        )

