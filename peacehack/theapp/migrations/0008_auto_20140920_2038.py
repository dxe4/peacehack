# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0007_auto_20140920_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Geo_FeatureID',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
