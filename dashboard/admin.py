from django.contrib import admin
from .models import Profile, Currency, Balance, Transaction
# Register your models here.
admin.site.register(Profile)
admin.site.register(Currency)
admin.site.register(Balance)
admin.site.register(Transaction)