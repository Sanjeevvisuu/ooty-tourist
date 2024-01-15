from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index"),
    path("about_us/",about_us,name="about_us"),
    path("package/",package,name="package"),
]