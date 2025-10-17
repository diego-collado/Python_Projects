from django.db import models # importa la API de modelos de Django (gestor de archivos, templates...)

# se va a guardar todo en una BBDD, por lo que tenemos que instanciar clases
class Tarea(models.Model):
    titulo = models.CharField(max_length=120) # crear un campo corto (requerido) con 120 caracteres máximo
    hecho = models.BooleanField(default=False) # campo tipo checkbox, no marcado en principio
    creado_en = models.DateTimeField(auto_now=True) # campo fecha/hora donde se guardan los datos al crear el nuevo registro (auto_now: lo guarda según se crea)

    def __str__(self):
        return self.titulo # se ve el título de la tarea a realizar en nuestra aplicación