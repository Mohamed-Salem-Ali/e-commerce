from django.urls import path, include

from authentication.views import UserProfileView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),  # Login, Logout, Password Reset
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Register
    path('auth/profile/', UserProfileView.as_view(), name='user-profile'),
]
