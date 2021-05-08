from django.contrib import admin
from django.urls import path,include
from myauth import urls
from main import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('main.urls')),
    path('myauth/',include('myauth.urls')),
]
