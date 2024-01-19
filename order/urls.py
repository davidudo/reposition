from django.urls import path

from . import views
from .views import (
    OrderCreateView,
    OrderDeleteView,
    OrderHistoryListView,
    OrderListView,
    OrderUpdateView,
)

urlpatterns = [
    path("", OrderListView.as_view(), name="order-list"),
    path("create/", OrderCreateView.as_view(), name="order-create"),
    path("update/<str:pk>/", OrderUpdateView.as_view(), name="order-update"),
    path("delete/<str:pk>/", OrderDeleteView.as_view(), name="order-delete"),
    path("history/", OrderHistoryListView.as_view(), name="order-history"),
]
