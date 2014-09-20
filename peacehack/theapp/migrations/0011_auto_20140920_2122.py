# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0010_auto_20140920_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crazyobject',
            name='ActionGeo_FeatureID',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='ActionGeo_Lat',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Geo_CountryCode',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Geo_FeatureID',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Religion1Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Religion2Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Type1Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Type2Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Type3Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2CountryCode',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2EthnicCode',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Geo_ADM1Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Geo_FeatureID',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Religion1Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Religion2Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Type1Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Type2Code',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Type3Code',
            field=models.TextField(null=True, blank=True),
        ),
    ]
