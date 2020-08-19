from model.off import *
from model.connection import *
from model.database import *
from model.category import *
from model.product import *
# from model.category_product import *
# from model.favourite import *
# from view import *


def initiate_app():
	"""Initiating application"""
	
	
	#Connecting to PostgreSQL Server
	db_connection = Connection()
	connection = db_connection.connect_to_dbms()

	#Retrieving database name
	database = db_connection.database
	my_database = db_connection.database
	#print(my_database)

	#Retrieving the category list of products defined by User
	my_category = Category(connection)
	categories = my_category.categories
	#print(categories)
	
	#Extracting datas from OFF Api
	off_datas = OpenFoodFacts(categories)
	entire_list = off_datas.get_categories_from_OFF_api()
	#print(entire_list)
	
	#Initializing the view
	#my_view = View()

	#Creating MySQL database and tables
	# database = my_database.database -On a déjà notre base créée
	#database_creation_result = my_database.create_database()
	#my_view.show_result_creation_database(database_creation_result, database)
	my_database = Database(connection)
	my_database.create_tables()
	
	#my_view.show_result_creation_tables(tables_creation_result)
	#Inserting categories
	my_category.insert_categories()
	#my_view.show_result_insert_categories(insert_data_into_category_result, categories)
	
	#Inserting products
	my_product = Product(connection)
	my_product.insert_products(entire_list)
	'''
	my_view.show_result_insert_products(insert_data_into_product_result, entire_list)
	#Inserting categories_products
	my_category_product = Category_Product(connection)
	result_products, insert_data_into_category_product_result = my_category_product.insert_categories_products()
	my_view.show_result_insert_categories_products(result_products, insert_data_into_category_product_result)
	'''
	
initiate_app()

