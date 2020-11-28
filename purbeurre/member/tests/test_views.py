from django.test import TestCase
from django.http import HttpResponse
from django.http import HttpRequest
from django.test import Client
from django.urls import reverse
from django.urls import resolve
from ..models import *
from ..views import *


class MemberViewPageTestCase(TestCase):
	""" Testing all views from Member Application """


	def setUp(self):
		""" Initiate elements """

		# Instanciate Client class to simulate http requests
		self.client = Client()
		# Create a user
		PbUser.objects.create_user(
								username="John", 
								email="fake_email@adibou.com",
								password="Pass123"
							)
			
	
	#Accountpage ----------------------------------------------
	def test_account_url_resolves_to_account_view(self):
		""" - Testing if account url points to accountpage view """

		url = resolve('/member/account')
		self.assertEqual(url.func, account)

	
	def test_if_accountpage_contains_correct_elements(self):
		""" - Testing if accountpage view returns correct elements """

		#  Getting accountpage view
		url = reverse('member:account')
		#  Getting HttpResponse
		response = self.client.get(url)
		# Getting content of account page
		html = response.content.decode('utf8')
		# Checking if status code is 200
		self.assertEqual(response.status_code, 200)
		# Checking if template used is account.html
		self.assertTemplateUsed(response, 'member/account.html')

		# Checking if 'Espace Membres' is displayed when user is not logged in
		self.assertIn('<p class="nameprd">Espace membres</p>', html)
		# Checking if 'Se Connecter' is displayed when user is not logged in
		self.assertIn('<a href="/member/connect">Se connecter</a>', html)
		# Checking if 'Créer un compte' is displayed when user is not logged in
		self.assertIn('<a href="/member/register">Créer un compte</a>', html)

		# Retrieving user email
		user = PbUser.objects.get(email="fake_email@adibou.com")
		# Authenticating user
		auth = self.client.login(username=user, password="Pass123")
		# Getting HttpResponse
		response = self.client.get(reverse('member:account'))
		# Getting content of account page
		html = response.content.decode('utf8')		
		# Checking if username is displayed when user is logged in
		self.assertIn('<p class="nameprd">John</p>', html)
		# Checking if user email is displayed when user is logged in
		self.assertIn('<h6 style="color: white;">Email : <i>fake_email@adibou.com</i></h6>', html)
		# Checking if 'Se déconnecter' is displayed when user is logged in
		self.assertIn('<a href="/member/disconnect">Se déconnecter</a>', html)
		# Checking if 'Modifier son mot de passe' is displayed when user is logged in
		self.assertIn('<a href="/member/modifypassword">Modifier son mot de passe</a>', html)

	
	#Registerpage ----------------------------------------------
	def test_register_url_resolves_to_register_view(self):
		""" - Testing if register url points to registerpage view """

		url = resolve('/member/register')
		self.assertEqual(url.func, register)


	def test_if_registerpage_contains_correct_elements(self):
		""" - Testing if registerpage view returns correct elements """

		#  Getting accountpage view
		url = reverse('member:register')
		#  Getting HttpResponse
		response = self.client.get(url)
		# Getting content of account page
		html = response.content.decode('utf8')
		# Checking if status code is 200
		self.assertEqual(response.status_code, 200)
		# Checking if template used is account.html
		self.assertTemplateUsed(response, 'member/register.html')

		# Testing POST method
		# Counting users before inserting a new one
		user_count_before = PbUser.objects.count()
		# Testing if user details can be sent to register view		
		response = self.client.post(reverse('member:register'), {
													'username':'Derrick',
													'email':'der.frog@email.com',
													'password': 'Password2'
												})
		# Counting users after inserting a new one
		user_count_after = PbUser.objects.count()
		# Testing if new favourite is added in Favourite DB
		self.assertEqual(user_count_after, user_count_before + 1)

		# Getting content of register page
		html = response.content.decode('utf8')
		# Checking if confirmation message is displayed
		self.assertIn("<strong>L'utilisateur Derrick a bien été enregistré. Merci.</strong>", html)

		#Checking if duplicate entry is detected
		response = self.client.post(reverse('member:register'), {
													'username':'Patrick',
													'email':'fake_email@adibou.com',
													'password': 'MoPthu45'
												})
		html = response.content.decode('utf8')
		self.assertIn('<strong>Choisissez une autre adresse email car celle-ci est déjà enregistrée.</strong>', html)
	

	#Connectpage ----------------------------------------------
	def test_connect_url_resolves_to_connect_view(self):
		""" - Testing if connect url points to connectpage view """

		url = resolve('/member/connect')
		self.assertEqual(url.func, connect)

	
	def test_if_connectpage_contains_correct_elements(self):
		""" - Testing if registerpage view returns correct elements """

		#  Getting accountpage view
		url = reverse('member:connect')
		#  Getting HttpResponse
		response = self.client.get(url)
		# Checking if status code is 200
		self.assertEqual(response.status_code, 200)
		# Checking if template used is account.html
		self.assertTemplateUsed(response, 'member/connection.html')

		# Testing GET method
		response = self.client.get(reverse('member:connect'), {'next':'donuts'})
		self.assertEqual(response.status_code, 200)

		# Testing POST method
		# Checking if success message is displayed when credentials are correct
		auth = self.client.login(username='fake_email@adibou.com', password="Pass123")	
		response = self.client.post(reverse('member:connect'), { 'auth': auth })
		html = response.content.decode('utf8')
		self.assertIn('<strong>Vous êtes connecté en tant que John !</strong>', html)
		# Checking if error message is displayed when credentials are not correct
		response = self.client.post(reverse('member:connect'), { 
																'email':'pascal@email.com',
																'password':'Pass234',
																 })													
		html = response.content.decode('utf8')		
		self.assertIn('<strong>Utilisateur inconnu ou mauvais de mot de passe.</strong>', html)


	#Disconnectpage ----------------------------------------------
	def test_disconnect_url_resolves_to_disconnect_view(self):
		""" - Testing if disconnect url points to disconnectpage view """

		url = resolve('/member/disconnect')
		self.assertEqual(url.func, disconnect)


	def test_if_disconnectpage_contains_correct_elements(self):
		""" - Testing if disconnectpage view returns correct elements """

		# Getting disconnectpage view
		url = reverse('member:disconnect')
		# Getting HttpResponse
		response = self.client.get(url)
		# Getting if status code is 200
		self.assertEqual(response.status_code, 200)
		# Checking if template used is disconnect.html
		self.assertTemplateUsed(response, 'member/disconnection.html')
	

	#ModifyPasswordpage ----------------------------------------------
	def test_modifypassword_url_resolves_to_modifypassword_view(self):
		""" - Testing if modifypassword url points to modifypassword view """

		url = resolve('/member/modifypassword')
		self.assertEqual(url.func, modifypassword)


	def test_if_modifypasswordpage_contains_correct_elements(self):
		""" - Testing if modifypasswordpage view returns correct elements """

		#  Getting modifypasswordpage view
		url = reverse('member:modifypassword')
		#  Getting HttpResponse
		response = self.client.get(url)
		# Checking if status code is 200
		self.assertEqual(response.status_code, 200)
		# Checking if template used is account.html
		self.assertTemplateUsed(response, 'member/modifypassword.html')

		# Testing GET method
		response = self.client.get(reverse('member:modifypassword'))
		self.assertEqual(response.status_code, 200)



