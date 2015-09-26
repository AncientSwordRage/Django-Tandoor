# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import malmesbury_tandoori.custom_fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'FoodCategory',
                'verbose_name_plural': 'FoodCategories',
            },
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('price', malmesbury_tandoori.custom_fields.CurrencyField(max_digits=4, decimal_places=2)),
                ('spice_rating', models.IntegerField()),
                ('FoodCategory', models.ForeignKey(related_name='FoodItem_in_FoodCategory', to='tandoor.FoodCategory')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem')),
            ],
            options={
                'verbose_name': 'FoodItem',
                'verbose_name_plural': 'FoodItems',
            },
        ),
    ]
