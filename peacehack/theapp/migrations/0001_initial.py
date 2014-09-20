# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrazyObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ActionGeo_ADM1Code', models.CharField(max_length=10, null=True, blank=True)),
                ('ActionGeo_CountryCode', models.CharField(max_length=4, null=True, blank=True)),
                ('ActionGeo_FeatureID', models.CharField(max_length=4, null=True, blank=True)),
                ('ActionGeo_FullName', models.CharField(max_length=200, null=True, blank=True)),
                ('ActionGeo_Lat', models.CharField(max_length=4, null=True, blank=True)),
                ('ActionGeo_Long', models.TextField(null=True, blank=True)),
                ('ActionGeo_Type', models.TextField(null=True, blank=True)),
                ('Actor1Code', models.TextField(null=True, blank=True)),
                ('Actor1CountryCode', models.TextField(null=True, blank=True)),
                ('Actor1EthnicCode', models.TextField(null=True, blank=True)),
                ('Actor1Geo_ADM1Code', models.TextField(null=True, blank=True)),
                ('Actor1Geo_CountryCode', models.IntegerField(null=True, blank=True)),
                ('Actor1Geo_FeatureID', models.IntegerField(null=True, blank=True)),
                ('Actor1Geo_FullName', models.TextField(null=True, blank=True)),
                ('Actor1Geo_Lat', models.TextField(null=True, blank=True)),
                ('Actor1Geo_Long', models.TextField(null=True, blank=True)),
                ('Actor1Geo_Type', models.IntegerField(null=True, blank=True)),
                ('Actor1KnownGroupCode', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor1Name', models.TextField(null=True, blank=True)),
                ('Actor1Religion1Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor1Religion2Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor1Type1Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor1Type2Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor1Type3Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2CountryCode', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2EthnicCode', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2Geo_ADM1Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2Geo_CountryCode', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2Geo_FeatureID', models.IntegerField(null=True, blank=True)),
                ('Actor2Geo_FullName', models.TextField(null=True, blank=True)),
                ('Actor2Geo_Lat', models.TextField(null=True, blank=True)),
                ('Actor2Geo_Long', models.TextField(null=True, blank=True)),
                ('Actor2Geo_Type', models.IntegerField(null=True, blank=True)),
                ('Actor2KnownGroupCode', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2Name', models.TextField(null=True, blank=True)),
                ('Actor2Religion1Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2Religion2Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2Type1Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2Type2Code', models.CharField(max_length=4, null=True, blank=True)),
                ('Actor2Type3Code', models.CharField(max_length=4, null=True, blank=True)),
                ('AvgTone', models.TextField(null=True, blank=True)),
                ('DATEADDED', models.IntegerField(null=True, blank=True)),
                ('EventBaseCode', models.IntegerField(null=True, blank=True)),
                ('EventCode', models.IntegerField(null=True, blank=True)),
                ('EventRootCode', models.IntegerField(null=True, blank=True)),
                ('FractionDate', models.TextField(null=True, blank=True)),
                ('GLOBALEVENTID', models.IntegerField(null=True, blank=True)),
                ('GoldsteinScale', models.TextField(null=True, blank=True)),
                ('IsRootEvent', models.IntegerField(null=True, blank=True)),
                ('MonthYear', models.IntegerField(null=True, blank=True)),
                ('NumArticles', models.IntegerField(null=True, blank=True)),
                ('NumMentions', models.IntegerField(null=True, blank=True)),
                ('NumSources', models.IntegerField(null=True, blank=True)),
                ('QuadClass', models.IntegerField(null=True, blank=True)),
                ('SOURCEURL', models.TextField(null=True, blank=True)),
                ('SQLDATE', models.IntegerField(null=True, blank=True)),
                ('Year', models.IntegerField(null=True, blank=True)),
                ('Day', models.IntegerField(null=True, blank=True)),
                ('Month', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
