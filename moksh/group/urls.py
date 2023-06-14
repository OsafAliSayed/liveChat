from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path("", views.groups, name="groups"),
    path('<slug:slug>/', views.group, name="group"),
    path('<slug:slug>/edit', views.edituser, name="edituser"),
]
