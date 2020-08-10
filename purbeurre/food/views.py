from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)

def homepage(request):
	""" Homepage of the application """
	return render(request, 'food/index.html')


def date_actuelle(request):
    return render(request, 'food/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'food/addition.html', locals())