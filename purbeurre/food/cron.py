import requests
from .models import *
from random import randint


def my_scheduled_job():

	# List of categories
	categories = [
		"Boissons", "Viandes", "Biscuits", "Fromages", "Desserts", "Snacks", "Charcuteries",
		"Epicerie", "Petit-déjeuners", "Céréales et dérivés", "Sauces", "Produits de la mer", 
		"Confiseries", "Volailles", "Légumes et dérivés", "Surgelés", "Conserves", "Poissons",
		"Boissons alcoolisées", "Poulets", "Gâteaux", "Pains", "Yaourts", "Confitures",
		"Jus de fruits", "Graines", "Vins", "Huiles", "Fruits", "Pâtisseries", "Miels", "Pizzas",
		"Soupes", "Bonbons", "Chips", "Saucissons", "Bières", "Sirops", "Compotes", "Laits", "Thés"
	]

	# Populating Product table		
	category_six = []
	# Choose 6 random products from list 'categories'
	for c in range(6):
		categ = randint(0, len(categories)-1)
		pop_categ = categories[categ]
		category_six.append(pop_categ)
		del categories[categ]

	entire_list = []

	# Trying to extract 50 products from each of the 6 categories
	for category in category_six:	
		payload = {
			"action": "process",
			"tagtype_0": "categories",
			"tag_contains_0": "contains",
			"tag_0": category,
			"page_size": "50",
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
				products_list.append(Category.objects.get(name=category).id)
				products_list.append(my_product["nutriments"]["fat_100g"])
				products_list.append(my_product["nutriments"]["saturated-fat_100g"])
				products_list.append(my_product["nutriments"]["sugars_100g"])
				products_list.append(my_product["nutriments"]["salt_100g"])
			
			# If required field is missing, go to next product	
			except KeyError:
				pass

			# Then append it to the list
			else:			
				entire_list.append(products_list)
				i += 1
				
				if i == 50:
					break

	# Retrieving number of entries in entire_list list
	lines = len(entire_list)
	print("Number of products extracted from OFF API: ", lines)

	# Inserting lines in Product table
	t = 0
	for i in range(lines):
		try:	
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
			t += 1

		except:
			continue

	print("Number of products added in table 'Product': ", t)


