from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .forms import *
from .models import *
from django.contrib import messages
from django.utils.dateparse import parse_date
import datetime


def nueva(request):
    if request.method == "POST":
        form = FormPublicidadInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            inicio = datos.get("fechainicio")
            fin = datos.get("fechafin")
            promocion = datos.get("promocion")
            cliente = datos.get("cliente")

            instPromocion = Promocion.objects.get(id=promocion)
            instCliente = Cliente.objects.get(dni=cliente)

            try:
                fIni = formatoDate(inicio)
                fFin = formatoDate(fin)

                if fIni > fFin:
                    messages.error(request, "Las fechas no son correctas.")
                else:
                    p = Publicidad(fechainicio=fIni, fechafin=fFin, promocion=instPromocion, cliente=instCliente);
                    p.save()

                    return HttpResponseRedirect("/publicidad/lista")
            except:
                messages.error(request, "El formato de las fechas no es correcto (dd-mm-yyyy) ")

    else:
        form = FormPublicidadInsert()

    return render(request, 'nuevoGeneral.html', {'form': form, 'elem': 'Añadir','titulo':'Añadir Publicidad'})

def listar(request):
   datos = Publicidad.objects.all()
   lista = []

   for publicidad in datos:

      data = {
         "id": publicidad.id,
         "ini": formatoDateString(str(publicidad.fechainicio)),
         "fin": formatoDateString(str(publicidad.fechafin)),
         "prom": publicidad.promocion.codigo,
         "cli": publicidad.cliente.nombre,
      }

      lista.append(data)

   return render(request, './pulista.html', {"lista": lista})

def eliminar(request, pk):
   try:
      promo = Publicidad.objects.get(id=pk)
      promo.delete()
   except Publicidad.DoesNotExist:
      raise Http404("Publicidad no existe")

   return HttpResponseRedirect("/publicidad/lista")

def detalle(request, pk):
   try:
       publicidad = Publicidad.objects.get(id=pk)

       data = {
           "id": publicidad.id,
           "ini": formatoDateString(str(publicidad.fechainicio)),
           "fin": formatoDateString(str(publicidad.fechafin)),
           "prom": publicidad.promocion.codigo,
           "cli": publicidad.cliente.nombre,
       }

   except Promocion.DoesNotExist:
      raise Http404("Publicidad no existe")

   return render(request, 'pudetalle.html', {"datos": data})

def modificar(request,pk):

    try:
        publicidad = Publicidad.objects.get(id=pk)

        if request.method == "POST":
            form = FormPublicidadUpdate(request.POST)

            if form.is_valid():
                datos = form.cleaned_data

                # recogemos los datos
                inicio = datos.get("fechainicio")
                fin = datos.get("fechafin")
                promocion = datos.get("promocion")
                cliente = datos.get("cliente")

                try:

                    fIni = formatoDate(inicio)
                    fFin = formatoDate(fin)

                    if fIni > fFin:
                        messages.error(request, "Las fechas no son correctas.")
                    else:

                        antiPub = Publicidad.objects.get(id=pk)
                        instPromocion = Promocion.objects.get(id=promocion)
                        instCliente = Cliente.objects.get(dni=cliente)

                        # actualizamos datos
                        antiPub.fechainicio = fIni
                        antiPub.fechafin = fFin
                        antiPub.promocion = instPromocion
                        antiPub.cliente = instCliente
                        antiPub.save()

                        return HttpResponseRedirect("/publicidad/lista")
                except:
                    messages.error(request, "El formato de las fechas no es correcto (dd-mm-yyyy)")

        elif request.method == "GET":

            data = {
                "id": publicidad.id,
                "ini": formatoDateString(str(publicidad.fechainicio)),
                "fin": formatoDateString(str(publicidad.fechafin)),
                "nomProEle": publicidad.promocion.nombre,
                "idProEle": publicidad.promocion.id,
                "nomCliEle": publicidad.cliente.nombre,
                "idCliEle": publicidad.cliente.dni,
            }

            datosPromocion = listaPromociones(data["nomProEle"])
            datosCliente = listaClientes(data["nomCliEle"])

            return render(request, 'pumodificar.html', {"datos": data,"datosPromocion": datosPromocion,
                'datosCliente': datosCliente})

    except Promocion.DoesNotExist:
        raise Http404("Publicidad no existe")

    return HttpResponseRedirect('/publicidad/' + str(pk) + '/modificar')

def listaPromociones(nombre):
   tipos = Promocion.objects.all();
   lista = []

   for tipo in tipos:
      if nombre != tipo.nombre:
         data = {
            "id": tipo.id,
            "nom": tipo.nombre,
         }
         lista.append(data)

   return lista

def listaClientes(nombre):
   tipos = Cliente.objects.all();
   lista = []

   for tipo in tipos:
      if nombre != tipo.nombre:
         data = {
            "dni": tipo.dni,
            "nom": tipo.nombre,
         }
         lista.append(data)

   return lista

def formatoDate(fecha):

    d = datetime.datetime.strptime(fecha, '%d-%m-%Y').day
    m = datetime.datetime.strptime(fecha, '%d-%m-%Y').month
    y = datetime.datetime.strptime(fecha, '%d-%m-%Y').year

    return datetime.datetime(y, m, d).date()

def formatoDateString(fecha):

    #en la bbdd se guarda yyyy-mm-dd cambiamso para que sea dd-mm-yyy
    cad = fecha.split('-')
    cad = cad[2] + '-' + cad[1] + '-' + cad[0]

    return cad
