from django.urls import path
from main import views,api
from django.shortcuts import render

urlpatterns = [
    path("home",views.home,name="home"),
    path("my_issues",views.my_issues,name="my_issues"),
    path("all_issue",views.all_issue,name="all_issue"),
    path("create_issue",views.create_issue,name="create_issue"),
    path("particular_issue/<int:pk>",views.particular_issue,name="particular_issue"),
    path("like",api.likeapi,name="like"), #api_url
]

