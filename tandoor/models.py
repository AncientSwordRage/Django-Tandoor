from django.db import models
from django_tandoor.custom_fields import CurrencyField
from taggit.managers import TaggableManager


# Create your models here.
class FoodItem(models.Model):
    class Meta:
        verbose_name = "FoodItem"
        verbose_name_plural = "FoodItems"

    name = models.CharField(max_length=128)
    price = CurrencyField(max_digits=4,decimal_places=2,currency_symbol='£')
    description = models.TextField(blank=True)
    FoodCategory = models.ForeignKey('FoodCategory', related_name='items')
    tags = TaggableManager()
    spice_rating = models.IntegerField()

    def __str__(self):
        return self.name

class FoodCategory(models.Model):

    class Meta:
        verbose_name = "FoodCategory"
        verbose_name_plural = "FoodCategories"

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
   