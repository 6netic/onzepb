
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .models import *



class IndexPageTestCase(TestCase):
	""" Tests if index page returns 200 """

	def test_index_page(self):
		response = self.client.get(reverse('homepage'))
		self.assertEqual(response.status_code, 200)


class LegalPageTestCase(TestCase):
	""" Tests if legal page returns 200 """

	def test_legal_page(self):
		response = self.client.get(reverse('food:legal'))
		self.assertEqual(response.status_code, 200)


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
'''    

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



class SearchPageTestCase(TestCase):
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
	
	def test_search_page_returns_200(self):
		""" ................. """		

		#tester GET /food/search?search_word=nutella
		c = Client()
		c.get('/food/search', {'search_word': 'ornicus'})
		#prod = Product.objects.get(name="Produit1")
		#product_id = prod.id
		response = self.client.get(reverse('food:detail'))
		self.assertEqual(response.status_code, 200)







'''
impossible = Album.objects.create(title="Transmission Impossible")
album_id = Album.objects.get(title='Transmission Impossible').id
response = self.client.get(reverse('store:detail', args=(album_id,)))
self.assertEqual(response.status_code, 200)
'''
    # test that detail page returns a 404 if the item does not exist.


# Result page
	# test that result page returns 200 if the product exists
    # test that result page returns 404 if the product does not exist

# Detail page
	# test that detail page...
'''
class DetailPageTestCase(TestCase):
	""" ......."""

	def test_detail_page(self):
		truc = self.client.get(reverse('detail'))
		self.assertEqual(truc.status_code, 200)
'''

# Favourite page
	# test that a new product is registered
    # test that a new product belongs to a user
    # test that a new product belongs to a user is not registered twice


# Legal page
'''
class LegalPageTestCase(TestCase):
	""" test that legal page returns 200 """

	def test_legal_page(self):
		responses = self.client.get(reverse('date'))
		self.assertEqual(responses.status_code, 200)
'''
