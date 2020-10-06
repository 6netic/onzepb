from django.urls import path
from . import views

# Contains paths for food app
app_name = 'food'

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('legal', views.legal, name='legal'),    
	path('detail/<int:product_id>', views.detail, name='detail'),
	path('search', views.search, name='search'),
	path('saveprd/', views.saveprd, name='saveprd'),
	path('showfavourites', views.showfavourites, name='showfavourites'),
]
