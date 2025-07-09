# 1.- 3enRayaPy
Juego clásico de 3 en raya, desarrollado en Python

## 2.- Descripción general: 
3enRayaPy es el juego clásico de 3 en raya (Tic-Tac-Toe) diseñado para poder jugarse en la consola de Python. 

Permite que 2 jugadores se enfrenten en un tablero de 3x3, donde el primer jugador que consiga alinear 3 símbolos consecutivos (horizontal, vertical o diagonal) gana la partida.

En esta versión, se puede bien jugar contra un humano o contra el PC (IA básica).

Este pequeño proyecto resuelve el problema de ofrecer un entretenimiento simple y educativo, ideal para aprender lógica básica y algoritmia, así como para aquell@s que buscan un juego casual para jugar en sus pocos ratos libres.

## 3.- Objetivos del Proyecto (SMART)
1.- Permitir a los jugadores seleccionar si quieren jugar contra otro jugador o contra el PC
2.- Proveer de una interfaz simple y clara de tipo CLI(Command LIne, en consola)
3.- Implementar un algoritmo básico de IA para que el usuario pueda jugar contra el PC
4.- Permitir que el juego detecte automáticamente el ganador y termine la partida
5.- Reiniciar o finalizar el juego después que un jugador haya ganado o se produzca un empate.

## 4.- Requisitos
- FUNCIONALES:
    · El sistema debe permitir a los jugadores colocar sus símbolos en el tablero
    · El sistema debe permitir jugar contra un humano o contra el PC
    · El juego debe anunciar al ganador o si la partida terminó en empate
    · El tablero debe actualizarse después de cada jugada, es decir, debe reflejar las nuevas posiciones de los símbolos
    · El sistema debe detectar entradas inválidas y pedir nueva jugada si llegase el caso
- NO FUNCIONALES:
    · El juego se debe cargar en menos de 1 segundo
    · La CLI debe ser clara y legible por el jugador
    · El juego debería ser capaz de ejecutarse en la consola sin necesidad de instalar dependencias adicionales (es apto para poder jugar en cualquier consola/terminal de Python)

## 5.- Tecnologías a utilizar
- Lenguaje: Python 3.x
- Librerías: en este caso no se utilizarán librerías externas, solo aquellas que vienen por defecto instaladas en Python
- Control de versiones: Git + Github
- Plataforma: Consola (entorno local - CLI)

## 6.- Estructura del Proyecto (Arquitectura)
/3enRayaPy
    |__ src
    |    |__ game                contiene la lógica principal del juego
    |    |    |_ __init__.py  
    |    |    |_ board.py        maneja la creación/estado del tablero
    |    |    |_ player.py       define jugadores (IA / humanos)
    |    |    |_ ai.py           implementa la IA básica
    |    |    |_ game.py         lógica (jugadas) e interacción jugador
    |    |
    |    |__ test                contiene las PRUEBAS UNITARIAS
    |         |_ test_board.py   valida el tablero y sus reglas
    |         |_ test_player.py  valida el jugador y la interacción
    |         |_ test_ai.py      valida la IA y la interacción
    |_ main.py                   archivo de ejecución principal
    |_ README.md                 instrucciones del juego
    |_ requirements.txt          instalación de dependencias de 3º

## 7.- Diagrama de Flujo (casos de uso)
- Adjunto en la carpeta

## 8.- Plan de desarrollo
- SEMANA - ACTIVIDAD
----------------------------------------------------------------------
-   1 |     Diseño del tablero y manejo entrada/salida de datos
----------------------------------------------------------------------
-   2 |     Implementación de la lógica del jugador y las reglas
----------------------------------------------------------------------
-   3 |     Implementación de la IA básica
----------------------------------------------------------------------
-   4 |     Pruebas, mejoras, refactorización
----------------------------------------------------------------------
-   5 |     Documentación y empaquetado
----------------------------------------------------------------------

## 9.- Testing
- Pruebas unitarias: 
    · Comprobación del tablero: correcta actualización de casillas
    · Verificación del ganador: detectarlo de manera precisa
    · Prueba IA: asegurarse que la IA realizar movimientos correctos
- Herramientas: PyTest

## 10.- Documentación
- README.md:
    · Instalación y configuración
    · Instrucciones para el juego (comandos/controles)
    · Descripción de la IA 
    · Descripción de las reglas del juego

- Documentación del código:
    · Funciones y clases comentadas
    · Archivos de pruebas con explicaciones claras

## 11.- Licencias y créditos
- Licencia: MIT License / Creative Commons
- Autor/es: XXX
- Colaborador/es: XXX
- Fuentes externas: Código de la IA (algoritmo público)

## INSTRUCCIONES DE USO
- Busca y ejecuta `main.py`
- Elige juego contra otro jugador o contra el PC
- Gana quién antes consiga alinear 3 símbolos