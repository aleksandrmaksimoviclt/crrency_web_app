
from requests_oauthlib import OAuth2Session
from django.contrib.auth.models import User

from .models import GoogleUser


class Google(object):
    def __init__(self, tokens):
        token = tokens['google']
        self.client_id = token['client_id']
        self.client_secret = token['client_secret']
        self.redirect_uri = 'http://localhost:8000/auth/google/check_response/'
        self.auth_base_url = 'https://accounts.google.com/o/oauth2/auth'
        self.token_url = 'https://accounts.google.com/o/oauth2/token'
        self.scope = [
            'https://www.googleapis.com/auth/userinfo.email',
            'https://www.googleapis.com/auth/userinfo.profile',   
        ]
        self._authorization_url = None
        self._google = None
        self._state = None

    @property
    def google(self):
        google = OAuth2Session(self.client_id, scope=self.scope, redirect_uri=self.redirect_uri)
        self._google = google
        return self._google

    def login(self):
        self._authorization_url, self._state = self.google.authorization_url(
            self.auth_base_url,
            # offline for refresh token
            # force to always make user click authorize
            access_type="offline",
            approval_prompt="force")

    @property
    def state(self):
        ''' Used for checking auth and callback csrf token'''
        return self._state

    @property
    def authorization_url(self):
        ''' Only after login '''
        return self._authorization_url
    
    def google_fetch(self, redirect_response):
        import pdb; pdb.set_trace()
        token = self.google.fetch_token(
            token_url=self.token_url,
            client_secret=self.client_secret,
            authorization_response=redirect_response)
        import pdb; pdb.set_trace()
        response = self.google.get('https://www.googleapis.com/oauth2/v1/userinfo')
        if response.status_code == 400:
            return False, False
        content = response.json()