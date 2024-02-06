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


def viaje_editar(request, id):
    viaje_update = models.Viaje.objects.get(id=id)
    perfil_viaje = models.Perfil.objects.get(id=viaje_update.perfil_id)

    if request.method == "POST":
        form = forms.ViajeForm(request.POST, instance=viaje_update)
        
        if form.is_valid():
            viaje = form.save(commit=False)
            viaje.save()
            return viaje_list(request, perfil_viaje.user_id)
    else:
        form = forms.ViajeForm(instance=viaje_update)
        return render(request, "bitacora/viaje_edit.html", {"form": form})

    return viaje_list(request, perfil_viaje.user_id)


def viaje_borrar(request, id):
    viaje_update = models.Viaje.objects.get(id=id)
    perfil_viaje = models.Perfil.objects.get(id=viaje_update.perfil_id)
    viaje_update.delete()
    return viaje_list(request, perfil_viaje.user_id)


def viaje_etapa_create(request, id):
    if request.method == "POST":
        form = forms.Viaje_EtapaForm(request.POST)
        if form.is_valid():
            viaje_etapa = form.save(commit=False)
            viaje_etapa.viaje_id = id
            form.save()
            #return redirect("bitacora:viaje_list")
            return viaje_etapa_list(request, viaje_etapa.viaje_id)
    else:
        form = forms.Viaje_EtapaForm()
    return render(request, "bitacora/viaje_etapa_create.html", {"form": form, "viaje_id": id})


def viaje_etapa_editar(request, id):
    viaje_etapa_update = models.Viaje_Etapa.objects.get(id=id)
    #perfil_viaje = models.Perfil.objects.get(id=viaje_update.perfil_id)

    if request.method == "POST":
        form = forms.Viaje_EtapaForm(request.POST, instance=viaje_etapa_update)
        
        if form.is_valid():
            viaje_etapa = form.save(commit=False)
            viaje_etapa.save()
            return viaje_etapa_list(request, viaje_etapa.viaje_id)
    else:
        form = forms.Viaje_EtapaForm(instance=viaje_etapa_update)
        return render(request, "bitacora/viaje_etapa_edit.html", {"form": form, "viaje_id": viaje_etapa_update.viaje_id})

    return viaje_etapa_list(request, viaje_etapa_update.viaje_id)


def viaje_etapa_list(request, id):
    viaje_etapas = ""
    #viaje_etapas = models.Viaje_Etapa.objects.get(viaje_id=id)
    if models.Viaje_Etapa.objects.filter(viaje_id=id).exists():
        viaje_etapas = models.Viaje_Etapa.objects.filter(viaje_id=id)
    context = {"viaje_etapas": viaje_etapas, "viaje_id":id}
    return render(request, "bitacora/viaje_etapa_list.html", context)


def viaje_etapa_borrar(request, id):
    viaje_etapa_update = models.Viaje_Etapa.objects.get(id=id)
    viaje = models.Viaje.objects.get(id=viaje_etapa_update.viaje_id)
    viaje_etapa_update.delete()
    return viaje_etapa_list(request, viaje.id)

def perfil_viaje_list(request, id):
    perfil_viaje = False

    viajes = ""
    viaje_etapas = ""
    html = "Viajes del Perfil"
    if models.Perfil.objects.filter(id=id).exists():
        perfil_viaje = models.Perfil.objects.get(id=id)
        if models.Viaje.objects.filter(perfil_id=perfil_viaje.id).exists():
            html += "<div> Datos del Perfil: " + perfil_viaje.apellido + ", " +  perfil_viaje.nombre + " - " + perfil_viaje.moto +  "</div>"
            viajes = ""
            if models.Viaje.objects.filter(perfil_id=perfil_viaje.id).exists():
                viajes = models.Viaje.objects.filter(perfil_id=perfil_viaje.id)
                nro_viaje = 0
                for viaje in viajes:
                    nro_viaje += 1
                    #html += "<div style='margin-left:0px'>" + "_" + "</div>"
                    html += "<div style='margin-left:10px'> Viaje " + str(nro_viaje) + ": " + viaje.localidad_ini + "  -  " + viaje.localidad_fin + "</div>"
                    html += "<div style='margin-left:10px'> _______ " + "  " + viaje.fecha_ini.strftime("%Y/%m/%d") + "  -  " + viaje.fecha_fin.strftime("%Y/%m/%d") + "  -  " + str(viaje.km_recorridos) + " Km" + "</div>"
                    viaje_etapas = ""
                    if models.Viaje_Etapa.objects.filter(viaje_id=viaje.id).exists():
                        viaje_etapas = models.Viaje_Etapa.objects.filter(viaje_id=viaje.id)
                        nro_etapa = 0
                        for viaje_etapa in viaje_etapas:
                            nro_etapa += 1
                            html += "<div style='margin-left:75px'> Etapa "+ str(nro_etapa) + "  " + viaje_etapa.fecha_ini.strftime("%Y/%m/%d") + "  -  " + viaje_etapa.fecha_fin.strftime("%Y/%m/%d")+ ": " + viaje_etapa.localidad_ini + "  -  " + viaje_etapa.localidad_fin + "  -  " +str(viaje_etapa.km_recorridos) + " Km" + "</div>"
            
    context = {"viajes": html}
    return render(request, "bitacora/perfil_viaje_list.html", context)
