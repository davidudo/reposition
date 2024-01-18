from django.urls import path

from . import views
from .views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path("update/<str:pk>/", ProductUpdateView.as_view(), name="product-update"),
    path("delete/<str:pk>/", ProductDeleteView.as_view(), name="product-delete"),
    path("<str:pk>/", ProductDetailView.as_view(), name="product-detail"),
]
