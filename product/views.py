from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from product import products
from product.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = products.products
        return context


class ProductDetailView(TemplateView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs.get("pk")
        product = get(products.products, product_id)
        context["product"] = product
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = "products.html"


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products.html"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products.html"


def get(products, id):
    for product in products:
        if product["id"] == str(id):
            return product
    return None
