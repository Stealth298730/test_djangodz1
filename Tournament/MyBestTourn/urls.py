from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tournaments/", views.get_tournaments, name="get_tournaments"),
    path("tournaments/add/", views.add_tournament, name="add_tournament"),
    path("teams/", views.get_teams, name="get_teams"),
    path("teams/add/", views.add_team, name="add_team"),
]
