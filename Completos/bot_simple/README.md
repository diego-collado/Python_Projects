> [!IMPORTANT]
> El proyecto <b>bot simple</b> nos permite crear un bot completamente independiente de Internet, desarrollado en Python, que funciona offline, aprende de lo que se escribe, es sencillo y se ejecuta en consola, además que guarda lo aprendido para futuras conversaciones.
> Qué hará este bot:
  - Si conoce la respuesta → te responde.
  - Si no la conoce → te pregunta qué debería decir.
  - Guarda lo aprendido en un archivo .json.

> Este proyecto normalmente se hace como una aplicación de consola, y se estructura en:
- Busca las respuestas en su memoria aprendida
- Consulta un archivo de conocimientos (conocimiento.txt) si no sabe algo
- Pregunta si aún no tiene respuesta, y aprende de lo que se le enseñe

> Conceptos repasados en esta aplicación: 
- 1. <b>Diccionarios</b>: 
  - Para guardar y consultar pares pregunta–respuesta (memoria real del bot).
  - Ideal para búsquedas rápidas por clave.

- 2. <b>Lectura y escritura de archivos</b>: 
  - open(), with, read(), write() para trabajar con archivos de texto (.json, .txt).
  - Leer datos de conocimiento (conocimiento.txt) y guardar lo aprendido (memoria.json).

- 3. <b>Manejo de archivos JSON</b>:
  - Uso del módulo json para guardar y cargar información estructurada de manera persistente.
  - Funciones: json.load(), json.dump().

- 4. <b>Condicionales (if, else)</b>:
  - Para decidir si el bot responde desde la memoria, el conocimiento, o necesita aprender algo nuevo.

- 5. <b>Cadenas (str)</b>:
  - Transformaciones como .lower(), .strip(), .split() para manejar entradas del usuario.
  - Comparación de strings para encontrar coincidencias.

- 6. <b>Bucles</b>:
  - while True para mantener el bot activo.
  - for para recorrer líneas del conocimiento y buscar coincidencias.

- 7. <b>Funciones</b>:
  - Para estructurar el código en bloques reutilizables como responder(), aprender(), cargar_memoria()...

- 8. <b>Manejo de errores</b>: 
  - Se puede usar try-except al trabajar con archivos o entrada del usuario para hacerlo más robusto.

- 9. <b>Persistencia de datos</b>:
  - El bot "aprende" porque guarda información de una sesión a otra.

# 1.- SimpleBot
Bot simple, desarrollado en Python, con funcionalidades de aprendizaje automático

## 2.- Descripción general: 
Este proyecto tiene como objetivo el desarrollo de una aplicación basada en inteligencia artificial utilizando Python 3.x. El sistema simula un entorno de juego/interacción donde la IA responde a entradas del usuario siguiendo reglas predefinidas. La aplicación es modular, extensible y diseñada con principios de arquitectura limpia para facilitar el mantenimiento y escalabilidad.

## 3.- Objetivos del Proyecto (SMART)
- Específico: Desarrollar una IA capaz de interactuar con el usuario en un entorno definido, respetando las reglas programadas.
- Medible: Alcanzar al menos un 90% de cobertura en las pruebas unitarias y cumplir con todos los casos de uso establecidos.
- Alcanzable: Utilizando tecnologías conocidas (Python, PyTest, Git), con un alcance definido para el MVP.
- Relevante: Brinda un ejemplo funcional de desarrollo modular con IA para propósitos educativos o de entretenimiento.
- Temporal: El proyecto será completado en un plazo de 8 semanas desde el inicio del desarrollo.

## 4.- Requisitos
- FUNCIONALES:
    · El sistema debe permitir al usuario iniciar una nueva sesión de juego/interacción.
    · La IA debe interpretar las acciones del usuario y responder adecuadamente.
    · El sistema debe registrar los eventos relevantes del flujo de ejecución.
- NO FUNCIONALES:
    · El sistema debe ejecutarse en menos de 2 segundos por acción del usuario.
    · El código debe estar documentado con estilo PEP8.
    · La solución debe ser multiplataforma (Windows, Linux, macOS).
    · La arquitectura debe permitir pruebas unitarias de todos los módulos.

## 5.- Tecnologías a utilizar
- Lenguaje: Python 3.x
- Librerías:
  - random, json, os (estándar)
  - PyTest (para testing)
  - numpy o pandas si se requiere manejo de datos
  - Control de versiones: Git + GitHub
  - Plataforma: Local (CLI o GUI) / Web (si aplica, usar Flask o FastAPI)

## 6.- Estructura del Proyecto (Arquitectura)
/SimpleBot
    |
    |_ main.py 
    |
    |_ conocimiento.txt
    |
    |_ memoria.json
    |
    |__ ia
    |   |_ engine.py 
    |
    |__ game
    |   |_ logic.py 
    |
    |__ utils
    |   |_helpers.py 
    |
    |__ test               
    |     |_ test_logic.py   
    | 
    |__ docs               
    |     |_ diagrams           
    |
    |_ README.md                
    |_ requirements.txt
    |_ .gitignore         

## 7.- Diagrama de Flujo (casos de uso)
- Adjunto en la carpeta

## 8.- Plan de desarrollo
- Semana 1 | Actividad: Definición de requisitos, estructura y repositorio
- Semana 2 | Actividad: Implementación del motor base de la IA
- Semana 3 | Actividad: Programación de reglas de juego/interacción
- Semana 4 | Actividad: Diseño de interfaz CLI o GUI
- Semana 5 | Actividad: Implementación de pruebas unitarias
- Semana 6 | Actividad: Documentación y optimización del código
- Semana 7 | Actividad: Revisión final y entrega

## 9.- Testing
- Pruebas unitarias: 
    · Validación de entrada del usuario
    · Lógica de decisiones de la IA
    · Reglas de interacción
- Herramientas: PyTest y cobertura con pytest-cov

## 10.- Documentación
- README.md:
    · Instalación y configuración
    · Instrucciones de uso (comandos y controles)
    · Descripción de la IA y su funcionamiento
    · Reglas y condiciones del juego/sistema

- Documentación del código:
    · Comentarios en funciones y clases
    · Archivos de prueba con explicación de cada test case

## 11.- Licencias y créditos
- Licencia: MIT License / Creative Commons (según elección)
- Autor/es: [Nombre/s del autor]
- Colaborador/es: XXX
- Fuentes externas:
   - Algoritmo base de IA
   - Recursos visuales/sónicos de uso libre si aplica

## INSTRUCCIONES DE USO
- Clonar el repositorio:
```
git clone https://github.com/usuario/proyecto.git
cd proyecto
```
- Crear y activar un entorno virtual:
```
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```
- Instalar dependencias
```
pip install -r requirements.txt
```
- Ejecutar la aplicación:
```
python src/main.py
```

- Ejecutar pruebas unitarias:
```
pytest tests/
```