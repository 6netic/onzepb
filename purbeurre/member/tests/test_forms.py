
from django.test import TestCase
from ..forms import *


class MemberFormTest(TestCase):


	def setUp(self):

		self.form = MemberForm()


	def test_member_form_field_labels(self):
		""" - Testing labels in Member form """
		
		self.assertTrue(self.form.fields['username'].label == "Nom d'utilisateur")
		self.assertTrue(self.form.fields['email'].label == "Adresse Email")
		self.assertTrue(self.form.fields['password'].label == "Mot de passe")


	def test_member_form_field_widgets(self):
		""" - Testing widgets in Member form """

		self.assertEqual(self.form.fields['username'].widget.__class__.__name__, 'TextInput')
		self.assertEqual(self.form.fields['email'].widget.__class__.__name__, 'EmailInput')
		self.assertEqual(self.form.fields['password'].widget.__class__.__name__, 'PasswordInput')


	def test_member_form_field_maxlength(self):
		""" - Testing maxlength fields in Member form """

		self.assertEqual(self.form.fields['username'].max_length, 30)
		self.assertEqual(self.form.fields['email'].max_length, 30)
		self.assertEqual(self.form.fields['password'].max_length, 32)


	def test_member_form_field_required(self):
		""" - Testing required fields in Member form """

		self.assertTrue(self.form.fields['username'].required == True)
		self.assertTrue(self.form.fields['email'].required == True)
		self.assertTrue(self.form.fields['password'].required == True)



class ConnectionFormTest(TestCase):


	def setUp(self):

		self.form = ConnectionForm()


	def test_connection_form_field_labels(self):
		""" - Testing labels in Connection form """

		self.assertTrue(self.form.fields['email'].label == "Adresse Email")
		self.assertTrue(self.form.fields['password'].label == "Mot de passe")


	def test_connection_form_field_widgets(self):
		""" - Testing widgets in Connection form """

		self.assertEqual(self.form.fields['email'].widget.__class__.__name__, 'TextInput')
		self.assertEqual(self.form.fields['password'].widget.__class__.__name__, 'PasswordInput')
		self.assertEqual(self.form.fields['redirection'].widget.__class__.__name__, 'HiddenInput')



class ChangePasswordFormTest(TestCase):


	def setUp(self):

		self.form = ChangePasswordForm()

	
	def test_changepassword_form_field_labels(self):
		""" - Testing widgets in ChangePassword form """

		self.assertTrue(self.form.fields['old_password'].label == "Entrez l'ancien mot de passe")
		self.assertTrue(self.form.fields['new_password1'].label == "Entrez le Nouveau mot de passe")
		self.assertTrue(self.form.fields['new_password2'].label == "Retapez le Nouveau mot de passe")
		

	def test_changepassword_form_field_widgets(self):
		""" - Testing labels in ChangePassword form """

		self.assertEqual(self.form.fields['old_password'].widget.__class__.__name__, 'PasswordInput')
		self.assertEqual(self.form.fields['new_password1'].widget.__class__.__name__, 'PasswordInput')
		self.assertEqual(self.form.fields['new_password2'].widget.__class__.__name__, 'PasswordInput')


	












