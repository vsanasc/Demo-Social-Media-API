from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .profile import MyProfileAPI, ProfileAPI
from .signup import SignupAPI
from .feed import FeedAPI

urlpatterns = [
    path('sign-up/', SignupAPI.as_view()),
    path('my-profile/', MyProfileAPI.as_view()),
    path('feed/', FeedAPI.as_view()),
    path('friendship/', include('api.friendship.urls')),
    path('profile/<int:id>/', ProfileAPI.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]