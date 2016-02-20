
from django.utils import timezone

from dashboard.models import Balance
from transaction.models import InterestRate


class InterestRateTrigger(object):
    """docstring for InterestRateTrigger"""
    def __init__(self, user, currency):
        super(InterestRateTrigger, self).__init__()
        self.user = user
        self.currency = currency
        
    def count(self):
        try:
            balance = Balance.objects.get(user=self.user, currency=self.currency)
        except Exception as e:
            print(e)
        else:
            timedelta = timezone.now() - timebalance.change_time 
            interest_rate = InterestRate.objects.get(currency=self.currency)
            new_balance = balance.amount * (1 + interest_rate.rate / 365) ** timedelta
            balance.amount = new_balance
            balance.save()