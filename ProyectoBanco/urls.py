from django.urls import path
from . import views

urlpatterns = [
    
    path('inicio/', views.inicio, name='inicio'),
    path('acerca-de/', views.acerca_de, name='acerca_de'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
    path('salir/', views.salir, name='salir'),
    
    path('ElSol/', views.ElSol, name='ElSol'),
    path('formularios/', views.formulario, name='formularios'),
    path('pagina/', views.pagina, name='pagina'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('parcial/', views.parcial, name='parcial'),
]