# Create your views here.
from django.urls import path
from myauth import views

urlpatterns = [
    path("index",views.index,name="index"),
    path("signup",views.signUp,name="signup"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
       
]

