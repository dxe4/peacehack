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
    days = list(range(1, 29))  # 2->3 reasons
    result = [_get_data(2014, 2, day, 'UKR') for day in days]

    plt.plot(days, result)
    plt.ylabel('Times Mentioned')
    plt.xlabel('Day')
    plt.title('Ukraine times mentioned in febfruary')
    plt.savefig('ukraine.png')
    plt.close()


def ukraine_september():
    days_aug = list(range(15, 30))  # 2->3 reasons
    days_sep = list(range(1, 15))
    days = days_sep + days_aug

    result_sep = [_get_data(2014, 9, day, 'UKR') for day in days_sep]
    result_aug = [_get_data(2014, 8, day, 'UKR') for day in days_aug]
    result = result_aug + result_sep

    plt.plot(days, result)
    plt.ylabel('Times Mentioned')
    plt.xlabel('Day')
    plt.title('Ukraine times mentioned in august and september 2014')
    plt.savefig('ukraine_aug_sept.png')
    plt.close()
