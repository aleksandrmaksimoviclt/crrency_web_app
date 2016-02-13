

from .models import Transaction as TransactionModel
from .models import Currency
from dashboard.models import Balance, Profile
from django.contrib.auth.models import User


class UserBalance(object):
    def __init__(self, user, currency):
        self.user = user
        self.currency = currency
        self._user_balance = None

    def get_balance(self):
        try:
            user_bal = Balance.objects.get(
                user=self.user,
                currency=self.currency)
        except Balance.DoesNotExist:
            user_bal = Balance.objects.create(user=self.user, currency=self.currency)
        except Exception:
            user_bal = None  # log as warning
        self._user_balance = user_bal
        return user_bal

    @property
    def user_balance(self):
        return self._user_balance
    


class Transaction(object):
    def __init__(self, sender, sender_bal, recipient, recipient_bal, amount, currency):
        self.sender = sender
        self.sender_bal = sender_bal
        self.recipient_bal = recipient_bal
        self.recipient = recipient
        self.amount = amount
        self.currency = currency
        self._status = None

    @property
    def status(self):
        return self._status
    

    def make_transaction(self):
        try:
            self.sender_bal.amount -= float(self.amount)
            self.recipient_bal.amount += float(self.amount)
        except Exception as e:
            self._status = e  # logger warning
        else:
            self.sender_bal.save()
            self.recipient_bal.save()
        TransactionModel.objects.create(
                sender=self.sender,
                recipient=self.recipient,
                amount=self.amount,
                currency=self.currency,
            )
        self._status = 'OK'



def make_transaction(sender, recipient, amount, currency):
    sender = User.objects.get(username=sender)
    sender = Profile.objects.get(email=sender.email)
    recipient = Profile.objects.get(email=recipient)
    currency = Currency.objects.get(name=currency)
    sender_balance = UserBalance(sender, currency).get_balance()
    recipient_balance = UserBalance(recipient, currency).get_balance()
    tr = Transaction(
        sender,
        sender_balance,
        recipient,
        recipient_balance,
        amount,
        currency)
    tr.make_transaction()
    return tr.status

