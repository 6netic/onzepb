
from .models import PbUser
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
	
	# First access to connection form page
	if request.method == 'GET':
		redirection = request.GET.get('next')	
	error = False

	if request.method == 'POST':
		form = ConnectionForm(request.POST)
		redirection = form["redirection"].value()

		if form.is_valid():
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]			

			user = authenticate(username=email, password=password)
			if user:
				login(request, user)

				if redirection != 'None':
					return redirect(redirection)
			else:
				error = True
	else:
		form = ConnectionForm()
	
	return render(request, 'member/connection.html', locals())


def disconnect(request):
	""" This function disconnects a user to the system """

	logout(request)
	return render(request, 'member/disconnection.html', locals())



