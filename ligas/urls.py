from django.contrib import admin
from django.urls import path, include
from ligas import views

urlpatterns = [
    path("createequip", views.createequip, name="createequip"),
    path("createlliga", views.createlliga, name="createlliga"),
    path("menu", views.menu, name="menu"),
    path("classificacio/<int:lliga_id>", views.classificacio, name="classificacio"),
    path("edita_equip", views.edita_equip, name="edita_equip"),
    path("profile/", views.profile),
]