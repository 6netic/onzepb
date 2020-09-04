from django.urls import path
from . import views

# Contains paths for food app
app_name = 'food'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('date', views.date_actuelle),
    path('detail/<int:product_id>', views.detail, name='detail'),
    path('listing', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('saveprd/<str:former_barcode>/<str:new_barcode>', views.saveprd, name='saveprd'),
    path('showfavourites', views.showfavourites, name='showfavourites')
]
