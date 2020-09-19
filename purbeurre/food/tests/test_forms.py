from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpRequest
from django.urls import resolve
from ..views import *
from ..models import *




# Tester si le formulaire pointe bien vers le bon url

# Tester le type d'envoi

# Tester le type accept-charset

# Tester l'absence du bouton ou de la baslise submit

# Dans la balise input, tester que le placeholder vaut bien "Chercher"

# Dans la balise input, tester que l'attribut name vaut bien "search_word"

class SearchFormCase(TestCase):


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
		
		# Creating a favourite product		
		Favourite.objects.create(
							former_barcode='000123', 
							favourite_barcode='000124', 
							email_user = "fake_email@adibou.com"
					)		

	def test_(self):
		""" - Testing ... """

		client = Client()
		#search_word = "bojjou"
		response = self.client.get(reverse('food:search'), {'search_word':'Produit1'})
		#response = client.get('/food/search/', args=(search_word="ghjk",))
		print(response)



		