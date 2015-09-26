# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tandoor', '0005_auto_20150926_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcategory',
            name='spice_description',
            field=models.CharField(null=True, default=None, max_length=64, choices=[('mild', 'Mild'), ('medium', 'Medium'), ('hot', 'Hot'), ('very_hot', 'Fairly Hot'), ('none', None)]),
        ),
    ]
