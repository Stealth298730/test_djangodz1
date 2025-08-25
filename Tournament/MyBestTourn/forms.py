# forms.py
from django import forms
from .models import Team

class TeamForm(forms.Form):
    name = forms.CharField(
        label="Назва команди",
        widget=forms.TextInput(attrs={"class":"form-control"})
        )


class TournamentForm(forms.Form):
    name = forms.CharField(
        label="Назва турніру",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    bio = forms.CharField(
        label="Опис",
        widget=forms.Textarea(attrs={"class": "form-control"})
    )
    teams = forms.ModelMultipleChoiceField(
        label="Команди",
        queryset=Team.objects.all(),
        widget=forms.SelectMultiple(attrs={"class": "form-select"})
    )
