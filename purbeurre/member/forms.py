from django import forms
from django.contrib.auth.models import User


class MemberForm(forms.Form):
	""" This class creates a form to register a new member """

	username = forms.CharField(
								label="Nom d'utilisateur", 
								min_length=2, max_length=30, 
								widget=forms.TextInput, 
								required=True,
								
								)
	email = forms.EmailField(label="Adresse Email", widget=forms.EmailInput, max_length=30, required=True)
	password = forms.CharField(label="Mot de passe", max_length=32, widget=forms.PasswordInput, required=True)


class ConnectionForm(forms.Form):
	""" This class creates a form to authenticate a user """

	email = forms.CharField(label="Adresse Email", widget=forms.TextInput) #widget rajouté!!
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
	redirection = forms.CharField(widget=forms.HiddenInput, required=False)