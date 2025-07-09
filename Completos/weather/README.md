> [!IMPORTANT]
> <b>Weather CLI App</b> es una aplicación de línea de comandos (CLI) desarrollada en Python 3, que permite a los usuarios obtener información meteorológica en tiempo real para cualquier ciudad del mundo, conectándose a una API externa (OpenWeatherMap).
> Este proyecto busca facilitar el acceso rápido a los datos del clima desde un entorno local sin necesidad de interfaces gráficas o navegadores web, permitiendo su uso en contextos donde se requiere eficiencia, rapidez y portabilidad.
> Qué hará este bot: El sistema hace uso de la API RESTful de <b>OpenWeatherMap</b>, procesando y mostrando al usuario datos como:
- Temperatura actual
- Sensación térmica
- Estado del clima (ej. "nublado", "lluvioso")
- Humedad
- Velocidad del viento

> El proyecto tiene los siguientes propósitos:
- Proporcionar una herramienta práctica para consultar rápidamente el estado del tiempo.
- Fomentar el uso de APIs públicas y la integración de servicios externos en proyectos locales.
- Demostrar el uso de conceptos clave como programación modular, pruebas unitarias y control de versiones.
- Servir como base educativa para proyectos más complejos en desarrollo de software y ciencia de datos.

> Características principales:
- Entrada de ciudad por línea de comandos
- Conexión directa con API de OpenWeatherMap
- Manejo de errores: ciudades no encontradas, errores de red, claves API inválidas
- Formato limpio y comprensible en la salida
- Modularidad del código (separación de lógica principal, configuración y control)
- Pruebas unitarias con cobertura de errores comunes
- Documentación clara y completa

> Conceptos repasados en esta aplicación: 
- 1. <b>Módulos y organización del código</b>: 
  - PSeparación de la lógica del programa en distintos archivos: main.py, weather.py, config.py.
  - Uso del patrón if __name__ == "__main__" para ejecutar scripts correctamente.
- 2. <b>Importación de librerías</b>: 
  - Importación estándar (import os, import sys, import argparse).
  - Uso de librerías externas (requests) para acceder a recursos de red.

- 3. <b>Consumo de APIs (HTTP requests)</b>:
  - Uso del módulo requests para realizar llamadas HTTP (GET).
  - Procesamiento de respuestas JSON (response.json()).
  - Manejo de errores con try-except, status_code, y excepciones específicas.

- 4. <b>Manejo de JSON</b>:
  - Parseo de datos en formato JSON provenientes de una API.
  - Extracción de valores clave en diccionarios anidados.

- 5. <b>Argumentos desde la línea de comandos</b>:
  - Uso del módulo argparse para recibir argumentos como --city.
  - Validación y lectura de parámetros desde CLI.

- 6. <b>Funciones</b>:
  - Definición de funciones reutilizables con def.
  - Uso de return, parámetros con valor por defecto, docstrings y tipado básico.

- 7. <b>Estructuras de control</b>:
  - Condicionales (if, else, elif) para validaciones.
  - Bucles (si se implementa lógica de múltiples ciudades o intentos).

- 8. <b>Excepciones y manejo de errores</b>:
  - Captura de excepciones comunes (errores de red, errores en la respuesta, entradas inválidas).
  - Personalización de mensajes de error para el usuario.

- 9. <b>Pruebas unitarias</b>:
  - Uso del módulo unittest para definir pruebas automáticas.
  - Simulación de llamadas API (mocking, opcional).
  - Verificación de salidas esperadas, manejo de errores, y edge cases.

- 10. <b>Variables de entorno</b>:
  - Uso de os.environ.get("API_KEY") para leer claves privadas sin exponerlas en el código fuente.

- 11. <b>Estilo y buenas prácticas</b>:
  - Comentarios y docstrings para documentar funciones y módulos.
  - Organización modular.
  - Uso de requirements.txt para manejo de dependencias.
  - Git y GitHub para control de versiones.

