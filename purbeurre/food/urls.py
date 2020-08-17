from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('accueil', views.home),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('example1', views.example1),
    path('detail/<int:product_id>', views.detail, name='detail'),
    path('listing', views.listing, name='listing'),
    path('search', views.search, name='search')
]
