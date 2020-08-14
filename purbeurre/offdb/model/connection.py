#!/usr/bin/python

import psycopg2


class Connection:
	"""This class holds credentials to connect to MySQL DBMS"""

	def __init__(self):
		self.username = "p8user"
		self.password = "p8Passw"
		self.hostname = "localhost"
		self.database = "purbeurre_db"
		self.port = 5432


	def connect_to_dbms(self):
		""" This method connects to DBMS. Insert Try method please """				

		connection = psycopg2.connect(
			user = self.username,
			password = self.password,
			host = self.hostname,
			dbname = self.database,
			port = self.port
			#sslmode = require
		)
		return connection


