import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, context 
from Familiares.models import familiares


def inicio(request):
    return HttpResponse("Bienvenido a la pagina inicial")



def familia(request):
    mama = familiares(nombre= "Laura", nacimiento= datetime.datetime(1969, 7, 9), parentesco="Mama")
    papa = familiares(nombre= "Marcelo", nacimiento= datetime.datetime(1961, 10, 18), parentesco="Papa")
    hermana_1 = familiares(nombre= "Valentina", nacimiento= datetime.datetime(1999, 5, 13), parentesco="Hermana")
    hermana_2 = familiares(nombre= "Bernardita", nacimiento= datetime.datetime(2002, 6, 22), parentesco="Hermana")
    novia = familiares(nombre= "Yanina", nacimiento= datetime.datetime(1990, 12, 3), parentesco="Novia")
    mama.save()
    papa.save()
    hermana_1.save()
    hermana_2.save()
    novia.save()
    diccionario_famila = {
        "Nombre Madre":mama.nombre,
        "Nacimiento Madre":mama.nacimiento,
        "Parentesco Madre":mama.parentesco,
        "Nombre Padre":papa.nombre,
        "Nacimiento Padre":papa.nacimiento,
        "Parentesco Padre":papa.parentesco,
        "Nombre Hermana":hermana_1.nombre,
        "Nacimiento Hermana":hermana_1.nacimiento,
        "Parentesco Hermana":hermana_1.parentesco,
        "Nombre Hermana2":hermana_2.nombre,
        "Nacimiento Hermana2":hermana_2.nacimiento,
        "Parentesco Hermana2":hermana_2.parentesco,
        "Nombre novia":novia.nombre,
        "Nacimiento novia":novia.nacimiento,
        "Parentesco novia":novia.parentesco,
    }
    dochtml = loader.get_template("Plantillas\inicio.html")
    renderizado = dochtml.render({diccionario_famila})
    return HttpResponse(renderizado)
    
    


