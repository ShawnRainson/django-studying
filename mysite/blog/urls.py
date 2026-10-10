from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("about/", views.about, name="about"),
    path("", views.home, name="home"),
]