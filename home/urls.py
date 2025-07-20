from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("debug-request/", views.debug_request_view, name="debug-request"),
]
