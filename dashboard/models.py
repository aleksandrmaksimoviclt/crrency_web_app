
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone

from transaction.models import Currency


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    current_location = models.CharField(max_length=100, blank=True, null=True)
    date_joined = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_joined = timezone.now()
        return super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %s' % (self.surname, self.name)


class Balance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Profile)
    amount = models.FloatField(default=0)
    currency = models.ForeignKey(Currency)


    def __str__(self):
        return "%s's Total balance: %s %s" % (self.user, self.amount, self.currency)

'''class BalanceHistory(models.Model):
    balance = models.ForeignKey(Balance)
    timestamp = models.DateTimeField(auto_now=True)
'''



