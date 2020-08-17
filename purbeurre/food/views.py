from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
#from .models import Product, Category, CategoryProduct, Favourite
from .models import *

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


def example1(request):
    return render(request, 'food/listing.html')


def listing(request):
    #return render(request, 'food/listing.html')
    #albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    #message = """<ul>{}</ul>""".format("\n".join(albums))
    #return HttpResponse(message)
    
    #categories = Category.objects.all()
    #formatted_categories = ["<li>{}</li>".format(cat.name) for cat in categories]
    #message = """<ul>{}</ul>""".format("\n".join(formatted_categories))
    
    products = Product.objects.all()[:6]
    #formatted_products = ["<h5>{}</h5>".format(prod.name) for prod in products]
    #return HttpResponse(formatted_products)
    context = {'products': products}
    return render(request, 'food/listing.html', context)



def detail(request, product_id):
    #id = int(product_id) # make sure we have an integer.
    
    product = Product.objects.get(pk=product_id)
    context = {
        'product_name': product.name,
        'product_description': product.description,
        'product_nutrition_grade': product.nutrition_grade,
        'product_url': product.url,
        'product_url_pic': product.url_pic,
        'product_store': product.store,
        'product_fat': product.fat,
        'product_saturated_fat': product.saturated_fat,
        'product_sugar': product.sugar,
        'product_salt': product.salt,
    }
    return render(request, 'food/detail.html', context)
    


def search(request):

    word = request.GET.get("search_word")
    # Trouver une fonction qui renvoie 6 produits appartenant à la même catégorie 
    # mais avec un indice inférieur ou égal au produit recherché
    #product = Product.objects.filter(name__icontains=word)[:1]
    product = Product.objects.get(name__exact=word)

    context = {
        'word': word,
        'product': product,

        
    }
    





    return render(request, 'food/result.html', context)








































