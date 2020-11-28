
from .models import PbUser
from django.shortcuts import render
from .forms import *
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


def modifypassword(request):
	""" This function modifies user's password """

	# This is a POST request so we need to process the form data
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			try:
				former_password = form.cleaned_data['old_password']
				new_password1 = form.cleaned_data['new_password1']
				new_password2 = form.cleaned_data['new_password2']

				if request.user.check_password(former_password):
					if new_password1 == new_password2:
						print(request.user.email)
						u = PbUser.objects.get(email=request.user.email)
						u.set_password(new_password2)
						u.save()
						
						return render(request, 'member/passwordmodified.html')

					else:
						# Only former password is correct
						resp = "onlyformer"
					
				else:
					# Former password is false and new password is not the same in both fields
					resp = "none"

			except:
				# Datas transmitted cannot be taken into account
				resp = "data_error"

			return render(request, 'member/modifypassword.html', locals())
	
	else:
		# First time the form is loaded
		form = ChangePasswordForm()

	return render(request, 'member/modifypassword.html', {'form': form})
	


















