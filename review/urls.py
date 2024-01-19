from django.urls import path

from . import views
from .views import ReviewCreateView, ReviewDeleteView, ReviewListView, ReviewUpdateView

urlpatterns = [
    path("", ReviewListView.as_view(), name="review-list"),
    path("create/", ReviewCreateView.as_view(), name="review-create"),
    path("update/<str:pk>/", ReviewUpdateView.as_view(), name="review-update"),
    path("delete/<str:pk>/", ReviewDeleteView.as_view(), name="review-delete"),
]
