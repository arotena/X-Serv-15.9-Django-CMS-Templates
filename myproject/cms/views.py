from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template import Context
from django.template.loader import get_template
# Create your views here.

def mostrar (request, key):
    try:
        valor = Pages.objects.get(id=key)
        respuesta = "Name: " + valor.name +"</br>"
        respuesta += "Page: " + valor.page +"</br>"
    except Pages.DoesNotExist:
        respuesta = "Esta clave no existe"
    template = get_template("servir.html")
    argumentos = {'contenido': respuesta}
    return HttpResponse(template.render(Context(argumentos)))
    return HttpResponse(respuesta)

@csrf_exempt
def listar(request):
    if request.method == "POST":
        name = request.POST.get('name')
        page = request.POST['page']
        elemento = Pages(name=name,page=page)
        elemento.save()
    listado = Pages.objects.all()
    respuesta = "<ol>"
    for elemento in listado:
        respuesta += '<li><a href ="'"annotated/"+ str(elemento.id) + '">'
        respuesta += str(elemento.name) + '</a>'
    respuesta += "</ol>"

    if request.user.is_authenticated():
        loggeado = "<p>Logged in as " + request.user.username
        loggeado += '<br><a href="/logout">Logout</a>'
        template = get_template("plantilla.html")
        argumentos = {'contenido': respuesta, 'loggeado': loggeado}
        return HttpResponse(template.render(Context(argumentos)))
    else:
        loggeado = "<p>Not logged in</p> "
        loggeado += '<a href="/login">Loggeate</a>'
        respuesta += loggeado
        return HttpResponse("Elements:" + respuesta)

def login(request):
    respuesta = "Welcome " + request.user.username
    respuesta += '<br><a href="/">Inicio</a>'
    return HttpResponse(respuesta)
def notFound(request):
    return HttpResponse("Not Found: Argumentos invalidos")
