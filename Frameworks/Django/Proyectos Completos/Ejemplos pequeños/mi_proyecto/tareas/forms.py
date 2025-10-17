from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm): # lo utilizamos para poder codificar los campos HTML
    class Meta: # configuramos el formulario, donde aparecerán los registros (con el título, claro)
        model = Tarea
        fields = ['titulo']