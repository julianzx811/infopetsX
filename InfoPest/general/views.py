from django.shortcuts import render, get_object_or_404
from .models import Question, Choice, usuarios

# return render(request, 'polls/index.html', context)

def inicio(request):
    return render(request, 'html/login.html')

def pag_principal(request):
    context = {}
    usuario = request.POST.get('uname')
    contrasena = request.POST.get('psw')
    usuario_query = usuarios.objects.filter(usuario=usuario)
    contrasena_query = usuarios.objects.filter(contrasena=contrasena)
    if not usuario_query and not usuario_query:
        context['uname'] = 'no'
        context['psw'] = 'no'
    else:
        context['uname'] = usuario
        context['psw'] = contrasena
    return render(request, 'html/inicio.html',context)

def results(request):
    return render(request, 'html/registro.html')

def registro(request):
    email = request.POST.get('email')
    usuarioxd = request.POST.get('uname')
    password = request.POST.get('psw')
    psw_repeat = request.POST.get('psw-repeat')
    edadd = request.POST.get('edad')
    sexoo = 'nose'
    nuevo_usuario = usuarios(usuario=usuarioxd, contrasena=password, email_user=email, sexo=sexoo, edad=edadd)
    nuevo_usuario.save()
    context = {}
    context['uname'] = usuarioxd
    return render(request, 'html/inicio.html', context)