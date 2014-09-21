# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0012_auto_20140921_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crazyobject',
            name='EventCode',
            field=models.IntegerField(db_index=True, null=True, blank=True),
        ),
    ]
