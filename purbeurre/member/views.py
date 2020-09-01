#from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser, UserManager
from .models import PbUser#, PbUserManager

from django.shortcuts import render
from .forms import MemberForm
from .forms import ConnectionForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.db import IntegrityError

def account(request):
	""" leads to member page """

	return render(request, 'member/account.html')

def register(request):
	""" This method is in charge of creating a new user in the database """

	form = MemberForm(request.POST or None)
	# Checking whether entered values from the formular are correct
	if form.is_valid():
		try:
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = PbUser.objects.create_user(
												username=username,
												email=email,
												password=password,
											)
			sending = 'ok'
		
		except IntegrityError:
			sending = 'nok'
		return render(request, 'member/register.html', locals())
	
	# if not in POST method then display the formular
	return render(request, 'member/register.html', locals())


def connect(request):
	""" This function connect a user to the system """
	
	if request.method == 'GET':
		redirection = request.GET.get('next')
		#print("La valeur de redirection est :" + redirection)	
	
	error = False
	if request.method == 'POST':
		form = ConnectionForm(request.POST)
		redirection = form["redirection"].value()
		#print("La valeur de redirection est :" + redirection)

		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]			
			user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
			if user:  # Si l'objet renvoyé n'est pas None
				login(request, user)  # nous connectons l'utilisateur
				#In case it's not a redirection
				if redirection != 'None':
					return redirect(redirection)
			else: # else an error will be displayed
				error = True
	else:
		form = ConnectionForm()
	
	return render(request, 'member/connection.html', locals())


def disconnect(request):
	""" This function disconnects a user to the system """

	logout(request)
	return render(request, 'member/disconnection.html', locals())
	#return redirect(reverse(connect))





















