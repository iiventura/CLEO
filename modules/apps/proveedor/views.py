from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Proveedor
from .forms import FormProveedorInsert, FormProveedorUpdate
from django.contrib.auth.decorators import login_required

@login_required()
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

                s = Proveedor(nombre=nomPro, contacto=con, descripcion=des,borrado=0)
                s.save()

                return HttpResponseRedirect("/proveedor/lista")
            else:
                messages.error(request, 'El proveedor ya existe.')
                messages.error(request, '')
    else:
        form = FormProveedorInsert()

    return render(request, 'prvnuevo.html', {'form': form, 'elem': 'Añadir', 'titulo':'Añadir Proveedor'})

@login_required()
def listar(request):
   datos = Proveedor.objects.all()
   lista = []

   for proveedor in datos:
      if proveedor.borrado != 1:
          data = {
             "id": proveedor.id,
             "nombre": proveedor.nombre,
             "contacto": proveedor.contacto,

          }
          lista.append(data)
   return render(request, 'prvlista.html', {"lista": lista})

@login_required()
def eliminar(request, pk):
   try:
      prov = Proveedor.objects.get(id=pk)
      #prov.delete()
      prov.borrado = 1
      prov.save()
   except Proveedor.DoesNotExist:
      raise Http404("Proveedor no existe")

   return HttpResponseRedirect("/proveedor/lista")

@login_required()
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

@login_required()
def modificar(request, pk):
   try:
      proveedor = Proveedor.objects.get(id=pk)

      if request.method == "POST":
         form = FormProveedorUpdate(request.POST)

         if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            nomProv = datos.get("nombre")
            desc = datos.get("descripcion")
            contacto = datos.get("contacto")


            # actualizamos datos
            proveedor.nombre = nomProv
            proveedor.descripcion = desc
            proveedor.contacto = contacto
            proveedor.save()

            return HttpResponseRedirect("/proveedor/lista")

      elif request.method == "GET":

         data = {
            "id": proveedor.id,
            "nom": proveedor.nombre,
            "des": proveedor.descripcion,
            "cont": proveedor.contacto,

         }
         return render(request, 'prvmodificar.html', {"datos": data,"elem":"Modificar", "titulo":"Modificar Proveedor" })

   except Proveedor.DoesNotExist:
      raise Http404("Proveedor no existe")

   return HttpResponseRedirect('/proveedor/' + str(pk) + '/modificar')