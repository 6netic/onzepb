
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class PbUserManager(BaseUserManager):
	""" Custom user model manager where email is the unique identifiers 
		for authentication instead of usernames. """

	def create_user(self, email, password, **extra_fields):
		""" Create and save a User with the given email and password. """

		if not email:
			raise ValueError("Vous devez rentrer une adresse email.")
		
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields) #rajouter username
		user.set_password(password)
		user.save() # could also be user.save(using=self._db)
		return user


class PbUser(AbstractUser):
	""" This class redifines User model """

	username = models.CharField(
									verbose_name='Utilisateur',
									max_length=30,
								)
	email = models.EmailField(
								verbose_name='Adresse Email',
								max_length=255,
								unique=True,
							)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = PbUserManager()

	def __str__(self):
		return self.email












