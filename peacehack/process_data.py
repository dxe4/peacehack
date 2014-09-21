from django.db.models import Count

import matplotlib.pyplot as plt

from theapp.models import CrazyObject


def ukraine():
    result = []
    days = list(range(1, 29))  # 2->3 reasons

    for i in days:
        result_a = CrazyObject.objects.filter(
            Year=2014, Month=2, Day=i, Actor2CountryCode='UKR') \
            .aggregate(Count('NumMentions'))

        result_b = CrazyObject.objects.filter(
            Year=2014, Month=2, Day=i, Actor1CountryCode='UKR') \
            .aggregate(Count('NumMentions'))

        _sum = result_a['NumMentions__count'] + result_b['NumMentions__count']
        result.append(_sum)

    plt.plot(days, result)
    plt.xlabel('Times Mentioned')
    plt.ylabel('Day')
    plt.title('Ukraine times mentioned in febfruary')
    plt.savefig('ukraine.png')
