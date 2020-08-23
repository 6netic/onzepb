
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User



class MyBackend(BaseBackend):
	""" truc muche """



	def authenticate(self, request, username=None, password=None):
		""" Checks the email and password and then returns a user """
		
		try:
			user = User.objects.get(email=username)
			if user.check_password(raw_password = password):
				return user
			return None
		except User.DoesNotExist:
			return None


	def get_user(self, id):
		"""Doit représenter un champ constituant la clé primaire"""
		
		try:
			return User.objects.get(pk=id)
		except User.DoesNotExist:
			return None



