from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from stream_django.feed_manager import feed_manager

from .models import Profile, Balance
from django.contrib.auth.models import User


@login_required(login_url='/auth/login/')
def index(request):
    try:
        user = User.objects.get(username=request.user)
        profile = Profile.objects.get(username=user)
    except User.DoesNotExist:
        return HttpResponse('User object does not exist')
    except Profile.DoesNotExist:
        profile = ''
    try:
        balance = Balance.objects.get(user=profile)
    except Balance.DoesNotExist:
        balance = ''
    except Exception as e:
        balance = ''
        # log e

    return render(request, 'dashboard/index.html', {'profile': profile, 'balance': balance})


def feed(request):
    try:
        user = User.objects.get(username=request.user)
        profile = Profile.objects.get(username=user)
    except User.DoesNotExist:
        return HttpResponse('User object does not exist')
    except Profile.DoesNotExist:
        profile = ''
        flat_feed = feed_manager.get_news_feed(profile.id)['flat']