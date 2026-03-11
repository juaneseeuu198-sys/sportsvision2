from django.urls import path
from . import views

urlpatterns = [
    path('', views.herramientas, name='herramientas'),
    path('calorias/', views.calculadora_calorias, name='calculadora_calorias'),
    path('imc/', views.calculadora_imc, name='calculadora_imc'),
]
