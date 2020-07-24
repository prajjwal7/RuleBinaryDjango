from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('' , views.index , name="index"),
    path('O1Olive' , views.O1Olive , name="olive")
]
