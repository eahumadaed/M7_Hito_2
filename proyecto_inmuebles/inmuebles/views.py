from django.shortcuts import render, redirect
from .services import crear_usuario, obtener_usuario, actualizar_usuario, eliminar_usuario
from .forms import UsuarioForm

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/list.html', {'usuarios': usuarios})

def usuario_detail(request, id):
    usuario = obtener_usuario(id)
    return render(request, 'usuarios/detail.html', {'usuario': usuario})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            crear_usuario(form.cleaned_data)
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form.html', {'form': form})

def usuario_update(request, id):
    usuario = obtener_usuario(id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            actualizar_usuario(id, form.cleaned_data)
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/form.html', {'form': form})

def usuario_delete(request, id):
    eliminar_usuario(id)
    return redirect('usuario_list')
