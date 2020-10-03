
from django.test import TestCase
from ..models import *

class MemberModelTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# Set up non-modified objects used by all test methods
		PbUser.objects.create(
								username="Davy",
								email="david.reit@internet.com",
								password="myPass4665"
		)


	def test_user_name_label(self):
		""" - Testing if User table has correct field names """

		usr = PbUser.objects.get(id=1)
		# Username field
		label_name = usr._meta.get_field('username').verbose_name
		self.assertEqual(label_name, 'Utilisateur')
		# Email field
		label_name = usr._meta.get_field('email').verbose_name
		self.assertEqual(label_name, 'Adresse Email')
		# Password field
		label_name = usr._meta.get_field('password').verbose_name
		self.assertEqual(label_name, 'mot de passe')


	def test_user_field_max_length(self):
		""" - Testing length of fields in User table """
		
		# Testing length of username field
		usr = PbUser.objects.get(id=1)
		max_length = usr._meta.get_field('username').max_length
		self.assertEqual(max_length, 30)
		# Testing length of password field		
		max_length = usr._meta.get_field('password').max_length
		self.assertEqual(max_length, 128)
		# Testing length of email field		
		max_length = usr._meta.get_field('email').max_length
		self.assertEqual(max_length, 255)


	def test_user_field_type(self):
		""" - Testing if email field is unique """

		usr = PbUser.objects.get(id=1)
		usr_type = usr._meta.get_field('email').unique
		self.assertEqual(usr_type, True)































