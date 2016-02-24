

from .models import Transaction as TransactionModel
from .models import Balance


class UserBalance(object):
    def __init__(self, user, currency):
        self.user = user
        self.currency = currency
        self._user_balance = None

    @property
    def user_balance(self):
        try:
            user_bal = Balance.objects.get(
                user=self.user,
                currency=self.currency)
        except Balance.DoesNotExist:
            user_bal = None
        except Exception:
            user_bal = None  # log as warning
        self._user_balance = user_bal
        return self._user_balance


class Transaction(object):
    def __init__(self, sender, recipient, amount, currency):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.currency = currency

    def make_transaction(self):
        try:
            self.sender.amount -= self.amount
            self.recipient.amount += self.amount
        except Exception:
            pass  # logger warning
        else:
            self.sender.save()
            self.recipient.save()
        TransactionModel.objects.create(
                sender=self.sender.user,
                recipient=self.recipient.user,
                amount=self.amount,
                currency=self.currency,
            )


def make_transaction(sender, recipient, amount, currency):
    sender_balance = UserBalance(sender, currency).user_balance
    recipient_balance = UserBalance(sender, currency).user_balance
    tr = Transaction(sender_balance, recipient_balance, amount, currency)
    tr.make_transaction()

