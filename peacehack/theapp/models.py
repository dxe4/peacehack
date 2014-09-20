from django.db import models

# Create your models here.
_sample_data = {
    'ActionGeo_ADM1Code': 'USIA',
    'ActionGeo_CountryCode': 'US',
    'ActionGeo_FeatureID': 'IA',
    'ActionGeo_FullName': 'Iowa, United States',
    'ActionGeo_Lat': '42.0046',
    'ActionGeo_Long': '-93.214',
    'ActionGeo_Type': 2,
    'Actor1Code': 'COP',
    'Actor1CountryCode': 'TUR',
    'Actor1EthnicCode': 'mas',
    'Actor1Geo_ADM1Code': 'USMA',
    'Actor1Geo_CountryCode': 'US',
    'Actor1Geo_FeatureID': 617565,
    'Actor1Geo_FullName': 'Boston, Massachusetts, United States',
    'Actor1Geo_Lat': '42.3584',
    'Actor1Geo_Long': '-71.0598',
    'Actor1Geo_Type': 3,
    'Actor1KnownGroupCode': 'OPC',
    'Actor1Name': 'POLICE',
    'Actor1Religion1Code': 'SHN',
    'Actor1Religion2Code': 'SUN',
    'Actor1Type1Code': 'COP',
    'Actor1Type2Code': 'AGR',
    'Actor1Type3Code': 'BUS',
    'Actor2Code': ' JUD',
    'Actor2CountryCode': 'USA',
    'Actor2EthnicCode': 'mas',
    'Actor2Geo_ADM1Code': 'USIA',
    'Actor2Geo_CountryCode': 'US',
    'Actor2Geo_FeatureID': 'IA',
    'Actor2Geo_FullName': 'Iowa, United States',
    'Actor2Geo_Lat': '42.0046',
    'Actor2Geo_Long': '-93.214',
    'Actor2Geo_Type': 2,
    'Actor2KnownGroupCode': 'ICG',
    'Actor2Name': 'JUDGE',
    'Actor2Religion1Code': 'SHN',
    'Actor2Religion2Code': 'SUN',
    'Actor2Type1Code': 'JUD',
    'Actor2Type2Code': 'REB',
    'Actor2Type3Code': 'GOV',
    'AvgTone': '2.14746543778801',
    'DATEADDED': 20130727,
    'EventBaseCode': 10,
    'EventCode': 10,
    'EventRootCode': 1,
    'FractionDate': '2003.5753',
    'GLOBALEVENTID': 260993884,
    'GoldsteinScale': '0.0',
    'IsRootEvent': 1,
    'MonthYear': 200307,
    'NumArticles': 50,
    'NumMentions': 50,
    'NumSources': 5,
    'QuadClass': 1,
    'SOURCEURL': 'http://www.wkar.org/post/life-without-parole-deal-struck-cleveland-kidnapper',
    'SQLDATE': 20030730,
    'Year': 2003,
    'Day': 10,
    'Month': 10,
}


class CrazyObject(models.Model):
    ActionGeo_ADM1Code = models.CharField(max_length=10, blank=True, null=True)
    ActionGeo_CountryCode = models.CharField(
        max_length=4, blank=True, null=True)
    ActionGeo_FeatureID = models.CharField(max_length=4, blank=True, null=True)
    ActionGeo_FullName = models.CharField(
        max_length=200, blank=True, null=True)
    ActionGeo_Lat = models.CharField(max_length=4, blank=True, null=True)
    ActionGeo_Long = models.TextField(blank=True, null=True)
    ActionGeo_Type = models.TextField(blank=True, null=True)
    Actor1Code = models.TextField(blank=True, null=True)
    Actor1CountryCode = models.TextField(blank=True, null=True)
    Actor1EthnicCode = models.TextField(blank=True, null=True)
    Actor1Geo_ADM1Code = models.TextField(blank=True, null=True)
    Actor1Geo_CountryCode = models.IntegerField(blank=True, null=True)
    Actor1Geo_FeatureID = models.IntegerField(blank=True, null=True)
    Actor1Geo_FullName = models.TextField(blank=True, null=True)
    Actor1Geo_Lat = models.TextField(blank=True, null=True)
    Actor1Geo_Long = models.TextField(blank=True, null=True)
    Actor1Geo_Type = models.IntegerField(blank=True, null=True)
    Actor1KnownGroupCode = models.CharField(
        max_length=4, blank=True, null=True)
    Actor1Name = models.TextField(blank=True, null=True)
    Actor1Religion1Code = models.CharField(max_length=4, blank=True, null=True)
    Actor1Religion2Code = models.CharField(max_length=4, blank=True, null=True)
    Actor1Type1Code = models.CharField(max_length=4, blank=True, null=True)
    Actor1Type2Code = models.CharField(max_length=4, blank=True, null=True)
    Actor1Type3Code = models.CharField(max_length=4, blank=True, null=True)
    Actor2Code = models.CharField(max_length=4, blank=True, null=True)
    Actor2CountryCode = models.CharField(max_length=4, blank=True, null=True)
    Actor2EthnicCode = models.CharField(max_length=4, blank=True, null=True)
    Actor2Geo_ADM1Code = models.CharField(max_length=4, blank=True, null=True)
    Actor2Geo_CountryCode = models.CharField(
        max_length=4, blank=True, null=True)
    Actor2Geo_FeatureID = models.IntegerField(blank=True, null=True)
    Actor2Geo_FullName = models.TextField(blank=True, null=True)
    Actor2Geo_Lat = models.TextField(blank=True, null=True)
    Actor2Geo_Long = models.TextField(blank=True, null=True)
    Actor2Geo_Type = models.IntegerField(blank=True, null=True)
    Actor2KnownGroupCode = models.CharField(
        max_length=4, blank=True, null=True)
    Actor2Name = models.TextField(blank=True, null=True)
    Actor2Religion1Code = models.CharField(max_length=4, blank=True, null=True)
    Actor2Religion2Code = models.CharField(max_length=4, blank=True, null=True)
    Actor2Type1Code = models.CharField(max_length=4, blank=True, null=True)
    Actor2Type2Code = models.CharField(max_length=4, blank=True, null=True)
    Actor2Type3Code = models.CharField(max_length=4, blank=True, null=True)
    AvgTone = models.TextField(blank=True, null=True)
    DATEADDED = models.IntegerField(blank=True, null=True)
    EventBaseCode = models.IntegerField(blank=True, null=True)
    EventCode = models.IntegerField(blank=True, null=True)
    EventRootCode = models.IntegerField(blank=True, null=True)
    FractionDate = models.TextField(blank=True, null=True)
    GLOBALEVENTID = models.IntegerField(blank=True, null=True)
    GoldsteinScale = models.TextField(blank=True, null=True)
    IsRootEvent = models.IntegerField(blank=True, null=True)
    MonthYear = models.IntegerField(blank=True, null=True)
    NumArticles = models.IntegerField(blank=True, null=True)
    NumMentions = models.IntegerField(blank=True, null=True)
    NumSources = models.IntegerField(blank=True, null=True)
    QuadClass = models.IntegerField(blank=True, null=True)
    SOURCEURL = models.TextField(blank=True, null=True)
    SQLDATE = models.IntegerField(blank=True, null=True)
    Year = models.IntegerField(blank=True, null=True)
    Day = models.IntegerField(blank=True, null=True)
    Month = models.IntegerField(blank=True, null=True)
