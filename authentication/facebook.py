
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
from django.contrib.auth.models import User

from .models import FacebookUser


class Facebook(object):
    """docstring for Facebook"""
    def __init__(self, tokens):
        token = tokens['facebook']
        self.client_id = token['client_id']
        self.client_secret = token['client_secret']
        self.auth_base_url = 'https://www.facebook.com/dialog/oauth'
        self.token_url = 'https://graph.facebook.com/oauth/access_token'
        self.redirect_uri = 'http://localhost:8000/auth/facebook/check_response/'
        self._authorization_url = None
        self._facebook = None

    @property
    def facebook(self):
        facebook = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri)
        facebook = facebook_compliance_fix(facebook)
        self._facebook = facebook
        return self._facebook
    
    def login(self):
        self._authorization_url, state = self.facebook.authorization_url(self.auth_base_url)

    @property
    def authorization_url(self):
        ''' Only after login'''
        return self._authorization_url

    def facebook_fetch(self, redirect_response):
        token = self.facebook.fetch_token(
            token_url=self.token_url,
            client_secret=self.client_secret,
            authorization_response=redirect_response)
        response = self.facebook.get('https://graph.facebook.com/me?access_token=%s' % token['access_token'])
        if response.status_code == 400:
            return False, False
        content = response.json()
        try:
            name = content['name']
            first_name, last_name = name.split()
        except Exception:
            first_name = ''
            last_name = ''
        identifier = content['id']
        try:
            user = User.objects.get(username=identifier)
            token = FacebookUser.objects.get(user=user).access_token
        except User.DoesNotExist:
            user = User.objects.create_user(
                identifier,
                '',
                token['access_token'])
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            FacebookUser.objects.create(user=user, access_token=token['access_token'])
            token = token['access_token']
        return identifier, token
