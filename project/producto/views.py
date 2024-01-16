from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, "producto/index.html")


# * list

# def productocategoria_list(request):
#     objects = ProductoCategoria.objects.all()
#     context = {"object_list": objects}
#     return render(request, "producto/productocategoria_list.html", context)


class ProductoCategoriaList(ListView):
    model = ProductoCategoria
    # context_object_name = "object_list"
    # template_name = "producto/productocategoria_list.html"

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consultar = self.request.GET.get("consulta")
            object_list = ProductoCategoria.objects.filter(nombre__icontains=consultar)
        else:
            object_list = ProductoCategoria.objects.all()
        return object_list


class ProductoCategoriaCreate(CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria
    # context_object_name = "object"
    # template_name = "producto/productocategoria_detail.html"


class ProductoCategoriaUpdate(UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoCategoriaDelete(DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
