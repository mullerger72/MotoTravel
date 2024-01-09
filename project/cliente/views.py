from django.shortcuts import render

from . import models


def index(request):
    return render(request, "cliente/index.html")


def pais_list(request):
    paises = models.Pais.objects.all()
    context = {"paises": paises}
    return render(request, "cliente/pais_list.html", context)


def cliente_list(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/cliente_list.html", context)
