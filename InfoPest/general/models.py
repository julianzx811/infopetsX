import datetime
from django.db import models
from django.utils import timezone

class usuarios(models.Model):
    usuario = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200,null=False,default='no_contraseña')
    email_user = models.CharField(max_length=300, default='corre@hotmail.com')
    sexo = models.CharField(max_length=200, default='no llenado')
    edad = models.IntegerField(default=0)

    def __str__(self):
        return self.usuario + '-' + self.contrasena


class pets(models.Model):
    dueno_id = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    mascota_name =  models.CharField(max_length=200)
    edad = models.IntegerField(default=0)