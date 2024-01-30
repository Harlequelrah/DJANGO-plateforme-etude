from django.contrib import admin
from django.urls import path
from page.views import *
urlpatterns = [
    path('index/',index,name="index"),
    path('home/',home,name="home"),

]
