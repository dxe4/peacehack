# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0006_auto_20140920_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Code',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
