from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
#from .models import Product, Category, CategoryProduct, Favourite
from .models import *
from django.contrib.auth.decorators import login_required


def homepage(request):
	""" Homepage of the application """
	return render(request, 'food/index.html')

@login_required
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
    searched_p = Product.objects.filter(name__icontains=word).first()
    searched_p_id = searched_p.id
    searched_p_nut_g = searched_p.nutrition_grade
    searched_p_cat = searched_p.prd_cat
    #searched_p_cat = Product.objects.select_related('category').get('prd_cat')
    # Trouver une commande qui effectue une recherche en fonction du nutrition_grade et de la catégorie
    #best_p = Product.objects.filter(nutrition_grade__exact=searched_p_nut_g).filter(prd_cat__exact=searched_p_cat).exclude(name=searched_p)[:6]
    best_p = Product.objects.filter(prd_cat__exact=searched_p_cat).filter(nutrition_grade__lte=searched_p_nut_g).exclude(pk=searched_p_id)[:6] 
    #cat = Product.objects.filter(category__id=searched_p_cat)
    #cat = Product.objects.category.name

    context = {
        'word': word,
        'product': searched_p,
        'nutrition': searched_p_nut_g,
        'category': searched_p_cat,
        'others': best_p,
        #'cat': cat        
    }
    return render(request, 'food/result.html', context)








































