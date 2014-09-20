# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0004_auto_20140920_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Geo_CountryCode',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
    ]
