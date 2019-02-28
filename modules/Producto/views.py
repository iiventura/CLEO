from django.contrib import messages
from django.shortcuts import render

from modules.Producto.models import Producto, Tipoproducto
from .forms import FormProductoInsert


def nuevo(request):
    if request.method == "POST":
        form = FormProductoInsert(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            # recogemos los datos
            id = datos.get("id")
            nombre = datos.get("nombre")
            tipo = datos.get("Tipo")

            if not Producto.objects.filter(id=id):  # todavia se puede guardar una maquina mas
                instTipoProducto = Tipoproducto.objects.get(id=tipo)
                p = Producto(id=id, nombre=nombre, tipoproducto=instTipoProducto);
                p.save()

                return render(request, 'pnuevo.html', {'form': form})
            else:
                messages.error(request, 'El producto ya existe.')
                messages.error(request, '')
    else:
        form = FormProductoInsert()

    return render(request, 'pnuevo.html', {'form': form})