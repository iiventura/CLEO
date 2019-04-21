from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .models import Empleado, TipoEmpleado

@login_required()
def listar(request):
    pass

@login_required()
def eliminar(request):
    pass

@login_required()
def modificar(request):
    pass
