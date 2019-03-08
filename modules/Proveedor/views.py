from django.contrib import messages
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

                return render(request, 'prnuevo.html', {'form': form})
            else:
                messages.error(request, 'El proveedor ya existe.')
                messages.error(request, '')
    else:
        form = FormProveedorInsert()

    return render(request, 'prnuevo.html', {'form': form})


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
   return render(request, 'prlista.html', {"lista": lista})
