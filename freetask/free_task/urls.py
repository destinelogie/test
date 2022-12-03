from django.urls import path
from .views import HomePage, Register, LogIn, LogOut

urlpatterns = [
    path('home/', HomePage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', LogIn, name="login-page"),
    path('logout/', LogOut, name="log-out")
]