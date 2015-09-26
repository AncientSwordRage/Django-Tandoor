# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tandoor', '0003_auto_20150602_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcategory',
            name='categoryType',
            field=models.CharField(max_length=128, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodcategory',
            name='description',
            field=models.TextField(blank=True, null=True, default=True),
        ),
    ]
