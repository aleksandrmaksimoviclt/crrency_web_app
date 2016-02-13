#!/usr/bin/env python
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix
from django.contrib.auth.models import User

from .models import LinkedinUser


class Linkedin(object):
    """docstring for Linkedin"""
    def __init__(self, tokens):
        token = tokens['linkedin']
        self.client_id = token['client_id']
        self.client_secret = token['client_secret']
        self.auth_base_url = 'https://www.linkedin.com/uas/oauth2/authorization'
        self.token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'
        self.redirect_url = 'http://localhost:8000/auth/linkedin/check_response/'
        self.redirect_url = 'http://192.168.5.20:8000/auth/linkedin/check_response/'
        self._authorization_url = None
        self._linkedin = None

    @property
    def linkedin(self):
        linkedin = OAuth2Session(self.client_id, redirect_uri=self.redirect_url)
        linkedin = linkedin_compliance_fix(linkedin)
        self._linkedin = linkedin
        return self._linkedin

    def login(self):
        self._authorization_url, state = self.linkedin.authorization_url(self.auth_base_url)
    
    @property
    def authorization_url(self):
        ''' Only after login'''
        return self._authorization_url

    def linkedin_fetch(self, redirect_response):
        token = self.linkedin.fetch_token(token_url=self.token_url, client_secret=self.client_secret, authorization_response=redirect_response)
        response = self.linkedin.get('https://api.linkedin.com/v1/people/~?oauth2_access_token=%s&format=json' % token['access_token'])
        if response.status_code == 401:
            return False, False
        content = response.json()
        try:
            first_name = content['firstName']
            last_name = content['lastName']
        except Exception:
            first_name = ''
            last_name = ''
        identifier = content['id']
        try:
            user = User.objects.get(username=identifier)
            old_token = LinkedinUser.objects.get(user=user).access_token
            if old_token == token['access_token']:
                pass
        except User.DoesNotExist:
            user = User.objects.create_user(
                identifier,
                '%s@linkedin.com' % identifier,
                token['access_token'])
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            LinkedinUser.objects.create(user=user, access_token=token['access_token'])
            token = token['access_token']
        return identifier, token