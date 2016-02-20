
from django.db import models
from django.conf import settings


class LinkedinUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    access_token = models.CharField(max_length=200)

    def __str__(self):
        return 'LinkedinUser' or None


class FacebookUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    access_token = models.CharField(max_length=300)

    def __str__(self):
        return '%s' % user

class GoogleUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    access_token = models.CharField(max_length=300)

    def __str__(self):
        return '%s' % user
