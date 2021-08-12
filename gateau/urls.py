from django.contrib import admin
from django.urls import path, include
from gateau import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("desserts/", views.dessert_list, name="dessert_list"),
]
