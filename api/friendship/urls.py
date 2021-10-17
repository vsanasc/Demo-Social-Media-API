from django.urls import path

from .friends import MyFriendsAPI
from .request import RequestFriendsAPI, AcceptRequestAPI

urlpatterns = [
    path('', MyFriendsAPI.as_view()),
    path('request/', RequestFriendsAPI.as_view()),
    path('accept-request/', AcceptRequestAPI.as_view()),
]