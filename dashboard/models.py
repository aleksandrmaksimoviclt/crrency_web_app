
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone


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
        return self.surname


class Currency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    total = models.FloatField(default=0)
    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True)
    # members = models.ForeignKey(NetworkMembers)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Currency, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Balance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Profile)
    amount = models.FloatField(default=0)
    currency = models.ForeignKey(Currency)


    def __str__(self):
        return "Total balance: %s %s" % (self.amount, self.currency)

'''class BalanceHistory(models.Model):
    balance = models.ForeignKey(Balance)
    timestamp = models.DateTimeField(auto_now=True)
'''
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateTimeField(editable=False)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='recipient')
    amount = models.FloatField()
    currency = models.ForeignKey(Currency)

    def save(self, *args, **kwargs):
        if not self.id:
            self.time = timezone.now()
        return super(Transaction, self).save(*args, **kwargs)


