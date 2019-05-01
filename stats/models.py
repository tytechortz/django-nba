from django.db import models

# Create your models here.
class Team(models.Model):
    city = models.CharField(max_length=20)
    fullname = models.CharField(max_length=30)
    tricode = models.CharField(max_length=3)
    teamId = models.CharField(max_length=10)
    nickname = models.CharField(max_length=20)
    confName = models.CharField(max_length=4)
    confName = models.CharField(max_length=4)
    divName = models.CharField(max_length=10)
    photo_url = models.TextField()

    def __str__(self):
        return self.nickname

