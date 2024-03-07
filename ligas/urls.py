from django.contrib import admin
from django.urls import path, include
from ligas import views

urlpatterns = [
    path("classificacio", views.classificacio)
]