
class Product:
	"""This class deals with all database operations"""


	def __init__(self, connection):
		"""Initializing the class with connection details"""
		
		self.connection = connection


	def insert_products(self, entire_list):
		"""This method populates table Product"""

		cursor = self.connection.cursor()
		for line in entire_list:
			sql_command = "INSERT INTO Product(name, description, nutrition_grade, barcode, url, url_pic, store, prd_cat, fat, saturated_fat, sugar, salt) VALUES(%(name)s, %(description)s, %(nutrition_grade)s, %(barcode)s, %(url)s, %(url_pic)s, %(store)s, %(prd_cat)s, %(fat)s, %(saturated_fat)s, %(sugar)s, %(salt)s)"			
			add_product_value = {
							'id': cursor.lastrowid,
							'name': line[0],
							'description': line[1],
							'nutrition_grade': line[2],
							'barcode': line[3],
							'url': line[4],
							'url_pic': line[5],
							'store': line[6],
							'prd_cat': line[7],
							'fat': line[8],
							'saturated_fat': line[9],
							'sugar': line[10],
							'salt': line[11],
							}
			cursor.execute(sql_command, add_product_value)			
		self.connection.commit()
		cursor.close()




	'''
	[
	['Eau de source', 'Eau de source naturelle', 'a', '3274080005003', 'https://fr.openfoodfacts.org/produit/3274080005003/eau-de-source-cristalline', 'Carrefour,auchan,Leclerc', 1, 4, 0, 0, 0.0275], 
	["Le Bon Paris à l'étouffée conservation sans nitrite", '', 'c', '7613035989535', 'https://fr.openfoodfacts.org/produit/7613035989535/le-bon-paris-a-l-etouffee-conservation-sans-nitrite-herta', 'Magasins U,Leclerc', 2, 2.5, 1, 0.5, 1.9], 
	['Prince goût chocolat au blé complet', 'BISCUITS FOURRÉS (35%) PARFUM CHOCOLAT', 'd', '7622210449283', 'https://fr.openfoodfacts.org/produit/7622210449283/prince-gout-chocolat-au-ble-complet-lu', 'Carrefour Market,Magasins U,Auchan,Intermarché,Carrefour,Casino,Leclerc,Cora,Bi1', 3, 17, 5.6, 32, 0.58], 
	['Camembert', 'Camembert au lait de vache pasteurisé', 'd', '3228021170039', 'https://fr.openfoodfacts.org/produit/3228021170039/camembert-president', 'Magasins U,Carrefour', 4, 21, 15, 0, 1.4], 
	['Napolitain', 'Gâteau fourrage au chocolat - Napolitain Classic', 'e', '3017760290692', 'https://fr.openfoodfacts.org/produit/3017760290692/napolitain-lu', 'Carrefour,Magasins U,Cora Intermarche SuperU', 5, 20, 9, 34, 0.24]
	]


	def insert_products(self, entire_list):
		"""This method populates table Product"""
		
		cursor = self.connection.cursor()	
		try:
			for line in entire_list:				
				add_product = ("INSERT IGNORE INTO Product "
							"(name, description, nutrition_grade, barcode, "
							"url, store, prd_cat, fat, "
							"saturated_fat, sugar, salt)"
							" VALUES (%(name)s, %(description)s, %(nutrition_grade)s, %(barcode)s, "
							"%(url)s, %(store)s, %(prd_cat)s, %(fat)s, "
							"%(saturated_fat)s, %(sugar)s, %(salt)s)")
				add_product_value = {
							'id': cursor.lastrowid,
							'name': line[0],
							'description': line[1],
							'nutrition_grade': line[2],
							'barcode': line[3],
							'url': line[4],
							'store': line[5],
							'prd_cat': line[6],
							'fat': line[7],
							'saturated_fat': line[8],
							'sugar': line[9],
							'salt': line[10],
							}
				cursor.execute(add_product, add_product_value)
			
			insert_data_into_product_result = True
		except:
			insert_data_into_product_result = False		
		self.connection.commit()
		return insert_data_into_product_result


	def list_products(self, selected_category):
		"""This method selects all products that belong to the chosen category"""

		cursor = self.connection.cursor()
		sql_request = ("SELECT id, name, nutrition_grade FROM Product WHERE prd_cat=(%(prd_cat)s)")
		sql_value = {'prd_cat': selected_category,}
		cursor.execute(sql_request, sql_value)
		prd_list = cursor.fetchall()
		cursor.close()
		return prd_list


	def find_substitute(self, selected_category, selected_product):
		"""This method finds a better food than the selected one"""

		cursor = self.connection.cursor(buffered=True)		
		sql_request = ("SELECT name,description,barcode,nutrition_grade,store,url FROM Product"
						" WHERE prd_cat=(%(prd_cat)s) AND "
						"nutrition_grade < (SELECT nutrition_grade FROM Product WHERE id=(%(id)s))")
		sql_value = {'id': selected_product,
					'prd_cat': selected_category,}
		cursor.execute(sql_request,sql_value)
		result = cursor.fetchone()
		cursor.close()
		return result


	def retrieve_old_prd(self):
		"""This method retrieves old product linked to the substitute food"""

		cursor = self.connection.cursor()
		cursor.execute("USE {}".format(self.database))
		sql_request = ("SELECT Product.name "
						"FROM Product INNER JOIN Favourite "
						"ON Product.id=Favourite.Category_Product_product_id ORDER BY id ASC")
		cursor.execute(sql_request)
		old_prd_result = cursor.fetchall()
		cursor.close()
		return old_prd_result


	---------------------------------------------------------------------------------------
	def insert_vendor_list(vendor_list):
	    """ insert multiple vendors into the vendors table  """
	    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
	    conn = None
	    try:
	        # read database configuration
	        params = config()
	        # connect to the PostgreSQL database
	        conn = psycopg2.connect(**params)
	        # create a new cursor
	        cur = conn.cursor()
	        # execute the INSERT statement
	        cur.executemany(sql,vendor_list)
	        # commit the changes to the database
	        conn.commit()
	        # close communication with the database
	        cur.close()
	    except (Exception, psycopg2.DatabaseError) as error:
	        print(error)
	    finally:
	        if conn is not None:
	            conn.close()


	# insert multiple vendors
	    insert_vendor_list([
	        ('AKM Semiconductor Inc.',),
	        ('Asahi Glass Co Ltd.',),
	        ('Daikin Industries Ltd.',),
	        ('Dynacast International Inc.',),
	        ('Foster Electric Co. Ltd.',),
	        ('Murata Manufacturing Co. Ltd.',)
	    ])
	'''





















