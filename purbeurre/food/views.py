from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from .models import *
from django.contrib.auth.decorators import login_required
import logging

def homepage(request):
    """ Homepage of the application """

    return render(request, 'food/index.html')


def legal(request):
    """ Redirects to legal mentions page """
    
    return render(request, 'food/legal.html')


def search(request):
    """ This method finds a products the user is looking for """

    word = request.GET.get("search_word")
    # Retrieving the first product found
    try:
        search_prd = Product.objects.filter(name__icontains=word).first()
        search_prd_id = search_prd.id
        search_prd_nut = search_prd.nutrition_grade
        search_prd_cat = search_prd.prd_cat
        
        # Gives back the first 6 products found
        best_prds = Product.objects.filter(prd_cat__exact=search_prd_cat).\
                            filter(nutrition_grade__lte=search_prd_nut).\
                            exclude(pk=search_prd_id)[:6]
        
    except AttributeError:
        raise Http404("Il n'y a pas de réponse à votre recherche. Désolé.")

    return render(request, 'food/result.html', locals())


def detail(request, product_id):
    """ This method shows the detail of a specific product """
    
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


def saveprd(request):
    """ This method saves a product into the database """

    former_barcode = request.GET.get("former_barcode")
    new_barcode = request.GET.get("new_barcode")
    email = request.user.email

    try:
        new_entry = Favourite.objects.create(
                                            former_barcode=former_barcode, 
                                            favourite_barcode=new_barcode, 
                                            email_user = email,
                                        )
        return HttpResponse("<p align='center' style='color: green;'>Ce produit a bien été enregistré dans vos favoris</p>")
    except:
        return HttpResponse("<p align='center' style='color: red;'>Ce produit a déjà été enregistré en base de données.</p>")


@login_required
def showfavourites(request):
    """ This method shows all the registered products from a specific user """

    email = request.user.email
    favourites = Favourite.objects.all().filter(email_user=email)
    favourite_list = []
    for i in range(len(favourites)):
        new_code = favourites[i].favourite_barcode
        product = Product.objects.get(barcode=new_code)
        favourite_list.append(product)
        
    return render(request, 'food/favourite.html', locals())


