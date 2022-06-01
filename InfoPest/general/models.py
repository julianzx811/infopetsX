import datetime
from django.db import models
from django.utils import timezone

class info_pets_empresas(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200, null=False, default='no_telefono')
    correo = models.CharField(max_length=300, default='corre@hotmail.com')

class veterinaria(models.Model):
    empresa_id = models.ForeignKey(info_pets_empresas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200, null=False, default='no_telefono')
    correo = models.CharField(max_length=300, default='corre@hotmail.com')

class veterinarios(models.Model):
    veterinaria_id = models.ForeignKey(veterinaria, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=200)
    contrasena = models.CharField(max_length=200,null=False,default='no_contraseña')
    email_user = models.CharField(max_length=300, default='corre@hotmail.com')
    sexo = models.CharField(max_length=200, default='no llenado')
    edad = models.IntegerField(default=0)

    def __str__(self):
        return self.usuario + '-' + self.contrasena

class mascota(models.Model):
    dueno_id = models.ForeignKey(veterinarios, on_delete=models.CASCADE)
    mascota_name = models.CharField(max_length=200)
    edad = models.IntegerField(default=0)
    sexo = models.CharField(max_length=200, default='no llenado')

class historial_clinico(models.Model):
    mascota_id = models.ForeignKey(mascota, on_delete=models.CASCADE)
    mascota_historial = models.CharField(max_length=2000, default='historial vacio')

class citas(models.Model):
    veterinario_id = models.ForeignKey(veterinarios, on_delete=models.CASCADE)
    mascota_id = models.ForeignKey(mascota, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField(default=timezone.now)
    razon = models.CharField(max_length=400, default='sin razon aparente')

