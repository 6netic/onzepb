
from django.test import TestCase
from django.http import HttpResponse
from django.http import HttpRequest
from django.test import Client
from django.urls import reverse
from django.urls import resolve
from .models import *
from .views import *
from member.models import *

'''
class HomePageTestCase(TestCase):


	def setUp(self):
		""" Initiate elements """

		self.client = Client()


	def test_root_url_resolves_to_homepage_view(self):
		""" Testing resolving URL """

		found = resolve('/')
		self.assertEqual(found.func, homepage)


	def test_food_url_resolves_to_homepage_view(self):
		""" Testing resolving URL """
		
		found = resolve('/food/')
		self.assertEqual(found.func, homepage)


	def test_homepage_contains_correct_elements(self):
		""" Testing Homepage view """

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
		self.assertIn('<link href="/static/css/styles.css" rel="stylesheet" />', html)
		# Checking if logo image is present
		self.assertIn('<img id="logo" src="/static/assets/img/logo.png" alt="Pur Beurre Logo">', html)
		# Checking if logo image and website name redirect to homepage
		self.assertIn('<a class="navbar-brand" href="/food/">', html)
		self.assertIn('<img id="logo" src="/static/assets/img/logo.png" alt="Pur Beurre Logo">', html)
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



class LegalPageTestCase(TestCase):


	def setUp(self):
		""" Initiate elements """

		self.client = Client()


	def test_legal_url_resolves_to_legal_view(self):
		""" Testing if legal view points to the right url """

		#response = self.client.get(reverse('food:legal'))
		#self.assertEqual(response.status_code, 200)
		found = resolve('/food/legal')
		self.assertEqual(found.func, legal)
		

	def test_legal_contains_correct_elements(self):
		""" Testing Legal view """

		# Getting legalpage view
		url = reverse('food:legal')
		# Getting HttpResponse
		response = self.client.get(url)
		# Checking if status code is 200
		self.assertEqual(response.status_code, 200)
		# Checking if template used is legal.html
		self.assertTemplateUsed(response, 'food/legal.html')



class SearchPageTestCase(TestCase):


	def setUp(self):
		
		self.client = Client()

	
	def tearDown(self):

		pass
	

	def test_search_url_resolves_to_search_view(self):
		""" Testing if search view points to the right url """
		
		found = resolve('/food/search')
		self.assertEqual(found.func, search)

	
	def test_search_contains_correct_elements(self):
		""" Testing search view """

		fake_category_list = ["cat1", "cat2", "cat3"]
		for cat in fake_category_list:
			Category.objects.create(name=cat)
				
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
									prd_cat=Category(fake_product_list[i][7])
									)

		# tester la méthode GET
		self.client = Client()
		# Récupération du produit recherché
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
		

class DetailPageTestCase(TestCase):
	
	
	def test_detail_page_returns_200(self):
		""" test that detail page returns a 200 if the item exists. """

		fake_category_list = ["cat1", "cat2", "cat3"]
		for cat in fake_category_list:
			Category.objects.create(name=cat)
				
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
									prd_cat=Category(fake_product_list[i][7])
									)
		
		fake_prd_id = Product.objects.get(name="Produit1").id
		response = self.client.get(reverse('food:detail', args=(fake_prd_id,)))
		self.assertEqual(response.status_code, 200)
		# that test can't return 404 code coz product is always found


class SavePrdPageTestCase(TestCase):


	def setUp(self):
		pass
		

	def test_product_is_saved(self):
		""" - Testing if a product is registered when user is logged in """
		
		client = Client()

		fake_category_list = ["cat1", "cat2", "cat3"]
		for cat in fake_category_list:
			Category.objects.create(name=cat)
				
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
									prd_cat=Category(fake_product_list[i][7])
								)
		
		#Creating a User
		PbUser.objects.create_user(
								username="John", 
								email="fake_email@adibou.com",
								password="myPassword"
							)

		# Counting elements before inserting a new product
		fav_count_before = Favourite.objects.count()
		#print("Number of products in DB before inserting a new one :", fav_count_before)
		# Retrieving required elements
		fake_old_prd_barcode = Product.objects.get(name="Produit1").barcode
		fake_new_prd_barcode = Product.objects.get(name="Produit2").barcode
		fake_user = PbUser.objects.get(email="fake_email@adibou.com")
		auth = client.login(username="fake_email@adibou.com", password="myPassword")
		#print("Request is :", auth) -> returns True
		# Testing if incoming request (from search view) can be sent to saveprd view
		response = client.get(reverse('food:saveprd'), {
														'former_barcode':fake_old_prd_barcode,
														'new_barcode':fake_new_prd_barcode,
														'email': fake_user
														})
		fav_count_after = Favourite.objects.count()
		#print("Number of products in DB after inserting a new one :", fav_count_after)
		# Testing if new favourite is added in Favourite DB
		self.assertEqual(fav_count_after, fav_count_before + 1)
'''

