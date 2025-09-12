# forms.py
from django import forms
from .models import Team,Contact



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

class ContactForm(forms.Form):
    first_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),label="Ім'я")
    last_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),label="Прізвище")
    phone_number=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}),label="Номер телефону")
    email=forms.CharField(max_length=20,required=False,widget=forms.EmailInput(attrs={"class":"form-control"}),label="Електронна адреса")
    address=forms.CharField(max_length=20,required=False,widget=forms.TextInput(attrs={"class":"form-control"}),label="Адреса")
    
    class Meta:
        model=Contact
        fields=("first_name","last_name","phone_number","email","address",)