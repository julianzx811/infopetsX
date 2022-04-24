from django.urls import path
from . import views
#usuarios.objects.filter(usuario__startswith='yulian')
app_name = 'general'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pag_principal/', views.pag_principal, name='pag_principal'),
    path('registrandome/', views.registrandome, name='registrandome'),
    path('registro/', views.registro, name='registro'),
    path('pag_principal/new_mascota/<str:mascota>', views.creando_mascota, name='creando_mascota'),
    path('pag_principal/ver_mascotas/', views.ver_mascotas, name='ver_mascotas'),
]