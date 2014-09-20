# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0002_auto_20140920_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Geo_FeatureID',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
    ]
