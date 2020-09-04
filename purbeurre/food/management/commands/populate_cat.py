
from django.core.management.base import BaseCommand
from food.models import *



class Command(BaseCommand):
	""" This class does something I don't know yet """

	#args = "Boissons", "Viandes", "Biscuits", "Fromages", "Desserts"
	#options = ["Boissons", "Viandes", "Biscuits", "Fromages", "Desserts"]
	help = 'Truc de fou'
	

	def handle(self, *args, **options):
		""" This method does something """

		categories = ["Boissons", "Viandes", "Biscuits", "Fromages", "Desserts"]
		#categories_length = len(categories)
		#print(categories_length)
		for cat in categories:
			#print(cat)
			Category.objects.create(name=cat)
		print("Nombre de lignes insérées : ", lines) #3 lignes