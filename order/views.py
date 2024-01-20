from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)
from order.models import Order


class OrderListView(ListView):
    model = Order
    template_name = "orders.html"


class OrderCreateView(CreateView):
    model = Order
    template_name = "orders.html"


class OrderUpdateView(UpdateView):
    model = Order
    template_name = "orders.html"


class OrderDeleteView(DeleteView):
    model = Order
    template_name = "orders.html"


class OrderHistoryListView(ListView):
    model = Order
    template_name = "order_history.html"
