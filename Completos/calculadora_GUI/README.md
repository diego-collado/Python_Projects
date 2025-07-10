> [!IMPORTANT]
> <b>AdictoCalculator</b> es una calculadora con interfaz gráfica (GUI) simple y efectiva, desarrollada en Python 3.x, que permite al usuario realizar suma, resta, multiplicación, división y algunas funciones especiales como cambio de signo, inverso (1/x), borrar último carácter, limpiar todo.

> El proyecto tiene los siguientes propósitos:
- Interfaz gráfica (GUI) simple y efectiva usando Tkinter.
- Operaciones básicas: suma, resta, multiplicación, división.
- Funciones especiales: cambio de signo, inverso (1/x), borrar último carácter, limpiar todo.
- Manejo de errores comunes (división por cero, errores de sintaxis).
- Botonera interactiva con respuesta visual inmediata.

> Conceptos repasados en esta aplicación: 
- 1. <b>Programación orientada a objetos (POO)</b>
- 2. <b>Gestión de eventos y callbacks en interfaces gráficas</b>
- 3. <b>Widgets de Tkinter: Entry, Button, Frame</b>
- 4. <b>Validación y manejo de errores en expresiones</b>
- 5. <b>Diseño modular y reutilizable</b>
- 6. <b>Separación de lógica y vista (MVC básico)</b>

# 1.- AdictoCalculator
Este proyecto permite a un usuario utilizar funcionalidades básicas y específicas de una calculadora.

## 2.- Descripción general: 
<b>AdictoCalculator</b> es una aplicación de escritorio construida con Python y Tkinter que permite realizar cálculos matemáticos básicos. La calculadora está diseñada para ser intuitiva, rápida y personalizable. Se puede usar como proyecto base para extender funcionalidades como operaciones científicas, historial, o almacenamiento de resultados.

## 3.- Objetivos del Proyecto (SMART)
- Específico: Desarrollar una calculadora básica funcional con interfaz gráfica.
- Medible: Debe ejecutar correctamente al menos 10 operaciones diferentes.
- Alcanzable: Usar solo herramientas estándar de Python (Tkinter).
- Relevante: Refuerza conocimientos en GUI, OOP y buenas prácticas de desarrollo.
- Temporal: Proyecto completado en menos de una semana.

## 4.- Requisitos
- FUNCIONALES:
  · La aplicación debe mostrar un panel con botones de dígitos y operaciones.
  · El usuario puede introducir datos a través de los botones.
  · El campo de texto debe mostrar los cálculos realizados.
  · Los errores deben gestionarse visualmente con mensajes.
  · Botones de control como CE, Del, =, 1/x, +/- deben funcionar correctamente.

- NO FUNCIONALES:
    · La interfaz debe ser resistente a entradas inválidas.
    · La aplicación no debe permitir el cierre accidental sin confirmación (opcional).
    · Código debe ser modular y documentado.
    · Interfaz visual limpia y fácil de usar.

## 5.- Tecnologías a utilizar
- Lenguaje: Python 3.x
- Librerías:
  - Tkinter (GUI de Python)
  - unittest (para pruebas)
- Control de versiones: Git + GitHub
- Plataforma: Local (CLI)

## 6.- Estructura del Proyecto (Arquitectura)
adicto_calculator/
│── main.py
|
├── gui/
│   |_ calculator_gui.py
|
├── core/
│   |_ calculator_logic.py
│
├── tests/
│   ├── test_logic.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE

## 7.- Diagrama de Flujo (casos de uso)
- Adjunto en la carpeta

## 8.- Plan de desarrollo
- Semana 1 | Actividad: Separar lógica de UI, definir arquitectura
- Semana 2 | Actividad: Crear clases, funcionalidades
- Semana 3 | Actividad: Conectar lógica y GUI
- Semana 4 | Actividad: Crear y ejecutar pruebas unitarias
- Semana 5 | Actividad: Escribir pruebas unitarias
- Semana 6 | Actividad: README, instrucciones, licencia

## 9.- Testing
- Pruebas unitarias: 
    · Uso de unittest para funciones matemáticas (evaluate, changeSign, inverse).
    · Pruebas de excepciones: división por cero, entrada inválida.
    · Pruebas manuales de GUI: interacción con botones.

## 10.- Licencias y créditos
- Licencia: MIT License / Creative Commons (según elección)
- Autor/es: [Nombre/s del autor]
- Colaborador/es: XXX
- Inspirado en las calculadoras clásicas de escritorio
- Gracias a la comunidad Python por soporte y documentación.

## INSTRUCCIONES DE USO
- Instalación y configuración
```
git clone https://github.com/usuario/adicto_calculator.git
cd adicto_calculator
python main.py
```
- Instrucciones de uso:
   · Usar el mouse para hacer clic en los botones.
   · Botón CE: limpiar entrada.
   · Botón Del: borrar último carácter.
   · Botón +/-: cambiar signo.
   · Botón 1/x: invertir valor actual.
   · Botón =: resolver expresión