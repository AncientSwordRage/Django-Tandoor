# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tandoor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='FoodCategory',
            field=models.ForeignKey(related_name='items', to='tandoor.FoodCategory'),
        ),
    ]
