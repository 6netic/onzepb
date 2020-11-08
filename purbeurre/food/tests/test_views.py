from django.test import TestCase
from django.http import HttpResponse
from django.http import HttpRequest
from django.test import Client
from django.urls import reverse
from django.urls import resolve
from ..models import *
from ..views import *
from member.models import *


class FoodViewPageTestCase(TestCase):
	""" Testing all views from Food Application """

	
	def setUp(self):
		""" Initiate elements """

		# Instanciate Client class to simulate http requests
		self.client = Client()
		# Create and populate Category table
		fake_category_list = ["cat1", "cat2", "cat3"]
		for cat in fake_category_list:
			Category.objects.create(name=cat)
		# Create and populate Product table
		related_cat = Category.objects.get(name="cat1")
		fake_product_list = [
			['Produit1', 'Desc1', 'a', '000123', 'https://web.fr', 'https://stat/1.jpg', 'Magasin', 1, 4, 0, 0, 0.0275], 
			['Produit2', 'Desc2', 'b', '000124', 'https://web.fr', 'https://stat/2.jpg', 'Magasin', 1, 0, 0, 0, 0.02] 
		]		
		lines = len(fake_product_list)
		for i in range(lines):
			Product.objects.create(
									name=fake_product_list[i][0], 
									description=fake_product_list[i][1], 
									nutrition_grade=fake_product_list[i][2],
									barcode=fake_product_list[i][3],
									url=fake_product_list[i][4], 
									url_pic=fake_product_list[i][5], 
									store=fake_product_list[i][6],
									fat=fake_product_list[i][8],
									saturated_fat=fake_product_list[i][9],
									sugar=fake_product_list[i][10],
									salt=fake_product_list[i][11],
									prd_cat=related_cat
								)
		# Create a user
		PbUser.objects.create_user(
								username="John", 
								email="fake_email@adibou.com",
								password="myPassword"
							)
		# Creating a favourite product		
		Favourite.objects.create(
							former_barcode='000123', 
							favourite_barcode='000124', 
							email_user = "fake_email@adibou.com"
					)		

	
	#Homepage ----------------------------------------------
	def test_root_url_resolves_to_homepage_view(self):
		""" - Testing if homepage url points to homepage view """

		url = resolve('/')
		self.assertEqual(url.func, homepage)


	def test_food_url_resolves_to_homepage_view(self):
		""" - Testing if /food/ url points to homepage view """
		
		url = resolve('/food/')
		self.assertEqual(url.func, homepage)

	
	def test_homepage_contains_correct_elements(self):
		""" - Testing if homepage view returns correct elements """

		# Getting homepage view
		url = reverse('homepage')
		# Getting HttpResponse
		response = self.client.get(url)
		# Checking if status code is 200
		self.assertEqual(response.status_code, 200)
		# Checking if template used is index.html
		self.assertTemplateUsed(response, 'food/index.html')
		# Getting content of index page
		html = response.content.decode('utf8')
		# Checking if Bootstrap CSS is present
		self.assertIn('<link href="/static/food/css/styles.css" rel="stylesheet" />', html)
		# Checking if logo image is present
		self.assertIn('<img id="logo" src="/static/food/assets/img/logo.png" alt="Pur Beurre Logo">', html)
		# Checking if logo image and website name redirect to homepage
		self.assertIn('<a class="navbar-brand" href="/food/">', html)
		#self.assertIn('<img id="logo" src="/static/assets/img/logo.png" alt="Pur Beurre Logo">', html)
		self.assertIn('<span>Pur Beurre</span>', html)
		self.assertIn('</a>', html)
		# Checking if search form is present and redirects to search view
		self.assertIn('<form action="/food/search" method="get" accept-charset="utf-8">', html)                          
		self.assertIn('<input type="text" class="form-control" placeholder="Chercher" name="search_word">', html)
		self.assertIn('</form>', html)
		# Checking if member icon is present when user is not logged in
		self.assertIn('<img class="headicons" src="/static/member/assets/img/account_icon.png" alt="My Account">', html)
		# Checking if legal mentions are present and redirect to legal view
		self.assertIn('<a href="/food/legal" style="color: black;">Mentions légales</a>', html)

	
	#legal page ----------------------------------------------
	def test_legal_url_resolves_to_legal_view(self):
		""" - Testing if legal page url points to legal page view """

		url = resolve('/food/legal')
		self.assertEqual(url.func, legal)
		

	def test_legal_contains_correct_elements(self):
		""" - Testing if legal view returns correct elements """

		# Getting legal page view
		url = reverse('food:legal')
		# Getting HttpResponse
		response = self.client.get(url)
		# Checking if status code is 200
		self.assertEqual(response.status_code, 200)
		# Checking if template used is legal.html
		self.assertTemplateUsed(response, 'food/legal.html')

	
	#search page ----------------------------------------------
	def test_search_url_resolves_to_search_view(self):
		""" - Testing if search page url points to search view """

		url = resolve('/food/search')
		self.assertEqual(url.func, search)


	def test_search_contains_correct_elements(self):
		""" - Testing if search view returns correct elements """

		# Retrieving search products
		fake_search_word = 'Produit2'		
		fake_prd = Product.objects.get(name=fake_search_word)		
		# Checking if status code is 200 (product found)
		response = self.client.get(reverse('food:search'), {'search_word':'Produit2'})
		self.assertEqual(response.status_code, 200)
		# Checking if template used is result.html
		self.assertTemplateUsed(response, 'food/result.html')		
		# Checking if status code is 404 (product not found)
		response = self.client.get(reverse('food:search'), {'search_word':'Produit12'})
		self.assertEqual(response.status_code, 404)
		# Checking if template used is 404.html
		self.assertTemplateUsed(response, '404.html')

	
	#detail page ----------------------------------------------
	def test_detail_url_resolves_to_detail_view(self):
		""" - Testing if detail page url points to detail view """

		url = resolve('/food/detail/15')
		self.assertEqual(url.func, detail)


	def test_detail_contains_correct_elements(self):
		""" - Testing if detail view returns correct elements """

		# Retrieving one product with its id
		fake_prd_id = Product.objects.get(name="Produit1").id
		# Checking if status code is 200 (product found)
		response = self.client.get(reverse('food:detail', args=(fake_prd_id,)))
		self.assertEqual(response.status_code, 200)
	

	#save product page ----------------------------------------------
	def test_save_url_resolves_to_save_view(self):
		""" - Testing if detail page url points to detail view """

		url = resolve('/food/saveprd/')
		self.assertEqual(url.func, saveprd)
	
	
	def test_product_is_saved(self):
		""" - Testing if a product is registered when user is logged in """

		# Counting elements before inserting a new product
		fav_count_before = Favourite.objects.count()		
		# Retrieving required elements		
		fake_old_prd_barcode = Product.objects.get(name="Produit1").barcode
		fake_new_prd_barcode = Product.objects.get(name="Produit2").barcode
		fake_user = PbUser.objects.get(email="fake_email@adibou.com")
		# user is connected (returns True)		
		auth = self.client.login(username=fake_user, password="myPassword")		
		# Testing if incoming request (from search view) can be sent to saveprd view		
		response = self.client.get(reverse('food:saveprd'), {
													'former_barcode':fake_new_prd_barcode,
													'new_barcode':fake_old_prd_barcode,
													'email': fake_user
												})
		# Counting elements after inserting a new product
		fav_count_after = Favourite.objects.count()
		# Testing if new favourite is added in Favourite DB
		self.assertEqual(fav_count_after, fav_count_before + 1)
		
	
	# showfavourites page ----------------------------------------------
	def test_showfavourites_url_resolves_to_showfavourites_view(self):
		""" - Testing if favourite page url points to showfavourites view """

		url = resolve('/food/showfavourites')
		self.assertEqual(url.func, showfavourites)


	def test_showfavourites_contains_correct_elements(self):
		""" - Testing if showfavourites view returns correct elements """

		# Retrieving user email
		user = PbUser.objects.get(email="fake_email@adibou.com")
		# Authenticating user
		auth = self.client.login(username=user, password="myPassword")
		# Testing if response is ok for showfavourites view
		response = self.client.get(reverse('food:showfavourites'))
		self.assertEqual(response.status_code, 200)

	
