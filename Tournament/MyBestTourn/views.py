from django.shortcuts import render, redirect
from .forms import TournamentForm,TeamForm,ContactForm
from .models import Tournament,Team,Contact

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout



# Create your views here.






def index(request):
    context = {
        "tournaments" : [
        {
        
            "name":"Міжнародний",
        },
        {
            "name":"По шахам",

        },
        {
            "name":"Спортивний",
        },
    ]}
    return render(request=request,template_name="index.html",context=context)

def add_team(request):
    if request.method != "POST":
        form = TeamForm()
        return render(request=request,template_name="add_team.html",context=dict(form=form))

    form = TeamForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        team = Team(name=name)
        team.save()
        return redirect("get_teams")
    
def get_teams(request):
    teams = Team.objects.all()
    return render(request=request, template_name ="get_teams.html",context=dict(teams=teams))

def add_tournament(request):
    if request.method == "POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            bio = form.cleaned_data['bio']
            teams = form.cleaned_data['teams']
            tournament = Tournament.objects.create(name=name, bio=bio)
            tournament.teams.set(teams)

            return redirect("get_tournaments")
    else:
        form = TournamentForm()
    return render(request, "add_tournament.html", {"form": form})


def get_tournaments(request):
    return render(
        request=request,
        template_name="get_tournaments.html",
        context=dict(tournaments=Tournament.objects.all())
    )