class ShowFavouritesPageTestCase(TestCase):


	def test_favourite_is_saved(self):
		""" - Testing if favourite view contains correct elements when user is logged in """
		
		client = Client()
		#Creating a User
		fake_user = PbUser.objects.create_user(
					username="John", 
					email="fake_email@adibou.com",
					password="myPassword"
							)
		#print(PbUser.objects.count())-> OK 1 user in DB
		
		fake_category_list = ["cat1", "cat2", "cat3"]
		for cat in fake_category_list:
			Category.objects.create(name=cat)
				
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
									prd_cat=Category(fake_product_list[i][7])
								)
		

		# Creating a favourite product		
		Favourite.objects.create(
					former_barcode='000123', 
					favourite_barcode='000124', 
					email_user = "fake_email@adibou.com"
					)		
		#print(PbUser.objects.count()) -> OK 1 favourite in DB

		
		user = PbUser.objects.get(email="fake_email@adibou.com")
		print(user)
		
		auth = client.login(username=user, password="myPassword")
		print(auth)
		
		response = client.get(reverse('food:showfavourites'))
		print(response)
		#self.assertEqual(response.status_code, 200)
		

	'''
	def test_search_page_returns_200(self):
			""" ................. """		
			#album_id = Album.objects.get(title='Transmission Impossible').id
			#fake_product = Product.objects.get(name="Produit7")
			#word = "Produit7"
			response = self.client.get(reverse('food:listing'))
			self.assertEqual(response.status_code, 200)

	    # test that detail page returns a 404 if the item does not exist.

	def test_search_page_returns_200(self):
			""" ................. """		

			#tester GET /food/search?search_word=nutella
			c = Client()
			c.get('/food/search', {'search_word': 'ornicus'})
			#prod = Product.objects.get(name="Produit1")
			#product_id = prod.id
			response = self.client.get(reverse('food:detail'))
			self.assertEqual(response.status_code, 200)

	impossible = Album.objects.create(title="Transmission Impossible")
	album_id = Album.objects.get(title='Transmission Impossible').id
	response = self.client.get(reverse('store:detail', args=(album_id,)))
	self.assertEqual(response.status_code, 200)

	    # test that detail page returns a 404 if the item does not exist.
	'''

# Result page
	# test that result page returns 200 if the product exists
    # test that result page returns 404 if the product does not exist

	
'''



class SearchPageTestCase(TestCase):
	""" If search page returns 200 then the product is found """

	def setUp(self):
		fake_category_list = ["cat1", "cat2", "cat3", "cat4", "cat5", "cat6", "cat7"]
		for cat in fake_category_list:
			Category.objects.create(name=cat)


		fake_product_list = [
		['Produit1', 'Desc1', 'a', '000123', 'https://web.fr', 'https://stat/1.jpg', 'Magasin', 1, 4, 0, 0, 0.0275], 
		['Produit2', 'Desc2', 'b', '000124', 'https://web.fr', 'https://stat/2.jpg', 'Magasin', 1, 0, 0, 0, 0.02], 
		['Produit3', 'Desc3', 'a', '000125', 'https://web.fr', 'https://stat/3.jpg', 'Magasin', 1, 0, 0, 0, 0.0222], 
		['Produit4', 'Desc4', 'a', '000126', 'https://web.fr', 'https://stat/4.jpg', 'Magasin', 1, 0, 0, 0, 0.00127], 
		['Produit5', 'Desc5', 'a', '000127', 'https://web.fr', 'https://stat/5.jpg', 'Magasin', 1, 0, 0, 0, 0.00361], 
		['Produit6', 'Desc6', 'b', '000128', 'https://web.fr', 'https://stat/6.jpg', 'Magasin', 1, 3, 1.5, 75, 0.4], 
		['Produit7', 'Desc8', 'c', '000129', 'https://web.fr', 'https://stat/7.jpg', 'Magasin', 1, 0, 0, 8.9, 0]
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
									prd_cat=Category(fake_product_list[i][7])
									)


	def test_search_page_returns_200(self):
		""" ................. """		
		#album_id = Album.objects.get(title='Transmission Impossible').id
		#fake_product = Product.objects.get(name="Produit7")
		#word = "Produit7"
		response = self.client.get(reverse('food:listing'))
		self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item does not exist.
    

class DetailPageTestCase(TestCase):
	""" If search page returns 200 then the product is found """

	def setUp(self):
		
		fake_category_list = ["cat1", "cat2", "cat3"]
		for cat in fake_category_list:
			Category.objects.create(name=cat)
				
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
									prd_cat=Category(fake_product_list[i][7])
									)	
	
	def test_detail_page_returns_200(self):
		""" ................. """		

		prod = Product.objects.get(name="Produit1")
		product_id = prod.id
		response = self.client.get(reverse('food:detail', args=(product_id,)))
		self.assertEqual(response.status_code, 200)



# Result page
	# test that result page returns 200 if the product exists
    # test that result page returns 404 if the product does not exist

# Detail page
	# test that detail page...

class DetailPageTestCase(TestCase):
	""" ......."""

	def test_detail_page(self):
		truc = self.client.get(reverse('detail'))
		self.assertEqual(truc.status_code, 200)


# Favourite page
	# test that a new product is registered
    # test that a new product belongs to a user
    # test that a new product belongs to a user is not registered twice


# Legal page

class LegalPageTestCase(TestCase):
	""" test that legal page returns 200 """

	def test_legal_page(self):
		responses = self.client.get(reverse('date'))
		self.assertEqual(responses.status_code, 200)
'''
