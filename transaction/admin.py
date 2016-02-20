from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BorrowingLimit)
admin.site.register(InterestRate)
admin.site.register(BorrowingLimitHistory)
admin.site.register(InterestRateHistory)

