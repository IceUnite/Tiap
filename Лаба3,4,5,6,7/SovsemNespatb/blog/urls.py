from django.urls import path
from django.conf.urls import url
from blog.models import Post
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^blog/(?P<pk>[0-9]+)/$', views.kaknespatb, name="kaknespatb"),
    path('login/', authViews.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path('exit/', authViews.LogoutView.as_view(template_name="blog/exit.html"), name="exit"),
    path('registration/', views.registration, name="registration"),
    path('create/', views.create, name="create")
]