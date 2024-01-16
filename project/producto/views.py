from django.shortcuts import redirect, render
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
            consulta = self.request.GET.get("consulta")
            object_list = ProductoCategoria.objects.filter(nombre__icontains=consulta)
        else:
            object_list = ProductoCategoria.objects.all()
        return object_list


class ProductoCategoriaCreate(CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


# def productocategoria_detail(request, pk: int):
#     consulta = ProductoCategoria.objects.get(id=pk)
#     return render(request, "producto/productocategoria_detail.html", {"object": consulta})


class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria


# def productocategoria_update(request, pk: int):
#     consulta = ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         form = ProductoCategoriaForm(request.POST, instance=consulta)
#         if form.is_valid():
#             form.save()
#             return redirect("producto:productocategoria_list")
#     else:
#         form = ProductoCategoriaForm(instance=consulta)
#     return render(request, "producto/productocategoria_form.html", {"form": form})


class ProductoCategoriaUpdate(UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:productocategoria_list")


# def productocategoria_delete(request, pk: int):
#     consulta = ProductoCategoria.objects.get(id=pk)
#     if request.method == "POST":
#         consulta.delete()
#         return redirect("producto:productocategoria_list")
#     return render(request, "producto/productocategoria_confirm_delete.html", {"object": consulta})


class ProductoCategoriaDelete(DeleteView):
    model = ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
