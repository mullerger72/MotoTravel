from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, "bitacora/index.html")


def pais_list(request):
    paises = models.Pais.objects.all()
    context = {"paises": paises}
    return render(request, "bitacora/pais_list.html", context)


def viaje_list(request, id):
    #viajes = models.Viaje.objects.all()
    perfil_viaje = False
    viajes = ""
    if models.Perfil.objects.filter(user_id=id).exists():
        perfil_viaje = models.Perfil.objects.get(user_id=id)
        #perfil_viaje = models.Perfil.objects.filter(user_id=request.user.id)
        viajes = models.Viaje.objects.filter(perfil_id=perfil_viaje.id)
        #viajes = models.Viaje.objects.filter(perfil_id=16)
    context = {"viajes": viajes}
    return render(request, "bitacora/viaje_list.html", context)


def viaje_create(request, id):
    perfil_viaje = False
    if models.Perfil.objects.filter(user_id=id).exists() :
        perfil_viaje = models.Perfil.objects.get(user_id=id)

    if request.method == "POST":
        form = forms.ViajeForm(request.POST)
        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.perfil_id = perfil_viaje.id
            form.save()
            #return redirect("bitacora:viaje_list")
            return render(request,"bitacora/index.html")
    else:
        form = forms.ViajeForm()
    return render(request, "bitacora/viaje_create.html", {"form": form})


def perfil_list(request):
    perfiles = models.Perfil.objects.all()
    #perfiles = models.Perfil.objects.filter(user_id=request.user.id)
    context = {"perfiles": perfiles}
    return render(request, "bitacora/perfil_list.html", context)


def perfil_create(request, id):
    perfil_update = False
    if models.Perfil.objects.filter(user_id=id).exists() :
        perfil_update = models.Perfil.objects.get(user_id=id)

    if request.method == "POST":
        if perfil_update :
            form = forms.PerfilForm(request.POST, instance=perfil_update)
        else:
            form = forms.PerfilForm(request.POST)
        
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.user_id = request.user.id
            #perfil.moto = perfil_update.apellido
            #form.save()
            perfil.save()
            #return redirect("bitacora:perfil_list")
            return render(request,"bitacora/index.html")
            #return render(request,"bitacora/perfil_create.html", {"form": form})
    else:
        if perfil_update :
            form = forms.PerfilForm(instance=perfil_update)
        else:
            form = forms.PerfilForm()

        #form = forms.PerfilForm(instance=perfil_update)
    return render(request, "bitacora/perfil_create.html", {"form": form})

def perfil_borrar(request, id):
#    viaje = models.Viaje.objects.get(id=1)
#    viaje.delete()
    perfil = models.Perfil.objects.get(id=id)
    perfil.delete()
    return redirect("bitacora:perfil_list")
