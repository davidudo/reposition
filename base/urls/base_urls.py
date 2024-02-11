from django.urls import path

from base.views import base_views as views

urlpatterns = [
    path("", views.home, name="home"),
]
