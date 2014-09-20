import csv
import re
import os
from glob import glob

from django.conf import settings
from pymongo import MongoClient


# BAD IDEA DONT DO THIS !

csv_headers = [
    'GLOBALEVENTID', 'SQLDATE', 'MonthYear', 'Year', 'FractionDate',
    'Actor1Code', 'Actor1Name', 'Actor1CountryCode', 'Actor1KnownGroupCode',
    'Actor1EthnicCode', 'Actor1Religion1Code', 'Actor1Religion2Code',
    'Actor1Type1Code', 'Actor1Type2Code', 'Actor1Type3Code', 'Actor2Code',
    'Actor2Name', 'Actor2CountryCode', 'Actor2KnownGroupCode',
    'Actor2EthnicCode', 'Actor2Religion1Code', 'Actor2Religion2Code',
    'Actor2Type1Code', 'Actor2Type2Code', 'Actor2Type3Code', 'IsRootEvent',
    'EventCode', 'EventBaseCode', 'EventRootCode', 'QuadClass',
    'GoldsteinScale', 'NumMentions', 'NumSources', 'NumArticles', 'AvgTone',
    'Actor1Geo_Type', 'Actor1Geo_FullName', 'Actor1Geo_CountryCode',
    'Actor1Geo_ADM1Code', 'Actor1Geo_Lat', 'Actor1Geo_Long',
    'Actor1Geo_FeatureID', 'Actor2Geo_Type', 'Actor2Geo_FullName',
    'Actor2Geo_CountryCode', 'Actor2Geo_ADM1Code', 'Actor2Geo_Lat',
    'Actor2Geo_Long', 'Actor2Geo_FeatureID', 'ActionGeo_Type',
    'ActionGeo_FullName', 'ActionGeo_CountryCode', 'ActionGeo_ADM1Code',
    'ActionGeo_Lat', 'ActionGeo_Long', 'ActionGeo_FeatureID',
    'DATEADDED', 'SOURCEURL'
]


def fix_values(val):
    if val.isdigit():
        return int(val)
    else:
        return val


def read_file(fpath):
    result = []
    _date = re.findall('([0-9]+)', fpath)[0]
    date_dict = {
        'Year': _date[:4],
        'Month': _date[4:6],
        'Day': _date[6:],
    }

    with open(fpath, 'rb') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter='\t')
        for row in csv_reader:
            row = dict(zip(csv_headers, row))
            row.update(date_dict)
            row = {k: fix_values(v) for k, v in row.items() if v}
            result.append(row)

    return result


def get_csv_files(directory=None):
    directory = directory or os.getcwd()
    print(directory)
    files = glob("".join((directory, '/*', 'CSV')))
    return files


def import_to_mongo():
    client = MongoClient(settings.MONGODB_URL,
                         settings.MONGODB_PORT)
    db = client['dev-db']
    dev_collection = db['dev-collection']

    files = get_csv_files(settings.DATA_DIR[0])
    for _file in files:
        print('importing {}'.format(_file))
        rows = read_file(_file)
        dev_collection.insert(rows)
