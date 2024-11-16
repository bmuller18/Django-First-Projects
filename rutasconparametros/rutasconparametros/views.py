from django.http import HttpResponse

def adulto(requests, edad):
    if(edad >= 18):
        return HttpResponse("Bienvenido adulto")
    else:
        return HttpResponse("Lo siento, no puedes entrar")
    