
from django.contrib import admin
from django.urls import path
from . import views
from . import viewsets
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]


api_urlpatterns = [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/registration', viewsets.registration.as_view(), name='post_registration'),
    path('api/registration-list', viewsets.registration_list.as_view(), name='user_device'),
    path('api/get-profile-details',viewsets.profile_details.as_view(),name="current_profile"),
    path('api/logout', viewsets.Logout.as_view(),name="user_logout"),
    path('api/profile-update', viewsets.profile_update.as_view(),name="user_profile_update"),
    path('api/profile-filter',viewsets.profiledata_filter.as_view(),name="profile_filter")
]

urlpatterns += api_urlpatterns


