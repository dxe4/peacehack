# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0003_auto_20140920_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crazyobject',
            name='ActionGeo_CountryCode',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='ActionGeo_FeatureID',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='ActionGeo_Lat',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1KnownGroupCode',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Religion1Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Religion2Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Type1Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Type2Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor1Type3Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2CountryCode',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2EthnicCode',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Geo_ADM1Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Geo_CountryCode',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Geo_FeatureID',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2KnownGroupCode',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Religion1Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Religion2Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Type1Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Type2Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='crazyobject',
            name='Actor2Type3Code',
            field=models.CharField(max_length=8, null=True, blank=True),
        ),
    ]
