'''
-----> Django: ¿un monstruo en nuestra casa? -------------------------------------------------------------------->
    · es un FRAMEWORK: un entorno de trabajo, el cual tiene su propio lenguaje
    · como un buen framework, tiene un montón de componentes "precocinados/pre-built" (ejemplo: https://getbootstrap.com/docs/5.3/examples/)
    · se adapta a cualquier proyecto o aplicación
    · permite la construcción de aplicaciones de forma SEGURA
    · es GRATIS y de CÓDIGO ABIERTO
    · tiene una gran comunidad de ayuda: https://www.djangoproject.com/community/

-----> ¿Y si tengo varios proyectos, cómo independizo? ---------------------------------------------------------->
Para estar en la implementación de varios proyectos, lo mejor de lo mejor, es utilizar ENTORNOS VIRTUALES:
    · son "zonas" aisladas, las cuales trabajan de forma independiente al resto
    · es lo más parecido (en programación) a las VMs (Virtual Machines - Máquinas Virtuales)
    · pagas por recurso: CPU, memoria RAM, HDD/SSD, versión de un sistema operativo...
    · posibilita el poder instalar LO QUE QUERAMOS REALMENTE, de forma independiente al ANFITRIÓN
    (ordenador que lleva todo el peso de los entornos virtuales)
    · así, evitamos conflictos/problemas en:
        -- uso de bibliotecas               -- utilizar X versión de Python o cualquier otro lenguaje 
        -- instalación de subprogramas      -- despliegue de aplicaciones sin interrumpir el uso normal del anfitrión

        EV1 = [Python 2.1 + Numpy]      EV2 = [Python 8.3.5 + Keras]    EV3 = [Python 3.10.12 + SciFi]
                     |                                  |                               |
                     -------------------------------------------------------------------- 
                                                        |
                                                ENTORNOS VIRTUALES
                                                    SEPARADOS
                                        podemos utilizar pip sin problema...
                                        podemos utilizar cualquier orden....

Para todo este "carajal", utilizamos los VENV que tiene disponibles Python, lo que nos permite:
    · gestionar las dependencias de un proyecto sin interferir en el resto de los proyectos que estén en este sistema
    · cargamos X módulos en una zona determinada de mi sistema
    · realizamos pruebas y test sin comprometer el resto de la máquina

-----> Juan Palomo: Yo me lo guiso y me monto un virtual -------------------------------------------------------->
Pasos a seguir para "comandear" en nuestro Windows:
    FASE A: el cómo construimos un VENV - - - - - - - - - - - - - - -
    1.- abrimos CMD en modo administrador: buscamos SÍMBOLO DE SISTEMA y hacemos clic sobre la opción EJECUTAR COMO ADMINISTRADOR
    2.- aparecemos en la carpeta C:\Windows\system32, la "natural" de Windows cuando eres administrador
    3.- accedemos a la carpeta donde queramos "instalar" el entorno virtual
    4.- creamos una carpeta (modo visual) y accedemos mediante el CMD: cd C:\Users\A4-Profesor\Downloads\Django
    5.- ¡ya estamos en la carpeta! escribimos dir para ver qué contenido tenemos en la carpeta en cuestión
    6.- al crear un entorno virtual, se instalan ciertas "cositas" que necesita ese entorno... ¡¡vamos que nos crea
    una maldita carpeta dentro de nuestros proyectos!
    7.- introduzco el siguiente código para crear un VENV: python -m venv nombre_que_me_venga_en_gana_sobre_el_proyecto
    python -m venv ejemplo_basico
    8.- ¡¡Ostras, me ha creado una carpeta!! Ale, pues me meto en ella: cd ejemplo_basico
    9.- al escribir dir, veremos que hay un montón de carpetas que el VENV necesita para poder trabajar
    
    FASE B: el cómo arrancamos un VENV - - - - - - - - - - - - - - -
    10.- nos tenemos que meter dentro de la carpeta Scripts de nuestro nuevo entorno: cd Scripts
    11.- esta carpeta está creada por VENV... ¡¡Ahora vamos a activar el entorno por fin!!
    12.- lo activamos mediante el código: activate (ejecutado dentro de la carpeta)
    13.- ya tenemos el CMD activado en modo VENV... el prompt nos aparece así: (ejemplo_basico) C:\Users\A4-Profesor\Downloads\Django\ejemplo_basico\Scripts>

    14 y +.- Para desactivarlo, codificamos: deactivate

    FASE C: jugando con VENV en Visual Studio Code - - - - - - - -
    15.- en el buscador superior, escribimos: > create y seleccionamos aquel en el que aperezca Crear ambiente...
    16.- seleccionamos la opción Venv, para que el área actual de trabajo sea VENV
    17.- tenemos que elegir la carpeta donde se guardarán todos y cada uno de los archivos que vamos a utilizar
    18.- una vez seleccionada la carpeta, se reinicia VSC y aparece todo en nuestro explorador de VSC
    19.- con > interpreter podemos seleccionar la versión de nuestro intérprete de Python...

    FASE D: evitando marrones de última hora - - - - - - - - - - -
    20.- se podría instalar en terminal el gestor de paquetes PIP
    21.- se instala codificando: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    22.- instalamos como tal: python get-pip.py
    23.- deberíamos activar el VENV en VSC perooooo, nos da problemas con PowerShell...
    24.- Ale, a solucionar codificando:
        --> Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
    25.- Lo mejor, ante todo, es probar python -m venv Proyecto para comenzar a trabajar

-----> Instalando Django: desencadenado!! ----------------------------------------------------------------------->
1º. Para instalar este framework: pip install django
A veces sucede que el sistema nos avisa de actualización de PIP (gestor de paquetes). Para ello, codificamos:
     python.exe -m pip install --upgrade pip
2º. Para verificar la instalación de Django:
    import django
    print(django.get_version())

SIEMPRE TENEMOS QUE TENER A MANO LA SIGUIENTE AYUDA:
    - https://www.djangoproject.com/
    - https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django
    - https://github.com/django/django
'''
import django

print(django.get_version())