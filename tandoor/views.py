from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import FoodCategory, FoodItem, CATEGORY_TYPE_CHOICES


# Create your views here.
class FoodItemDetailView(DetailView):
    model = FoodItem

class FoodCategoryListView(ListView):
    model = FoodCategory

    def get_context_data(self, **kwargs):
        context = super(FoodCategoryListView, self).get_context_data(**kwargs)
        context['category_type_choices'] = list(CATEGORY_TYPE_CHOICES)
        return context

class FoodCategoryDetailView(DetailView):
    model = FoodCategory

class HomeView(TemplateView):
    template_name = "TakeawayHomePage.html"

class AboutView(TemplateView):
    template_name = "TakeawayAboutPage.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['sections'] = [{'name':'About'},{'name':'Reviews'}]
        return context
