from django.urls import path
from . import views
#usuarios.objects.filter(usuario__startswith='yulian')
app_name = 'general'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('redirect_pag_principal/', views.redirect_pag_principal, name='redirect_pag_principal'),
    path('pag_principal/<int:id>', views.pag_principal, name='pag_principal'),
    path('registrandome/', views.registrandome, name='registrandome'),
    path('registro/', views.registro, name='registro'),
    path('pag_principal/new_mascota/<int:id>', views.creando_mascota, name='creando_mascota'),
    path('pag_principal/anadiendo_mascota/<int:id>', views.anadiendo_mascota, name='anadiendo_mascota'),
    path('pag_principal/ver_mascotas/<int:id>', views.ver_mascotas, name='ver_mascotas'),
]