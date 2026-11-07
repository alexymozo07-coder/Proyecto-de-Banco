from django.http import HttpResponse, request
from django.shortcuts import render

def inicio(request):
    return HttpResponse("Bienvenido a la página de inicio del Proyecto Banco.")

def acerca_de(request):
    return HttpResponse("Esta es la página 'Acerca de' del Proyecto Banco.")

def contacto(request):
    return HttpResponse("Esta es la página de contacto del Proyecto Banco.")

def servicios(request):
    return HttpResponse("Esta es la página de servicios del Proyecto Banco.")

def salir(request):
    return HttpResponse("Has salido de la sesión del Proyecto Banco.")

def ElSol(request):
    return render(request, "ProyectoBanco/El-Sol.html")

def formulario(request):
    return render(request, "ProyectoBanco/formularios .html")

def pagina(request):
    return render(request, "ProyectoBanco/pagina.html")

def pagina2(request):
    return render(request, "ProyectoBanco/pagina2.html")

def parcial(request):
    return render(request, "ProyectoBanco/parcial.html")



# Create your views here.
