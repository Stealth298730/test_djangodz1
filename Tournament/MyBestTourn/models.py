from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=10)


class Team(models.Model):
    name = models.CharField(max_length=20)

class Tournament(models.Model):
    first_name = models.CharField(max_length=10)
    date  = models.CharField(max_length=15)