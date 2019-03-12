from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Proveedor
from .forms import FormProveedorInsert


def nuevo(request):
    if request.method == "POST":
        form = FormProveedorInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomPro = datos.get("nombre")
            con = datos.get("contacto")
            des = datos.get("descripcion")


            if not Proveedor.objects.filter(nombre=nomPro): #todavia se puede guardar una maquina mas

                s = Proveedor(nombre=nomPro, contacto=con, descripcion=des)
                s.save()

                return HttpResponseRedirect("/proveedor/lista")
            else:
                messages.error(request, 'El proveedor ya existe.')
                messages.error(request, '')
    else:
        form = FormProveedorInsert()

    return render(request, 'nuevoGeneral.html', {'form': form, 'elem': 'Añadir', 'titulo':'Añadir Proveedor'})


def listar(request):
   datos = Proveedor.objects.all()
   lista = []
   data ={}
   for proveedor in datos:
      #instMaquina = Maquina.objects.get(id=tratamiento.maquina.id)
      data = {
         "id": proveedor.id,
         "nombre": proveedor.nombre,
         "contacto": proveedor.contacto,

      }
      lista.append(data)
   return render(request, 'prvlista.html', {"lista": lista})


def eliminar(request, pk):
   try:
      sala = Proveedor.objects.get(id=pk)
      sala.delete()
   except Proveedor.DoesNotExist:
      raise Http404("Proveedor no existe")

   return HttpResponseRedirect("/proveedor/lista")


def detalle(request, pk):
   try:
      proveedor = Proveedor.objects.get(id=pk)
      data = {
         "id": proveedor.id,
         "nombre": proveedor.nombre,
         "descripcion": proveedor.descripcion,
         "contacto": proveedor.contacto,
      }
   except Proveedor.DoesNotExist:
      raise Http404("Proveedor no existe")

   return render(request, 'prvdetalle.html', {"datos": data})
