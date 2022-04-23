from django.urls import path
from . import views
#usuarios.objects.filter(usuario__startswith='yulian')
app_name = 'general'
urlpatterns = [
    # ex: /general/
    path('', views.inicio, name='inicio'),
    # ex: /general/5/
    path('lol/', views.pag_principal, name='pag_principal'),
    # ex: /general/5/results/
    path('registro/', views.results, name='results'),
    # ex: /general/5/vote/
    path('vote/', views.registro, name='registro'),
]