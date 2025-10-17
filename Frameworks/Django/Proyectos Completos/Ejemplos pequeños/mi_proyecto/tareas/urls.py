from django.urls import path
from . import views

app_name = 'tareas'

urlpatterns = [
    path('',views.lista_tareas, name='lista'),
    path('crear/',views.crear_tarea, name='crear'),
    path('<int:pk>/toggle/',views.alternar_tareas, name='alternar'),
    path('<int:pk>/eliminar/',views.eliminar_tareas, name='eliminar'),
]