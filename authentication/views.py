
from django.shortcuts import render, redirect, render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.views.generic import View

from .register import register as new_user
from .register import user_activate

from .social_auth_tokens import tokens
from .linkedin import Linkedin
from .facebook import Facebook


def index(request):
    csrf_token = {}
    csrf_token.update(csrf(request))
    return render_to_response('authentication/login.html', csrf_token)


''' Basic login views'''

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


'''Linkedin Views'''

def linkedin(request):
    linkedin = Linkedin(tokens)
    linkedin.login()
    url = linkedin.authorization_url
    return redirect(url)

def linkedin_response_check(request, code):
    redirect_response = request.build_absolute_uri()
    linkedin = Linkedin(tokens)
    login, passwd = linkedin.linkedin_fetch(redirect_response)
    if login and passwd:
        user = auth.authenticate(username=login, password=passwd)
        auth.login(request, user)
        return HttpResponseRedirect('/dashboard/')
    else:
        HttpResponse('401')


''' facebook login views '''

def facebook(request):
    facebook = Facebook(tokens)
    facebook.login()
    url = facebook.authorization_url
    return redirect(url)

def facebook_response_check(request, code):
    redirect_response = request.build_absolute_uri()
    facebook = Facebook(tokens)
    login, passwd = facebook.facebook_fetch(redirect_response)
    if login and passwd:
        user = auth.authenticate(username=login, password=passwd)
        auth.login(request, user)
        return HttpResponseRedirect('/dashboard/')
    else:
        HttpResponse('401')