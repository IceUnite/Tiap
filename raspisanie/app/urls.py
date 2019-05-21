from django.urls import path
from django.views.generic import ListView, DetailView
from app.models import Days
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', ListView.as_view(queryset=Days.objects.all(), template_name="app/index.html")),
    path('login/', authViews.LoginView.as_view(template_name="app/login.html"), name="login"),
    path('redirect/', authViews.LogoutView.as_view(template_name="app/redirect.html"), name="redirect"),
    path('registration/', views.registration, name="registration")
]
