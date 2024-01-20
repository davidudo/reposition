from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)
from review.models import Review


class ReviewListView(ListView):
    model = Review
    template_name = "reviews.html"


class ReviewCreateView(CreateView):
    model = Review
    template_name = "reviews.html"


class ReviewUpdateView(UpdateView):
    model = Review
    template_name = "reviews.html"


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = "reviews.html"
