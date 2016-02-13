
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone


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


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateTimeField(editable=False)
    sender = models.ForeignKey('dashboard.Profile', related_name='sender')
    recipient = models.ForeignKey('dashboard.Profile', related_name='recipient')
    amount = models.FloatField()
    currency = models.ForeignKey(Currency)

    def save(self, *args, **kwargs):
        if not self.time:
            self.time = timezone.now()
        return super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return '%s sent %s %s %s' % (
            self.sender,
            self.recipient,
            self.amount,
            self.currency.name)


