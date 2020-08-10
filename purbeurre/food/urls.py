from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('accueil', views.home),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]

