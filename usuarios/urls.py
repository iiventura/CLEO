from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views as users_views
from .empleado import views
from .cliente import views


urlpatterns = [
    path('', users_views.home, name='base-home'),
    path('nosotros/', users_views.about, name='base-about'),
    path('registrar/', users_views.register, name='-base-registro'),
    path('registrar/empleado', users_views.register_empleado, name='registro-empleado'),
    path('login/',auth_views.LoginView.as_view(redirect_authenticated_user=True,
                                               template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('perfil/', users_views.perfil,name='perfil'),

    path('cliente/', include('usuarios.cliente.urls')),
    path('empleado/', include('usuarios.empleado.urls')),

]

"""
   Asignar un usuario a un grupo de permisos 
   from django.contrib.auth.models import Group
   my_group = Group.objects.get(name='my_group_name') 
   my_group.user_set.add(your_user)




   """