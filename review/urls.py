from django.urls import path

from . import views
from .views import ReviewCreateView, ReviewDeleteView, ReviewListView, ReviewUpdateView

urlpatterns = [
    path("", ReviewListView.as_view(), name="review_list"),
    path("create/", ReviewCreateView.as_view(), name="review_create"),
    path("update/<str:pk>/", ReviewUpdateView.as_view(), name="review_update"),
    path("delete/<str:pk>/", ReviewDeleteView.as_view(), name="review_delete"),
]
