from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ClienteRegistrationForm, EmpleadoRegistrationForm
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
            username=form.cleaned_data.get('username')
            messages.success(request,'Se ha registrado correctamente, por favor entre')
            return redirect('base-home')
    else:
        form = ClienteRegistrationForm()
    return render(request,'cliente/register.html',{'color':3,'form':form})

def register_empleado(request):
    if request.method == 'POST':
        form = EmpleadoRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Se ha registrado correctamente, por favor entre')
            return redirect('login')
    else:
        form = EmpleadoRegistrationForm()
    return render(request, 'empleado/register.html', {'color':2,'form': form})

@login_required
def perfil (request):

    if request.user.is_staff:
        empleado=Empleado.objects.get(user_id=request.user.id)
        return render(request, 'empleado/perfil.html',{'tipo_e':empleado.tipoempleado.nombre})

    elif request.user.is_client:
            return render(request, 'cliente/perfil.html')








