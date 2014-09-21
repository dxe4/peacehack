from django.db.models import Count

import matplotlib.pyplot as plt

from theapp.models import CrazyObject


def _get_data(year, month, day, country):
    result_a = CrazyObject.objects.filter(
        Year=year, Month=month, Day=day, Actor1CountryCode=country) \
        .aggregate(Count('NumMentions'))

    result_b = CrazyObject.objects.filter(
        Year=year, Month=month, Day=day, Actor2CountryCode=country) \
        .aggregate(Count('NumMentions'))
    return result_a['NumMentions__count'] + result_b['NumMentions__count']


def ukraine_february():
    # https://raw.githubusercontent.com/papaloizouc/peacehack/master/doc/ukraine_feb.png
    days = list(range(1, 29))  # 2->3 reasons
    result = [_get_data(2014, 2, day, 'UKR') for day in days]

    plt.plot(days, result)
    plt.ylabel('Times Mentioned')
    plt.xlabel('Day')
    plt.title('Ukraine times mentioned in febfruary')
    plt.savefig('ukraine.png')
    plt.close()


def ukraine_september():
    # http://www.bbc.co.uk/news/world-europe-28357880
    days = list(range(1, 30))  # 2->3 reasons
    result = [_get_data(2014, 9, day, 'UKR') for day in days]

    plt.plot(days, result)
    plt.ylabel('Times Mentioned')
    plt.xlabel('Day')
    plt.title('Ukraine times mentioned in september 2014')
    plt.savefig('ukraine_sept.png')
    plt.close()


def nigeria_kidnap():
    # http://www.bbc.co.uk/news/world-africa-27120357
    days = list(range(1, 30))
    result = [_get_data(2014, 4, day, 'NGA') for day in days]

    plt.plot(days, result)
    plt.ylabel('Times Mentioned')
    plt.xlabel('Day')
    plt.title('Nigeria times mentioned in april 2014')
    plt.savefig('nigeria_nov.png')
    plt.close()
