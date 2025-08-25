from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=10)

class Team(models.Model):
    name = models.CharField(max_length=20)

class Tournament(models.Model):
    name = models.CharField(max_length=10)
    bio  = models.CharField(max_length=15,blank=True, null=True, default="")
    teams = models.ManyToManyField(Team, related_name='tournaments', blank=True,)
