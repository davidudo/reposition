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
    path("", OrderListView.as_view(), name="order_list"),
    path("create/", OrderCreateView.as_view(), name="order_create"),
    path("update/<str:pk>/", OrderUpdateView.as_view(), name="order_update"),
    path("delete/<str:pk>/", OrderDeleteView.as_view(), name="order_delete"),
    path("history/<str:pk>", OrderHistoryListView.as_view(), name=" sna"),
]
