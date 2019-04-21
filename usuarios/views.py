from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from usuarios.empleado.forms import EmpleadoRegistrationForm
from usuarios.cliente.forms import ClienteRegistrationForm
from .models import Empleado



def home(request):
        return render(request, 'main.html')

def about(request):
    pass

def register(request):
    if request.method == 'POST':
        form = ClienteRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Se ha registrado correctamente')
            return redirect('login')

    else:
        form = ClienteRegistrationForm()
    return render(request,'cliente/register.html',{'form':form})


@login_required()
def register_empleado(request):
    if request.method == 'POST':
        form = EmpleadoRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            tipo = form.cleaned_data.get('tipo')
            messages.success(request,'Se ha registrado correctamente')
            return redirect('login')
    else:
        form = EmpleadoRegistrationForm()
    return render(request, 'empleado/register.html', {'color':2,'form': form})


@login_required
def perfil (request):

    if request.user.is_staff and (not request.user.is_superuser):
            empleado=Empleado.objects.get(user_id=request.user.id)
            return render(request, 'empleado/perfil.html',{'tipo_e':empleado.tipoempleado.nombre})

    elif request.user.is_staff and  request.user.is_superuser:
        return HttpResponseRedirect('/admin')

    elif request.user.is_client:
            return render(request, 'cliente/perfil.html')









