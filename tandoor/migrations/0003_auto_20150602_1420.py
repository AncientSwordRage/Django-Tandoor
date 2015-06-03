# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tandoor', '0002_auto_20150602_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
