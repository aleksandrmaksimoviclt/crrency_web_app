from django.db import models
from django.conf import settings 

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    """docstring for Profile"""
    def __init__(self, arg):
        super (Profile, self).__init__()
        self.arg = arg
        