
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone


class InterestRate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rate = models.FloatField(default=0)
    time = models.DateTimeField(default=timezone.now)

    def save(self, **kwargs):
        interest_rate = super(InterestRate, self).save(**kwargs)
        # import pdb; pdb.set_trace()
        # InterestRateHistory.objects.create(
        #     interest_rate_hist=self,
        #     rate=self.rate)
    
    def __str__(self):
        return '%s' % self.rate


class InterestRateHistory(InterestRate):
    interest_rate_hist = models.ForeignKey(InterestRate, related_name='interest_rate_history')

    class Meta:
        ordering = ['-pk']
    
    def __str__(self):
        return '%s' % self.rate


class AbstractBorrowingLimit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    limit = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s' % self.limit    


class BorrowingLimit(AbstractBorrowingLimit):
    def save(self, **kwargs):
        borrowing_limit = super(BorrowingLimit, self).save()

        # BorrowingLimitHistory.objects.create(
        #     borrowing_limit_hist=self,
        #     limit=self.limit)


class BorrowingLimitHistory(AbstractBorrowingLimit):
    borrowing_limit_hist = models.ForeignKey(BorrowingLimit)

    class Meta:
        ordering = ['-pk']


class Currency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    total = models.FloatField(default=0)
    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True, blank=True)
    members = models.ManyToManyField('dashboard.Profile', related_name='member')
    interest_rate = models.ForeignKey(InterestRate)
    borrowing_limit = models.ForeignKey(BorrowingLimit)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Currency, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateTimeField(default=timezone.now, editable=False)
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

