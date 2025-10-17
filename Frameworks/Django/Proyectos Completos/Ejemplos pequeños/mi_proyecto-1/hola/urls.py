from django.urls import path # gestión de rutas de forma "legible"
from . import views # importa el módulo views de la misma app
# . significa desde el paquete actual, para luego buscar views.saludo

# PATTERNS
urlpatterns = [
    path('', views.saludo, name='saludo')
] # lista donde se registran la urls de la aplicación

'''
''             --> ruta vacía que se asigna a este aplicación (la ruta sería mi_proyecto/urls.py)
views.saludo   --> vista que vamos a mostrar cuando se ejecute la url que nos pedirá el usuario
name='saludo'  --> asignamos un nombre a la ruta para poder hacer un REVERSE, que es construir las 
urls por nombre en templates/codigo
'''