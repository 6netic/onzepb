
from django.core.management.base import BaseCommand
import requests
from food.models import *


class Command(BaseCommand):
	""" This class will get products from OpenFoodFacts API """

	help = 'Populating Category and Product table'

	
	def handle(self, *args, **options):
				
		# Defining categories list
		categories = ["Boissons", "Viandes", "Biscuits", "Fromages", "Desserts"]
		cat_entries_nb = len(categories)
		
		# Populating Category table
		for cat in categories:
			Category.objects.create(name=cat)		
		print("Number of elements put in Category table: ", cat_entries_nb)
		
		# Populating Product table
		entire_list = []
		for category in categories:	

			payload = {
				"action": "process",
				"tagtype_0": "categories",
				"tag_contains_0": "contains",
				"tag_0": category,
				"page_size": "100",
				"json": "1"
			}
			
			my_request = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
			result = my_request.json()
			my_products = result["products"]

			i = 0
			# Browsing the list of products
			for my_product in my_products:
				
				#Creating a list containing each line of products
				products_list = []

				try:
					products_list.append(my_product["product_name_fr"])
					products_list.append(my_product["generic_name"])
					products_list.append(my_product["nutrition_grades"])
					products_list.append(my_product["code"])
					products_list.append(my_product["url"])
					products_list.append(my_product["image_url"])
					products_list.append(my_product["stores"])
					products_list.append(categories.index(category) + 1)
					products_list.append(my_product["nutriments"]["fat_100g"])
					products_list.append(my_product["nutriments"]["saturated-fat_100g"])
					products_list.append(my_product["nutriments"]["sugars_100g"])
					products_list.append(my_product["nutriments"]["salt_100g"])
					
				except KeyError:
					pass

				else:			
					entire_list.append(products_list)
					i += 1
					
					if i == 100:
						break
			
		# Retrieving number of entries in entire_list list
		lines = len(entire_list)
		# Inserting lines in Product table
		for i in range(lines):
			Product.objects.create(
									name=entire_list[i][0], 
									description=entire_list[i][1], 
									nutrition_grade=entire_list[i][2],
									barcode=entire_list[i][3],
									url=entire_list[i][4], 
									url_pic=entire_list[i][5], 
									store=entire_list[i][6],
									fat=entire_list[i][8],
									saturated_fat=entire_list[i][9],
									sugar=entire_list[i][10],
									salt=entire_list[i][11],
									prd_cat=Category(entire_list[i][7])
								)

		print("Number of entries put in Product table: ",lines)
		













