from django.contrib import admin
from .models import Profile, Balance
from transaction.models import Transaction, Currency
# Register your models here.
admin.site.register(Profile)
admin.site.register(Currency)
admin.site.register(Balance)
admin.site.register(Transaction)