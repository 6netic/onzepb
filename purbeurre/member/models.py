

from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class PbUserManager(BaseUserManager):
	""" Custom user model manager where email is the unique identifiers 
		for authentication instead of usernames. """

	def create_user(self, email, password, **extra_fields):
		""" Create and save a User with the given email and password. """

		# I don't see username field reference so to be checked again
		if not email:
			raise ValueError("Vous devez rentrer une adresse email.")
		
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields) #rajouter username
		user.set_password(password)
		user.save() #otherwise try user.save(using=self._db)
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

'''
Exemple du Tutoriel de Django3 - some notions are missing to make it work

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.
class PbUserManager(BaseUserManager):
	""" This class redefines User class """

	def create_user(self, email, password):
		""" Creates and saves a User with the given email and password """

		if not email:
			raise ValueError("User must have an email address")

		user = self.model(
							email=self.normalize_email(email),
							password= ,
						)

		user.set_password(password)
		user.save(using=self._db)

		return user


class PbUser(AbstractBaseUser):
	""" This class does something """

	email = models.EmailField(
								verbose_name='email address',
								max_length=255,
								unique=True,
							)
	password = models.CharField(
								)

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = PbUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['password']

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does user have specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does user have permissions to view the app 'app_label'?"
		#Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is user a member of staff?"
		#Simplest possible answer: Yes, always
		return self.is_admin
	
'''




















