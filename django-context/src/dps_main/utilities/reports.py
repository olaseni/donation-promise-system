from django.db.models import Sum, Count
from django.db.models.functions import Coalesce
from dps_main.models import Cause


def top_causes_by_amount(limit=5):
    return Cause.objects.annotate(sum=Coalesce(Sum('promise__amount'), 0)).order_by('-sum')[:limit]


def top_causes_by_promises(limit=5):
    return Cause.objects.annotate(count=Count('promise')).order_by('-count')[:limit]
