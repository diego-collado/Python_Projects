from django.shortcuts import render, redirect, get_list_or_404
# renderiza tanto la página como tal, además de utilizar redirecciones y errores 404

# importamos todo lo que hemos creado anteriormente
from .models import Tarea
from .forms import TareaForm

# 1ª vista: lista de tareas -----------------------------------------------------------------
def lista_tareas(request):
    # consultar ORM: muestra todas las tareas ordenadas desde las nuevas hasta las viejas
    tareas = Tarea.objects.order_by('-creado_en')

    # renderizamos la lista para poder verla
    return render(request, 'tareas/lista.html',{'tareas':tareas})

# 2ª vista: crear tareas --------------------------------------------------------------------
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)

        if form.is_valid():
            form.save() # se guarda realmente en la BBDD
            return redirect('tareas:lista')
    else:
        form = TareaForm()# si la tarea se pide por GET, mostrará un formulario vacío
    
    return render(request, 'tareas/crear.html',{'form':form})

# 3ª vista: alternar tareas -----------------------------------------------------------------
def alternar_tareas(request,pk): # hacer el toggle, es decir, marcar/desmarcar
    tarea = get_list_or_404(Tarea,pk=pk)
    tarea.hecho = not tarea.hecho
    tarea.save()
    return redirect('tareas:lista')
    # busca la tarea, invierte si está hecha o no y lo guarda en la BBDD, para volver a la lista

# 4ª vista: eliminar tareas -----------------------------------------------------------------
def eliminar_tareas(request,pk):
    tarea = get_list_or_404(Tarea,pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas:lista')
    return render(request, 'tareas/confirmar_eliminar.html',{'tarea':tarea})