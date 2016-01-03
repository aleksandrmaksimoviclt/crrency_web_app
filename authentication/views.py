from django.shortcuts import render, redirect, render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .linkedin import login as linkedin_login
from .register import register as new_user
from .register import user_activate



def index(request):
    csrf_token = {}
    csrf_token.update(csrf(request))
    return render_to_response('authentication/login.html', csrf_token)

def register(request):
    return render(request, 'authentication/register.html', {})

def user_create(request):
    state, msg = new_user(request)
    if state:
        return render_to_response('authentication/register_success.html', {})
    else:
        return render_to_response('authentication/register.html', {})
    
def activate(request, user_id):
    msg = user_activate(user_id)
    return HttpResponse(msg)

def basic(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/authentication/login')

def linkedin(request):
    linkedin_login()
