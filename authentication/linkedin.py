#!/usr/bin/env python
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix


client_id = '77zdi1zo7xqmyv'
client_secret = 'mrQZZaFyBBPwREda'
authorization_base_url = 'https://www.linkedin.com/uas/oauth2/authorization'
token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'
redirect_url = 'https://127.0.0.1/'


def login():
    linkedin = OAuth2Session(client_id, redirect_uri='http://127.0.0.1')
    linkedin = linkedin_compliance_fix(linkedin)
    authorization_url, state = linkedin.authorization_url(authorization_base_url)
    print('Please go here and authorize,', authorization_url)
    redirect_response = input('Paste the full redirect URL here:')
    linkedin.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)
    r = linkedin.get('https://api.linkedin.com/v1/people/~')
    print(r.content)


if __name__ == '__main__':
    login()