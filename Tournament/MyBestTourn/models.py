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

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=20,null=True,default=None)
    address=models.CharField(max_length=100,null=True,default=None)
    user = models.ForeignKey("UserManager.MySuperUser",on_delete=models.CASCADE)