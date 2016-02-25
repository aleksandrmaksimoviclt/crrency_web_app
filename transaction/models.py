
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from simple_history.models import HistoricalRecords
from stream_django.activity import Activity



class Currency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    total = models.FloatField(default=0)
    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True, blank=True)
    members = models.ManyToManyField('dashboard.Profile', related_name='member')
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Currency, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class InterestRate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rate = models.FloatField(default=0)
    time = models.DateTimeField(default=timezone.now)
    currency = models.ForeignKey(Currency)
    history = HistoricalRecords()

    def __str__(self):
        return '%s' % self.rate


class BorrowingLimit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    limit = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    currency = models.ForeignKey(Currency)
    history = HistoricalRecords()

    def __str__(self):
        return '%s' % self.limit


class Transaction(models.Model, Activity):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    sender = models.ForeignKey('dashboard.Profile', related_name='sender')
    recipient = models.ForeignKey('dashboard.Profile', related_name='recipient')
    amount = models.FloatField()
    currency = models.ForeignKey(Currency)
    headline = models.CharField(max_length=30, blank=True)
    note = models.CharField(max_length=300, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        if not self.headline:
            self.headline = 'It was great doing bussiness with you!'
        return super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return '%s sent %s %s %s' % (
            self.sender,
            self.recipient,
            self.amount,
            self.currency.name)

    @property
    def activity_actor_attr(self):
        return self.sender

    @property
    def extra_activity_data(self):
        return {
            'recipient': self.recipient.name,
            'amount': self.amount,
            'headline': self.headline,
            'note': self.note,
        }
       