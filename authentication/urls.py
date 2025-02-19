from django.urls import path, include

from authentication.views import  loginPage, logoutUser, profile, registerPage

urlpatterns = [
    path('api/', include('dj_rest_auth.urls')),  # Login, Logout, Password Reset
    path('api/registration/', include('dj_rest_auth.registration.urls')),  # Register
    #path('api/profile/', UserProfileView.as_view(), name='user-profile'),
    path("login/", loginPage, name="login"),
    path("register/", registerPage, name="register"),
    path('logout/',logoutUser,name="logout"),
    path('profile/',profile,name="profile")
]
