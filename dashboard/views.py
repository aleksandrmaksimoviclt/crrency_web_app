from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Profile, Balance
from django.contrib.auth.models import User


@login_required(login_url='/auth/login/')
def index(request):
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(username=user)
    try:
        balance = Balance.objects.get(user=profile)
    except Balance.DoesNotExist:
        balance = ''

    return render(request, 'dashboard/index.html', {'profile': profile, 'balance': balance})