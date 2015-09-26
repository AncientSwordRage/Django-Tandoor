from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import FoodCategory, FoodItem


# Create your views here.
class FoodItemDetailView(DetailView):
    model = FoodItem

class FoodCategoryListView(ListView):
    model = FoodCategory

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
