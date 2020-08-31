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


def search(request):
    """ This method finds a products the user is looking for """

    word = request.GET.get("search_word")
    # Retrieving the first product found
    search_prd = Product.objects.filter(name__icontains=word).first()
    search_prd_id = search_prd.id
    search_prd_nut = search_prd.nutrition_grade
    search_prd_cat = search_prd.prd_cat
    # Gives back the first 6 products found
    best_prds = Product.objects.filter(prd_cat__exact=search_prd_cat).\
                            filter(nutrition_grade__lte=search_prd_nut).\
                            exclude(pk=search_prd_id)[:6] 

    return render(request, 'food/result.html', locals())


def listing(request):
    """ This is an example that shows the 6 first results - to be deleted"""
    
    products = Product.objects.all()[:6]
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
    







































