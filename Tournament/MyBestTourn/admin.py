from django.contrib import admin

from .models import Team,Subject,Tournament
# Register your models here.
admin.site.register([Tournament,Subject,Team])