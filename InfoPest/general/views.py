from django.shortcuts import render, reverse, redirect
from .models import veterinarios, mascota, info_pets_empresas, veterinaria, historial_clinico, citas
from django.http import HttpResponse
# return render(request, 'polls/index.html', context)

def inicio(request):
    return render(request, 'html/login.html')

def redirect_pag_principal(request):
    usuario_ = request.POST.get('uname')
    contrasena_ = request.POST.get('psw')
    #metodo con post para autenticar de que el usuario exista
    usuario_query = veterinarios.objects.filter(usuario=usuario_)
    contrasena_query = veterinarios.objects.filter(contrasena=contrasena_)
    if usuario_query.exists() and contrasena_query.exists():
        id = veterinarios.objects.get(usuario=usuario_)
        return pag_principal(request, id.id)
    else:
        return pag_principal(request, 0)

def pag_principal(request,id):
    context = {}
    if id == 0:
        context['uname'] = 'no'
        context['psw'] = 'no'
    else:
        usuario = veterinarios.objects.get(id=id)
        context['uname'] = usuario.usuario
        context['psw'] = usuario.contrasena
        context['id'] = usuario.id
    return render(request,'html/inicio.html',context)

def registrandome(request):
    veterinarias = veterinaria.objects.all()
    context = {'veterinarias': veterinarias}
    return render(request, 'html/registro.html',context)

def registro(request):
    email = request.POST.get('email')
    usuarioxd = request.POST.get('uname')
    password = request.POST.get('psw')
    psw_repeat = request.POST.get('psw-repeat')
    edadd = request.POST.get('edad')
    sexoo = request.POST['select']
    veterinaria_id = request.POST['select_veterinarias']
    nuevo_usuario = veterinarios(veterinaria_id=veterinaria.objects.get(pk=veterinaria_id), usuario=usuarioxd, contrasena=password, email_user=email, sexo=sexoo, edad=edadd)
    nuevo_usuario.save()
    id = nuevo_usuario.id
    return pag_principal(request, id)

def creando_mascota(request,id):
    return render(request, 'html/newMascota.html',{'id':id})

def anadiendo_mascota(request,id):
    nombre = request.POST.get('nombre')
    edad = request.POST.get('edad')
    sexo = sexoo = request.POST['select']
    new_mascota = mascota(dueno_id=veterinarios.objects.get(pk=id),mascota_name=nombre,edad=edad,sexo=sexo)
    new_mascota.save()
    new_historial_mascota = historial_clinico(mascota_id=mascota.objects.get(pk=new_mascota.id),mascota_historial='historial vacio')
    new_historial_mascota.save()
    return pag_principal(request, id)

def ver_mascotas(request,id):
    mascotas = mascota.objects.filter(dueno_id=id)
    context = {'mascotas': mascotas,'id':id}
    return render(request, 'html/mascotas.html',context)

def info_mascota(request,id):
    mascotas = mascota.objects.get(pk=id)
    dueno_id = mascotas.dueno_id
    mascota_name = mascotas.mascota_name
    edad = mascotas.edad
    sexo = mascotas.sexo
    historial = historial_clinico.objects.get(mascota_id=mascotas.id)
    context = {'dueno_id':dueno_id , 'mascota_name':mascota_name , 'edad':edad, 'sexo':sexo,'historial':historial.mascota_historial}
    return render(request, 'html/info_mascota.html', context)

def ver_mascotas_usuario(request):
    mascota_name = request.POST.get('mascota_name')
    mascotas = mascota.objects.filter(mascota_name__startswith=mascota_name)
    context = {'mascotas': mascotas}
    return render(request, 'html/ver_mascotas.html', context)

def agregar_cita(request,id):
    mascotas = mascota.objects.filter(dueno_id=id)
    context = {'mascotas': mascotas, 'id':id}
    return render(request, 'html/agregar_cita.html',context)

def guardar_cita(request,id):
    fecha = request.POST.get('fecha')
    mascota_id = request.POST.get('select_mascotas')
    razon = request.POST.get('razon')
    cita = citas(veterinario_id=veterinarios.objects.get(pk=id), mascota_id=mascota.objects.get(pk=mascota_id), fecha_cita=fecha, razon=razon)
    cita.save()
    return pag_principal(request, id)
