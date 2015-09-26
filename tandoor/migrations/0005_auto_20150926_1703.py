# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tandoor', '0004_auto_20150926_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcategory',
            name='categoryType',
            field=models.CharField(choices=[('starter', 'Starters'), ('special', 'Specials'), ('main', 'Mains'), ('sides', 'Sides and Extras')], max_length=128),
        ),
        migrations.AlterField(
            model_name='foodcategory',
            name='description',
            field=models.TextField(null=True, blank=True, default=None),
        ),
    ]
