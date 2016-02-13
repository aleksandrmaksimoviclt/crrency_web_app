
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


from .models import Transaction
from .transaction import make_transaction as make


def all_transactions(request):
    transactions = Transaction.objects.all().order_by('-time')
    return render(request, 'transaction/transactions.html', {'transactions': transactions,})

@csrf_exempt
def make_transaction (request):
    if request.method == "POST":
        sender = request.user
        recipient = request.POST.get('recipient', '')
        amount = request.POST.get('amount', '')
        currency = request.POST.get('currency', '')
        status = make(sender, recipient, amount, currency)
        print(status)
    return HttpResponseRedirect('/dashboard/transactions/')