from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, "bitacora/index.html")


def pais_list(request):
    paises = models.Pais.objects.all()
    context = {"paises": paises}
    return render(request, "bitacora/pais_list.html", context)


def viaje_list(request):
    viajes = models.Viaje.objects.all()
    context = {"viajes": viajes}
    return render(request, "bitacora/viaje_list.html", context)


def viaje_create(request):
    if request.method == "POST":
        form = forms.ViajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bitacora:viaje_list")
    else:
        form = forms.ViajeForm()
    return render(request, "bitacora/viaje_create.html", {"form": form})


def perfil_list(request):
    #perfiles = models.Perfil.objects.all()
    perfiles = models.Perfil.objects.filter(user_id=request.user.id)
    context = {"perfiles": perfiles}
    return render(request, "bitacora/perfil_list.html", context)


def perfil_create(request):
    if request.method == "POST":
        form = forms.PerfilForm(request.POST)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.user_id = request.user.id
            #perfil.moto = "Moto Hardcodeada"
            #form.save()
            perfil.save()
            return redirect("bitacora:perfil_list")
    else:
        form = forms.PerfilForm()
        form.moto = "Moto Hardcodeada 2"
    return render(request, "bitacora/perfil_create.html", {"form": form})

