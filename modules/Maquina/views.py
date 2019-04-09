from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .forms import FormMaquinaInsert, FormMaquinaUpdate
from .models import Maquina, TipoZona


def nuevo(request):
    if request.method == "POST":
        form = FormMaquinaInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomMaq = datos.get("nombre")
            fecha = datos.get("fechaingreso")
            tipo = datos.get("Tipo")

            if not Maquina.objects.filter(nombre=nomMaq): #todavia se puede guardar una maquina mas
                instTipoZona = TipoZona.objects.get(id=tipo)
                m = Maquina(nombre=nomMaq,fechaingreso=fecha,tipozona=instTipoZona);
                m.save()

                return HttpResponseRedirect("/maquina/lista")

            else:
                messages.error(request, 'La maquina ya existe.')
                messages.error(request, '')
    else:
        form = FormMaquinaInsert()

    return render(request, 'mnuevo.html', {'form': form})


def listar(request):
    datos = Maquina.objects.all()
    lista = []
    #print(lista.count()==0)

    for maquina in datos:


        tipoZona = TipoZona.objects.get(id=maquina.tipozona.id)
        data = {
            "id": maquina.id,
            "nom": maquina.nombre,
            "date": maquina.fechaingreso,
            "tipo": tipoZona.nombre.title(),
        }
        lista.append(data)

    return render(request, 'mlista.html', {"lista": lista})


def eliminar(request,pk ):
    try:
        maq = Maquina.objects.get(id=pk)
        maq.delete()
    except Maquina.DoesNotExist:
        raise Http404("Maquina no existe")

    return HttpResponseRedirect("/maquina/lista")


def modificar(request,pk ):
    try:
        maquina = Maquina.objects.get(id=pk)

        if request.method == "POST":
            form = FormMaquinaUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                # recogemos los datos
                nom = datos.get("nombre")
                fecha= datos.get("fechaingreso")
                tipo = datos.get("Tipo")
                instTipoZona = TipoZona.objects.get(id=tipo)

                # actualizamos datos
                maquina.nombre = nom
                maquina.fechaingreso=fecha
                maquina.tipozona = instTipoZona
                maquina.save()

                return HttpResponseRedirect("/maquina/lista")

        elif request.method == "GET":

            data = {

                "nom": maquina.nombre,
                "fecha": maquina.fechaingreso,
                "tipo":  maquina.tipozona.id,
                "nomTipoEle": maquina.tipozona.nombre,
            }

            datosTipo= listaTipos(data["nomTipoEle"])

            return render(request, 'mmodificar.html', {"datos": data, "datosTipo": datosTipo})

    except Maquina.DoesNotExist:
        raise Http404("Maquina no existe")

    return HttpResponseRedirect('/maquina/' + str(pk) + '/modificar')


def listaTipos(nombre):
   tipos = TipoZona.objects.all();
   lista = []

   for tipo in tipos:
      if nombre != tipo.nombre:
         data = {
            "id": tipo.id,
            "nom": tipo.nombre,
         }
         lista.append(data)

   return lista