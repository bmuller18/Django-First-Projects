from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo")

def despedida(request):
    return HttpResponse("Adiós mundo")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("Eres menor de edad")