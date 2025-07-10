# validaciones.py --> define las validaciones a realizar en la entrada de datos

# IMPORTS -----------------------------------------------
import re #https://docs.python.org/es/3/library/re.html

'''
-- EXPRESIONES REGULARES TÍPICAS PARA PYTHON --

· email                   -->   r"[^@]+[@][^@]+\.[^@]+"     <--> diego.collado@mio.es
· teléfono (sólo números) -->   r"^\d{7,15}$"               <--> 123456789
· letras (sin espacios)   -->   r"^[a-zA-Z]+$"              <--> Diego
· letras (con espacios)   -->   r"^[a-zA-Z\s]+$"            <--> Diego Collado
· sólo números            -->   r"^\d+$"                    <--> 12345
· alfanumérico            -->   r"^[a-zA-Z0-9]+$"           <--> Diego123
· password seguro         -->   r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$" <--> clave1234
· fechas (dd/mm/aaaa)     -->   r"^\d{2}/\d{2}/\d{4}$"      <--> 02/07/2025
· URL                     -->   r"^https?://[\w./-]+$"      <--> https://diego.es
· código postal           -->   r"^\d{5}$"                  <--> 45007
· DNI                     -->   r"^\d{8}[A-Za-z]$"          <--> 03800336T
· NIE                     -->   r"^[XYZ]\d{7}[A-Z]$"        <--> Z03800336T
'''


# FUNCTIONS -----------------------------------------------
def validar_nombre(nombre):
    return bool(nombre.strip()) # evitamos que introduzcan espacios en blanco o dejen vacío el nombre

def validar_telefono(telefono):
    return telefono.isdigit() and len(telefono) == 9
# isdigit --> comprueba si hay o no dígitos en el string

def validar_email(email):
    if not email:
        return True
    return re.match(r"[^@]+[@][^@]+\.[^@]+",email) # si tiene coincidencia con el patrón marcado