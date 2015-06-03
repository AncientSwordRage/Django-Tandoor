from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import FoodCategory, FoodItem


# Create your views here.
class FoodItemDetailView(DetailView):
    model = FoodItem

class FoodCategoryListView(ListView):
    model = FoodCategory

class FoodCategoryDetailView(DetailView):
    model = FoodCategory
