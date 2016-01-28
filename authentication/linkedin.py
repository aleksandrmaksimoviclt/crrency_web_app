#!/usr/bin/env python
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .social_auth_tokens import tokens


class Linkedin(object):
    """docstring for Linkedin"""
    def __init__(self, tokens):
        super(Linkedin, self).__init__()
        token = tokens['linkedin']
        self.client_id = token['client_id']
        self.client_secret = token['client_secret']
        self.auth_base_url = 'https://www.linkedin.com/uas/oauth2/authorization',
        self.token_url = 'https://www.linkedin.com/uas/oauth2/accessToken',
        self.redirect_url = 'https://localhost:80/auth/linkedin/check_response/',
        
    def login(self):
        linkedin = OAuth2Session(self.client_id, redirect_uri='https://localhost:80/auth/linkedin/check_response/')
        linkedin = linkedin_compliance_fix(linkedin)
        authorization_url, state = linkedin.authorization_url(self.auth_base_url)
        self.linkedin = linkedin
        return authorization_url

    def linkedin_fetch(self, redirect_response):
        linkedin = self.linkedin
        linkedin.fetch_token(token_url, client_secret=self.client_secret, authorization_response=self.redirect_response)
        r = linkedin.get('https://api.linkedin.com/v1/people/~')
        return r.content

if __name__ == '__main__':
    Linkedin(tokens).login()