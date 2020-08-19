from os import path
import psycopg2

class Database:
	"""This class deals with all database operations"""

	def __init__(self, connection):
		"""Initializing the class with connection details"""
		
		self.connection = connection


	def create_tables(self):
		""" Creates tables in the PostgreSQL database """

		sql_commands = (
			"""
			CREATE TABLE IF NOT EXISTS Category (
				id SERIAL PRIMARY KEY NOT NULL,
				name VARCHAR(20) NOT NULL
			)
			""",
			"""
			CREATE TABLE IF NOT EXISTS Product (
				id SERIAL PRIMARY KEY NOT NULL,
				name VARCHAR(255),
				description VARCHAR(255),
				nutrition_grade CHAR(1),
				barcode VARCHAR(255) NOT NULL,
				url VARCHAR(255),
				url_pic VARCHAR(255),
				store VARCHAR(255),
				prd_cat SMALLINT NOT NULL,
				fat DECIMAL(5,2),
				saturated_fat DECIMAL(5,2),
				sugar DECIMAL(5,2),
				salt DECIMAL(5,2),
				CONSTRAINT fk_Prod_Cat
					FOREIGN KEY(prd_cat)
						REFERENCES Category(id)
			)
			"""
			
			
		)
		try:
			cursor = self.connection.cursor()
			# create table one by one
			for sql_line in sql_commands:
				cursor.execute(sql_line)
			cursor.close()
			# commit the changes
			self.connection.commit()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
		'''
		finally:
			if self.connection is not None:
				self.connection.close()
		'''

