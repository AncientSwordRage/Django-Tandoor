from django.contrib import admin
from tandoor.models import FoodItem, FoodCategory
# Register your models here.

def make_starter(modeladmin, request, queryset):
    queryset.update(categoryType='starter')
make_starter.short_description = 'Mark as Starter'

def make_main(modeladmin, request, queryset):
    queryset.update(categoryType= 'main')
make_main.short_description = 'Mark as Main'

def make_side(modeladmin, request, queryset):
    queryset.update(categoryType='sides')
make_side.short_description = 'Mark as Side'

def make_special(modeladmin, request, queryset):
    queryset.update(categoryType='special')
make_special.short_description = 'Mark as Special'

def clear_description(modeladmin, request, queryset):
    queryset.update(description='')
clear_description.short_description = 'Clear description'

class FoodItemInline(admin.TabularInline):
    model = FoodItem

class FoodCategoryAdmin(admin.ModelAdmin):
    model = FoodCategory
    inlines = [
        FoodItemInline,
    ]
    actions = [make_starter,make_main,make_special,make_side,clear_description]

admin.site.register(FoodCategory,FoodCategoryAdmin)


