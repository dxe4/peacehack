# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0011_auto_20140920_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crazyobject',
            name='Day',
            field=models.IntegerField(db_index=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Month',
            field=models.IntegerField(db_index=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Year',
            field=models.IntegerField(db_index=True, null=True, blank=True),
        ),
    ]
