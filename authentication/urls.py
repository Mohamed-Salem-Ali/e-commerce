from django.urls import path, include

from authentication.views import  loginPage, logoutUser, profile, registerPage

# URL patterns for authentication-related views
urlpatterns = [
    path("login/", loginPage, name="login"),            # Route for user login page
    path("register/", registerPage, name="register"),   # Route for user registration page
    path('logout/',logoutUser,name="logout"),           # Route for logging out the user
    path('profile/',profile,name="profile")             # Route for user profile page
]
