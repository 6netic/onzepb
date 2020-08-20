from django import forms


class MemberForm(forms.Form):
	""" This class creates a form to register a new member """

	firstname = forms.CharField(label="Prénom", min_length=2, max_length=30, widget=forms.TextInput, required=True)
	lastname = forms.CharField(label="Nom", min_length=2, max_length=30, widget=forms.TextInput, required=True)
	email = forms.EmailField(label="Adresse Email", widget=forms.EmailInput, required=True)
	password = forms.CharField(label="Mot de passe", max_length=32, widget=forms.PasswordInput, required=True)
	#password = forms.CharField(label="Mot de passe", max_length=32, widget=forms.PasswordInput) Second entry