# 1.- Weather API
Este proyecto busca facilitar el acceso rápido a los datos del clima desde un entorno local sin necesidad de interfaces gráficas o navegadores web.

## 2.- Descripción general: 
Weather CLI App es una aplicación de línea de comandos (CLI) desarrollada en Python 3, que permite a los usuarios obtener información meteorológica en tiempo real para cualquier ciudad del mundo, conectándose a una API externa (por defecto, OpenWeatherMap).

Este proyecto busca facilitar el acceso rápido a los datos del clima desde un entorno local sin necesidad de interfaces gráficas o navegadores web, permitiendo su uso en contextos donde se requiere eficiencia, rapidez y portabilidad (como scripts de automatización, servidores o uso académico).

El sistema hace uso de la API RESTful de OpenWeatherMap, procesando y mostrando al usuario datos como:
 - Temperatura actual
 - Sensación térmica
 - Estado del clima (ej. "nublado", "lluvioso")
 - Humedad
 - Velocidad del viento

## 3.- Objetivos del Proyecto (SMART)
- Específico: Desarrollar una aplicación de línea de comandos para consultar la temperatura de una ciudad específica en tiempo real.
- Medible: La aplicación permitirá consultar al menos 5 ciudades diferentes y retornará los datos meteorológicos principales.
- Alcanzable: El proyecto será desarrollado en Python 3 utilizando requests y argparse, y se integrará con la API de OpenWeatherMap.
- Relevante: Permitirá a los usuarios acceder fácilmente a información meteorológica sin necesidad de interfaces gráficas.
- Temporal: El desarrollo debe completarse en 7 días, incluyendo pruebas y documentación.

## 4.- Requisitos
- FUNCIONALES:
  · El usuario puede ingresar el nombre de una ciudad y obtener:
    - - Temperatura actual
    - - Sensación térmica
    - - Descripción del clima
  · El sistema obtiene datos desde una API externa (OpenWeatherMap).
  · Validación de entradas del usuario (ciudades inválidas, errores de red).  
- NO FUNCIONALES:
    · Respuesta de la API en menos de 2 segundos.
    · El código debe estar comentado y seguir buenas prácticas de estilo (PEP8).
    · Compatible con Python 3.8 o superior.
    · oporte multiplataforma (Windows, Linux, macOS).

## 5.- Tecnologías a utilizar
- Lenguaje: Python 3.x
- Librerías:
  - requests (para llamar a la API)
  - argparse (para argumentos de línea de comandos)
  - unittest (para pruebas)
- Control de versiones: Git + GitHub
- Plataforma: Local (CLI)

## 6.- Estructura del Proyecto (Arquitectura)
weather-cli/
│
├── src/
│   ├── main.py
│   ├── weather.py
│   └── config.py
│
├── tests/
│   ├── test_weather.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE

## 7.- Diagrama de Flujo (casos de uso)
- Adjunto en la carpeta

## 8.- Plan de desarrollo
- Semana 1 | Actividad: Inicializar repositorio, estructura base, conectar API
- Semana 2 | Actividad: Implementar lógica principal (weather.py)
- Semana 3 | Actividad: Integrar argparse, refactorizar entrada
- Semana 4 | Actividad: Manejo de errores y validaciones
- Semana 5 | Actividad: Escribir pruebas unitarias
- Semana 6 | Actividad: Documentación y README
- Semana 7 | Actividad: Revisión final y entrega

## 9.- Testing
- Pruebas unitarias: 
    · Respuestas válidas de la API (mock)
    · Manejo de errores (ciudad no encontrada, sin conexión)
    · Parsing correcto de la información

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
- Instalación y configuración
```
git clone https://github.com/usuario/weather-cli.git
cd weather-cli
```
- Instalar dependencias:
```
pip install -r requirements.txt
```
- API key:
```
export API_KEY=tu_api_key_aqui
```

- Instrucciones de uso:
```
python src/main.py --city "Toledo"
```