from django.urls import path
from . import views

app_name = 'general'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    #pag principal y registro
    path('redirect_pag_principal/', views.redirect_pag_principal, name='redirect_pag_principal'),
    path('pag_principal/<int:id>', views.pag_principal, name='pag_principal'),
    path('registrandome/', views.registrandome, name='registrandome'),
    path('registro/', views.registro, name='registro'),
    #mascotas veterianario
    path('pag_principal/new_mascota/<int:id>', views.creando_mascota, name='creando_mascota'),
    path('pag_principal/anadiendo_mascota/<int:id>', views.anadiendo_mascota, name='anadiendo_mascota'),
    path('pag_principal/ver_mascotas/<int:id>', views.ver_mascotas, name='ver_mascotas'),
    path('pag_principal/ver_mascotas/info_mascota/<int:id>', views.info_mascota, name='info_mascota'),
    path('pag_principal/ver_mascotas_usuario', views.ver_mascotas_usuario, name='ver_mascotas_usuario'),
    #citas veterianario
    path('pag_principal/agregar_cita/<int:id>', views.agregar_cita, name='agregar_cita'),
    path('pag_principal/guardar_cita/<int:id>', views.guardar_cita, name='guardar_cita'),
]