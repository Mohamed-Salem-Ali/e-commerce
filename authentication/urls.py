from django.urls import path, include

from authentication.views import UserProfileView, profile, register, login

urlpatterns = [
    path('api/', include('dj_rest_auth.urls')),  # Login, Logout, Password Reset
    path('api/registration/', include('dj_rest_auth.registration.urls')),  # Register
    path('api/profile/', UserProfileView.as_view(), name='user-profile'),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path('profile',profile,name="profile")
]
