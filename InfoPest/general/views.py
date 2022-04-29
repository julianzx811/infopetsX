from django.shortcuts import render, reverse, redirect
from .models import usuarios, mascota,info_pets_empresas, veterinaria

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
    return render(request,'html/inicio.html',context)

def registrandome(request):
    return render(request, 'html/registro.html')

def registro(request):
    email = request.POST.get('email')
    usuarioxd = request.POST.get('uname')
    password = request.POST.get('psw')
    psw_repeat = request.POST.get('psw-repeat')
    edadd = request.POST.get('edad')
    sexoo = 'nose'
    nuevo_usuario = usuarios(veterinaria_id=veterinaria.objects.get(pk=1), usuario=usuarioxd, contrasena=password, email_user=email, sexo=sexoo, edad=edadd)
    nuevo_usuario.save()
    context = {}
    context['uname'] = usuarioxd
    return render(request, 'html/inicio.html', context)

def creando_mascota(request):
    return render(request, 'html/newMascota.html')

def ver_mascotas(request):
    return render(request, 'html/mascotas.html')