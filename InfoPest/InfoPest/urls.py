#password: usbcali
from django.contrib import admin
from django.urls import path, include
from general import views

urlpatterns = [
    path('general/', include('general.urls')),
    path('', views.inicio, name='incio'),
]