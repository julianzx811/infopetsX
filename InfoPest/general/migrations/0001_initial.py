# Generated by Django 3.2.5 on 2022-04-25 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info_pets_empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(default='no_telefono', max_length=200)),
                ('correo', models.CharField(default='corre@hotmail.com', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='veterinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.CharField(default='no_telefono', max_length=200)),
                ('correo', models.CharField(default='corre@hotmail.com', max_length=300)),
                ('empresa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.info_pets_empresas')),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=200)),
                ('contrasena', models.CharField(default='no_contraseña', max_length=200)),
                ('email_user', models.CharField(default='corre@hotmail.com', max_length=300)),
                ('sexo', models.CharField(default='no llenado', max_length=200)),
                ('edad', models.IntegerField(default=0)),
                ('veterinaria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.veterinaria')),
            ],
        ),
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mascota_name', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default=0)),
                ('sexo', models.CharField(default='no llenado', max_length=200)),
                ('dueno_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='historial_clinico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mascota_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='citas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mascota_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.mascota')),
                ('veterinario_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.usuarios')),
            ],
        ),
    ]
