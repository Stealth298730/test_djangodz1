from django.urls import path

from .import views

urlpatterns = [
    path("",views.index, name="index"),
    path("add_tournament/",views.add_tournament,name="add_tournament"),
    path("get_tournaments/",views.get_tournaments,name="get_tournaments"),
    path("get_teams/",views.get_teams,name="get_teams"),
    path("add_team/",views.add_team,name="add_team")
]
