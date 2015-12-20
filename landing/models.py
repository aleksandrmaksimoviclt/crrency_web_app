from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)


