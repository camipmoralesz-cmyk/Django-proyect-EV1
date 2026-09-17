from django.urls import path
from . import views

app_name = 'mascota'
urlpatterns = [path('', views.mascota, name='mascota')]