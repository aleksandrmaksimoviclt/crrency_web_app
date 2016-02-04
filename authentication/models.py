
from django.db import models
from django.conf import settings


class LinkedinUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    access_token = models.CharField(max_length=200)

    def __str__(self):
        return 'l_user'


class FacebookUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    access_token = models.CharField(max_length=300)

    def __str__(self):
        return 'fb_user'