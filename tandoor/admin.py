from django.contrib import admin
from tandoor.models import FoodItem, FoodCategory
# Register your models here.
 

class FoodItemInline(admin.TabularInline):
    model = FoodItem

class FoodCategoryAdmin(admin.ModelAdmin):
    model = FoodCategory
    inlines = [
        FoodItemInline,
    ]

admin.site.register(FoodCategory,FoodCategoryAdmin)
