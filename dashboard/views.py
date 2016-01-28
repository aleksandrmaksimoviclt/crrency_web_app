from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):
    return render(request, 'dashboard/index.html', {})

# @login_required(login_url='/authentication/login/')
# def index(request):
#    return HttpResponse('%s' %request.user)
#    {% endcomment %}