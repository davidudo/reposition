from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from products import products
from products.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = products.products
        return context


class ProductDetailView(TemplateView):
    model = Product
    template_name = "products/product_details.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    template_name = "products/products.html"


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/products.html"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/products.html"
