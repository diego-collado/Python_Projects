'''
Trabajando con PDF: abrir un archivo PDF desde Python utilizando la aplicación por defecto de nuestro
sistema operativo.
'''

# Abrir visor estándar de PDF: Acrobat Reader o similares - se abre un shell intermedio (tipo CMD)
import os # https://docs.python.org/es/3.10/library/os.html
path = 'demo.pdf' # ruta en la que está mi archivo, considerando que donde está el py es la raíz
os.system(path) # "manipula este archivo"

# Abrir visor estándar de PDF: Acrobat Reader o similares - sin utilizar shell intermedio, directo al visor
import webbrowser # https://docs.python.org/es/3/library/webbrowser.html
path = 'demo.pdf' # ruta en la que está mi archivo, considerando que donde está el py es la raíz
webbrowser.open_new(path) # "manipula este archivo"