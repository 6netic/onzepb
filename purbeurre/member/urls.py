from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('register', views.register, name='register'),
    path('connect', views.connect, name='connect'),
    path('disconnect', views.disconnect, name='disconnect'),

]
