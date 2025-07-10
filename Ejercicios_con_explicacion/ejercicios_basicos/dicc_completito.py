'''
Manejando los diccionarios de forma definitiva


# Creación de diccionario

persona = {} # creación de un diccionario vacío
persona = {
    "Nombre":"Diego",
    "Edad":48,
    "Profesión":"Docente",
    "Habilidades":["Programación","Sistemas & Redes", "Hacking/Pentest"],
    "Dirección": {
        "Ciudad":"Toledo",
        "País":"España"
    }
} # carga "a lo bruto" del diccionario

# Accediendo a los valores
print(persona["Nombre"])
print(persona["Habilidades"][2])

# Usando get y evitando errores
print(persona["Dirección"]["Ciudad"])
print(persona.get("Dirección","No existe"))# Si utilizamos GET y no encuentra lo que le pides, se va a la 2ª opción, en este caso, ERROR
print(persona.get("Dirección",{}).get("Ciudad","Error, no existe esta información"))
print(persona["Dirección"].get("Ciudad","Error......"))

# Modificando el valor de algo
persona["Edad"] = 49

# Añadiendo "cositas"
persona["email"] = "diego.collado@loquesea.es"

# Mostrando claves y valores
print("Claves:")
for clave in persona.keys():
    print(clave)

print("Valores:")
for valor in persona.values():
    print(valor)

print("Clave - Valor")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# "Accionando" nuestros diccionarios
persona_copia = persona.copy() # copiamos el contenido de persona en persona_copia
persona_copia.clear() # limpiamos el diccionario copiado

# verificando la existencia de "cosas"
if "Edad" in persona:
    print(f"Edad: {persona['Edad']} años")'''

# Diccionario de diccionarios
empresa = {
    "empleado_1":{"Nombre":"Diego","Edad":48},
    "empleado_2":{"Nombre":"Marta","Edad":48},
    "empleado_3":{"Nombre":"Izan","Edad":8},
    "empleado_4":{"Nombre":"Adrián","Edad":10}
}

print("\n\n ### Listado de empleados ###")
for num_empleado,datos_empleado in empresa.items():
    print(f"ID empleado: {num_empleado}:")
    print(f"Nombre: {datos_empleado['Nombre']}\nEdad: {datos_empleado['Edad']}")