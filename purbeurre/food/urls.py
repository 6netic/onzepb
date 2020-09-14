from django.urls import path
from . import views

# Contains paths for food app
app_name = 'food'

urlpatterns = [
    path('date', views.date, name='dates'),
    path('', views.homepage, name='homepage'),
    path('legal', views.legal, name='legal'),
    
    path('detail/<int:product_id>', views.detail, name='detail'),
    path('search', views.search, name='search'),
    path('saveprd/', views.saveprd, name='saveprd'),
    #path('saveprd/<str:former_barcode>/<str:new_barcode>', views.saveprd, name='saveprd'),
    path('showfavourites', views.showfavourites, name='showfavourites'),
    path('listing', views.listing, name='listing'),
]
