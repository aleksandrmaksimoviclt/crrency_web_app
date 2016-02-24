
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Profile, Balance
from transaction.models import Transaction, Currency

# Register your models here.
admin.site.register(Profile, SimpleHistoryAdmin)
admin.site.register(Currency, SimpleHistoryAdmin)
admin.site.register(Balance, SimpleHistoryAdmin)
admin.site.register(Transaction)