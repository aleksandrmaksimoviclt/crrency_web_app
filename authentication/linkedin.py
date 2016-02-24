#!/usr/bin/env python
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix
from django.contrib.auth.models import User

from .models import LinkedinUser
from dashboard.models import Profile


class Linkedin(object):
    """docstring for Linkedin"""
    def __init__(self, tokens):
        token = tokens['linkedin']
        self.client_id = token['client_id']
        self.client_secret = token['client_secret']
        self.auth_base_url = 'https://www.linkedin.com/uas/oauth2/authorization'
        self.token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'
        self.redirect_url = 'http://localhost:8000/auth/linkedin/check_response/'
        # self.redirect_url = 'http://192.168.1.105:8000/auth/linkedin/check_response/'
        self.request_url = 'https://api.linkedin.com/v1/people/~'
        self._authorization_url = None
        self._linkedin = None
        self._response = None
        self.request_items = [
            'firstName',
            'lastName',
            'id',
            'headline',
            'email-address',
            'location',
        ]
        self._details = None
        self.msg = None

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

    @property
    def response(self):
        return self._response

    @property
    def details(self):
        return self._details

    @property
    def token(self):
        return self._token
    

    def _get_details_url(self, details):
        if details:
            url = ':('
            for detail in details:
                url += '%s,' % detail
            url += ')'
        else:
            url = ''
        return url

    def request_details(self, token, details):
        response = self.linkedin.get(
            self.request_url + self._get_details_url(details) +
            '?oauth2_access_token=%s&format=json' % token['access_token'])
        self._response = response
        self._details = response.json()
        
    def check_existing(self):
        try:
            user = User.objects.get(username=self.details['id'])
        except User.DoesNotExist:
            user = None
        return user
    
    def create_new_user(self):
        try:
            user = User.objects.create_user(
                self.details['id'],
                self.details['emailAddress'],
                self.token['access_token'])
        except Exception as e:
            self.msg.append(e)
            user = None
        return user

    def save_token(self, user):
        token = self.token['access_token']
        try:
            linkedin_user = LinkedinUser.objects.get(user=user)
            linkedin_user.access_token = token
            linkedin_user.save()

        except LinkedinUser.DoesNotExist:
            LinkedinUser.objects.create(user=user, access_token=token)
        user.set_password(token)
        user.save()

    def linkedin_fetch(self, redirect_response):
        self._token = self.linkedin.fetch_token(token_url=self.token_url, client_secret=self.client_secret, authorization_response=redirect_response)
        print(self.token)
        self.request_details(self.token, self.request_items)
        if not self.response.status_code == 200:
            return False, False
        user = self.check_existing()
        if not user:
            user = self.create_new_user()
            self.create_profile(user)
        self.save_token(user)  
        return self.details['id'], self.token['access_token']

    def create_profile(self, user):
        try:
            #add headline
            Profile.objects.create(
                username=user,
                name=self.details['firstName'],
                surname=self.details['lastName'],
                email=self.details['emailAddress'],
                current_location=self.details['location']['name'],
            )
        except Exception as e:
            pass
