from django.shortcuts import render, reverse, redirect
from .models import usuarios, mascota,info_pets_empresas, veterinaria
from django.http import HttpResponse
# return render(request, 'polls/index.html', context)

def inicio(request):
    return render(request, 'html/login.html')

def redirect_pag_principal(request):
    usuario_ = request.POST.get('uname')
    contrasena_ = request.POST.get('psw')
    #metodo con post para autenticar de que el usuario exista
    usuario_query = usuarios.objects.filter(usuario=usuario_)
    contrasena_query = usuarios.objects.filter(contrasena=contrasena_)
    if usuario_query.exists() and contrasena_query.exists():
        id = usuarios.objects.get(usuario=usuario_)
        return pag_principal(request, id.id)
    else:
        return pag_principal(request, 0)

def pag_principal(request,id):
    context = {}
    if id == 0:
        context['uname'] = 'no'
        context['psw'] = 'no'
    else:
        usuario = usuarios.objects.get(id=id)
        context['uname'] = usuario.usuario
        context['psw'] = usuario.contrasena
        context['id'] = usuario.id
    return render(request,'html/inicio.html',context)

def registrandome(request):
    return render(request, 'html/registro.html')

def registro(request):
    email = request.POST.get('email')
    usuarioxd = request.POST.get('uname')
    password = request.POST.get('psw')
    psw_repeat = request.POST.get('psw-repeat')
    edadd = request.POST.get('edad')
    sexoo = request.POST['select']
    nuevo_usuario = usuarios(veterinaria_id=veterinaria.objects.get(pk=1), usuario=usuarioxd, contrasena=password, email_user=email, sexo=sexoo, edad=edadd)
    nuevo_usuario.save()
    id = nuevo_usuario.id
    context = {}
    context['uname'] = usuarioxd
    return pag_principal(request,id)

def creando_mascota(request,id):
    return render(request, 'html/newMascota.html',{'id':id})

def anadiendo_mascota(request,id):
    nombre = request.POST.get('nombre')
    edad = request.POST.get('edad')
    sexo = sexoo = request.POST['select']
    new_mascota = mascota(dueno_id=usuarios.objects.get(pk=id),mascota_name=nombre,edad=edad,sexo=sexo)
    new_mascota.save()
    return pag_principal(request, id)

def ver_mascotas(request,id):
    mascotas = mascota.objects.filter(dueno_id=id)
    context = {'mascotas': mascotas}
    return render(request, 'html/mascotas.html',context)
