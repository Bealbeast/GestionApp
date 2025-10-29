from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.management import  call_command
from .forms import TareaForm
from .models import Tarea

@login_required
def dashboard(request):
    UserTareas = Tarea.objects.filter(usuario=request.user, completada=False).order_by('fecha_limite')
    return render(request, 'dashboard.html', {'tareas': UserTareas})

@login_required
def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
    tarea.completada = True
    tarea.save()
    return redirect('dashboard')

@login_required
def desmarcar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
    tarea.completada = False
    tarea.save()
    return redirect('historial_tareas')

@login_required
def historial_tareas(request):
    tareas_completadas = Tarea.objects.filter(usuario=request.user, completada=True).order_by('-fecha_limite')
    return render(request, 'historial.html', {'tareas':tareas_completadas})

@login_required
def agregar_tarea(request): 
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect('dashboard')
    else:
        form = TareaForm()
    return render(request, 'agregar_tarea.html', {'form': form})


def home(request):
    return redirect('dashboard')

def ver_usuarios(request):
    usuarios = User.objects.all()
    return HttpResponse("<br>".join([u.username for u in usuarios]))

def ejecutar_migraciones(request):
    call_command('migrate')
    return HttpResponse("Migraciones ejecutadas")
