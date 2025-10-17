from django.shortcuts import render
from django.http import HttpResponse # controla el envío de respuestas al navegador (browser)
# esta clase representa la respuesta HTTP que devolverá la vista (el cuerpo, cabecera...)

# FUNCTIONS
def saludo(request): # request es obligatorio, es la petición que le hacemos como tal (objeto con los datos de la petición)
    return HttpResponse('¡¡<b>Hola</b>, mundo mundial!!<br> ¿Qué pacha nennnnn? <br>Estamos aquín reuniossssss') # devuelve el objeto con el texto plano que verá el usuario en el browser