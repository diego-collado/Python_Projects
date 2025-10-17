# Desarrollando el CRUD: Guía paso a paso

## 💬 <b>Desarrollo APP</b> 💬

### 🏁 Resumen del proceso desarrollo
<u>1\.- Creación del entorno de desarrollo</u>
- Configuración de entorno virtual.
- Instalación de Django y dependencias iniciales.

<u>2\.- Inicialización del proyecto</u>
- Generación del proyecto base con <b>django-admin startproject</b>.
- Configuración de settings.py (base de datos, apps, plantillas, estáticos, variables de entorno).

<u>3\.- Creación de las aplicaciones</u>
- Generación de una app con <b>python manage.py startapp</b>.
- Registro de la app en <b>INSTALLED_APPS</b>.
- Definición de modelos (<b>models.py</b>) y migraciones (<b>makemigrations</b> y <b>migrate</b>).

<u>4\.- Configuración de rutas (<b>URLs</b>)</u>
- Definición de URLs globales (<b>project/urls.py</b>).
- Creación de urls.py dentro de cada app para modularidad.

<u>5\.-  Desarrollo de vistas y lógica de negocio</u>
- Implementación de <b>vistas basadas en clases (CBV)</b> o <b>funciones (FBV)</b>.
- Gestión de datos mediante el <b>ORM</b> de Django.

<u>6\.- Creación de plantillas (<b>templates</b>)</u>
- Uso del sistema de plantillas Django.
- Inclusión de HTML, Bootstrap y bloques reutilizables (<b>base.html</b>).
- Incorporación de formularios con <b>django-crispy-forms</b>.

<u>7\.- Gestión de archivos estáticos y medios</u>
- Configuración de <b>STATICFILES_DIRS</b>, <b>STATIC_ROOT</b>, <b>MEDIA_URL</b> y <b>MEDIA_ROOT</b>.

<u>8\.- Autenticación y permisos</u>
- Implementación de login, logout y registro de usuarios.
- Integración de django-allauth para verificación por email.
- Restricción de acceso mediante <b>LoginRequiredMixin</b> y decoradores.

<u>9\.- Dashboard y estadísticas (si aplica)</u>

- Creación de panel de control con <b>Chart.js</b>.
- Implementación de <b>endpoints</b> JSON para métricas (login, tareas, sistema).

<u>10\.- Mensajes y notificaciones</u>
- Uso del sistema de mensajes de <b>Django (messages)</b>.
- Alertas de éxito, error o advertencia en la interfaz.

<u>11\.- Testing y verificación funcional</u>
- Pruebas unitarias y de integración con <b>pytest</b> o <b>manage.py test</b>.

<u>12\.- Despliegue y mantenimiento</u>
- Configuración de entorno de producción (<b>DEBUG=False</b>).
- Variables de entorno con <b>django-environ</b>.
- Servidor <b>WSGI (Gunicorn)</b> o <b>ASGI (Uvicorn)</b> y base de datos en producción.

--- 

### 💼 Proyecto + estructura

1\.- Para la creación del proyecto, ejecutamos en la terminal: <p align="center">```django-admin startproject crudsite```</p>

2\.- Para la creación del proyecto, ejecutamos en la terminal: <p align="center">```python manage.py startapp tareas```</p>

3\.- La estructura del proyecto, se quedará tal y como hemos visto en la sección <b>[arquitectura](#-arquitectura-)</b>.

4\.- Para la configuración, se edita el archivo crudsite/settings.py:
<ul>
    <li>añadimos la app nuestra al path de todo el proyecto</li>
    <li>cambiamos hora, idioma, carpeta de plantillas...</li>
    <li><b>cambiar en producción la SECRET KEY para evitar hackeos</b></li>
</ul>

5\.- Se crea la carpeta <b>TEMPLATES/</b>, donde estarán contenidas tanto el archivo <b>base.html</b> (donde se renderiza todo el contenido) y el resto de los archivos visuales (en formato HTML).

6\.- Creamos el modelo de tarea (denominado <b>TASK</b>), con todos los <i>campos</i> que se van a utilizar en la futura vista de usuario.

7\.- Es el momento idóneo para crear el primer versionado, para lo cual ejecutaremos el siguiente código en terminal: <p align="center">```python manage.py makemigrations```</p>

Este primer comando analiza tus modelos (<b>models.py</b>) y crea archivos de migración en la carpeta <b>MIGRATIONS/</b>, denominado <i>0001_initial.py</i>. 

Cada archivo describe qué debe cambiar en la base de datos (crear una tabla nueva, agregar un campo, eliminar o modificar un campo, cambiar relaciones, etc.), es decir, no cambia la base de datos todavía, solo crea el plan de cambios.

Posteriormente, se toman las migraciones creadas con <i>makemigrations</i> y se aplican realmente en la base de datos ejecutando el comando en la terminal:<p align="center">```python manage.py migrate```</p>

8\.- Se añadirán ciertas líneas al archivo <b>tareas/admin.py</b>. Las opciones implementadas no son obligatorias, per sí muy recomendables ya que cuando creas un modelo (por ejemplo <i>Tarea en models.py</i>), Django no lo muestra automáticamente en el admin panel (<b>/admin</b>), por lo que debemos registrarlo en <b>admin.py</b>.

9\.- Después de implementar el código, tenemos que crear un usuario superadministrador para poder gestionar todo Django ejecutando en la terminal el comando: <p align="center">```python manage.py createsuperuser```</p>

Para este ejemplo, los datos de acceso son: 

- Usuario  ----> <b>profe</b>
- Password --> <b>@Aula42025</b>

10\.- Ahora es el momento de hacer la magia utilizando el siguiente comando en la terminal:<p align="center">```python manage.py runserver```</p>

---

### 📂 Creación de rutas
11\.- Se deberán crear las rutas del proyecto y app en el archivo <b>crudsite/urls.py</b>, donde se implementan las urls de todas las funcionalidades y <i>partes</i> del CRUD.
Debemos tener en cuenta:

- <i>path(''...)</i> define la ruta URL determinada como una cadena vacía (<b>'  '</b>), lo que nos dice que estamos en la raíz de la app (<b>/</b>).
- <i>views.TaskListView.as_view()</i> convierte la URL en <b>CBV (Class-Based View)</b>
- <i>as_view()</i> convierte la clase en una función para que Django la pueda manejar a la hora de trabajar con la petición HTTP
- <i>(name='lista')</i> muestra el listado de elementos, es decir, trabaja como un alias de la ruta
- <i>int:pk</i> es un convertidor de ruta para Django, o lo que es lo mismo, la ruta espera un número entero, el cual se pasa como argumento gracias al parámetro <b>PK (Primary Key)</b> que tendremos en nuestra vista.

Se debe tener muy en cuenta que cada uno de los registros que estamos visualizando en la lista, se implementa en la base de datos como registro en una tabla, por lo que necesitamos la <b>PK</b> para poder trabajar de forma correcta, eficiente y sin errores.

12\.- Ahora, creamos un nuevo archivo <b>urls.py</b> para nuestra aplicación, el cual va a tener disponible la lista de urls que se podrán ejecutar según cada petición recibida, de modo que cada vista es manejada según la url que recibe como parámetro. En un momento dado, cada url se convierte en una clase basada en vistas, las cuales Django puede utilizar directamente.

12+1\.- Crearemos el archivo <b>tareas/forms.py</b>, el cual contendrá el formulario (campos) que se verá en las propias vistas de la app. Se crea a partir de una clase formulario propia de Django y (como vimos antes), aplicaremos una configuración (tipo de campo, longitud...), o lo que es lo mismo, tendremos disponible un <b>MODELO</b>.

14\.- Ahora implementamos las vistas, donde realmente definimos qué vista irá a qué funcionalidad (crear, listar...), es decir, trabajamos directamente con las <b>CBV</b>.

15\.- Momento de recodificar las <b>templates</b>, o lo que es lo mismo, crear un archivo HTML (de toda la vida) donde inyectaremos el código necesario para que se plasmen correctamente los datos. El primer archivo que tenemos que implementar es <b>templates/base.html</b>. Además, se va a utilizar <b>BootStrap vía CDN</b> para la creación rápida de estilos.

16\.- Se crea la carpeta <b>TAREAS/</b> dentro de <b>TEMPLATES/</b>, el cual estarán contenidas las plantillas de HTML de cada aplicación. Si tenemos 4 aplicaciones, habrá 4 carpetas diferentes, cada una de ellas con las plantillas que se necesiten para poder ver todo el contenido de la BBDD que tenemos disponible con Django.

17\.- Implementamos el archivo <b>task_list.html</b>, una plantilla para el listado de tareas, la cual está dentro de la carpeta <b>TAREAS/</b> de <b>TEMPLATES/</b>.

18\.- Después del archivo anterior, crearemos <b>task_detail.html</b>, <b>task_confirm_delete.html</b> y <b>task_form.html</b> para parametrizar lo mínimo de nuestro CRUD.

### 📌 Autenticación & permisos

19\.- En este caso, se necesita que cada usuario sólo vea y gestione sus propias tareas, por lo que se realizarán las siguientes acciones:
<ul>
    <li>Añadir un campo owner al modelo</li>
    <li>Obligar al usuario a iniciar sesión para acceder al CRUD</li>
    <li>Restringir la edición y borrado de propietarios (owners en la zona de administración)</li>
</ul>

20\.- Creamos un modelo de propietario (el famoso <b>owner</b>) en nuestro archivo <b>tareas/models.py</b>.

21\.- Ahora debemos realizar la migración con <i>cuidaito</i>... Si <u><b>NO</b></u> tenemos datos, la migración se hace directamente... En caso contrario, debemos hacer una migración temporal mediante un <b>usuario administrador</b>, es decir, debemos disponer de un usuario por defecto.

Al no tener datos, la migración la realizamos implementando en al terminal los comandos: <p align="center">```python manage.py makemigrations```&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```python manage.py migrate```</p>

Si se produce el error que hemos comentado, podemos añadir <b>null=True</b> en nuestro código para que momentaneamente, permitamos la creación y manejo de campos nulos en la BBDD para hacer la backup, lo que permitirá que se creen las migraciones sin tener que asignar valores a los datos ya existentes.

22\.- Añadiremos las urls de autenticación a Django en nuestro archivo <b>urls.py</b>.

23\.- Se retocan las views añadiendo:
<ul>
    <li>Carga de bibliotecas de Django para gestión de usuarios y mensajes de error</li>
    <li>Creación de una vista por owner</li>
    <li>Creación de filtrado y ordenación de la lista de tareas, controlando que estén correctas y que pertenezcan al usuario que tiene abierta la sesión</li>
    <li>Creación de una nueva paginación automática, de forma que tendremos disponible un control de errores de paginación, evitando algún que otro problema de inyección</li>
    <li>Control de errores si asignamos el número de página directamente en la URL <i>/articulos/?page_size=33</i>, la cual no existe, devuelve 10 (por defecto, 10 elementos por página)</li>
</ul>

Cada usuario tiene un información determinada, es decir, tiene una información personalizada al contexto, la cual se enviará la HTML, donde se incluye el nombre del modelo, la página actual (paginación) y los filtros o formularios que este usuario tiene disponibles. 

Se debe tener muy en cuenta que los <b>args</b> en Python se utiliza para una función que viene implementado por un número variable de parámetros: <p align="center">```def funcion(*args)```</p>

En el caso de <b>kwags</b>, realmente es una convención, podemos implementar <i>**daigualqueponer</i>, lo que nos permite dar un nombre a cada argumento de entrada, pudiendo acceder a ellos dentro de la función a través de un diccionario (<b>clave</b>: <b>valor</b>): <p align="center">```def funcion(**kwargs)```</p>

En la función que nos va a crear el contexto, tenemos <i>params = self.request.GET.copy()</i>, que realmente crea una copia de la URL <i>/articulos/?q=django&page=2&order=asc</i>, la cual contendra:<p align="center">```{'q':'django','page':2,'order':'asc'}```</p>
    
Al resto de las clases que tenemos en <b>views.py</b>, las tenemos que añadir <b>LoginRequiredMixin</b> y <b>OwnerQuerysetMixin</b>, para hacerlas dependientes de la autenticación. 

En la clase <b>TaskCreateView</b>, la hacemos dependiente la creación de nuevas tareas siempre y cuando tengamos permiso para ello, es decir, que obligamos al usuario a que esté logueado y, además, que tenga privilegios para poder crear tareas. En el caso del <b>update</b> y el <b>delete</b>, tenemos que hacerlo dependiente del usuario.

Creamos el <b>objeto OwnerRequiredMixin</b>, para gestionar todo lo relativo a testeo, o lo que es lo mismo, si el usurio no está logueado o lo hace de forma incorrecta, le lanzamos un error <b>403 (Forbidden)</b>.

24\.- Creamos un <b>login</b>, el cual deberá estar en la ruta <b>templates/registration/login.html</b>.

25\.- Imnplentamos el <b>logout</b>, en la misma ruta anterior

26\.- Insertamos el control de mensajes para que la aplicación nos pueda informar acerca de errores o cualquier información importante. Para ello, actualizamos con el código conveniente el archivo <b>templates/base.html</b>, si bien deberíamos tener en cuenta que el <b>middleware</b> está cargado ya en <b>crudsite/settings.py</b>.

27\.- Ahora, nos ponemos manos a la obra con los filtros, la ordenación y la paginación avanzada, para lo cual se añaden los controles en la plantilla y se mejora la paginación, programando estos controles en el archivo <b>templates/tareas/task_list.html</b>.

28\.- En el archivo <b>crudsite/settings.py</b>, debemos añadir las redirección tras el <b>login/logout</b> para la mejora y eficiencia de la UX.

<p align="center">⚠️<b>IMPORTANTE</b>⚠️</p>
<p align="center"><b>SE HAN INCLUÍDO LÍNEAS PARA REGISTRO DE NUEVOS USUARIOS Y TODO LO RELATIVO A LA VISUALIZACIÓN CON EL FRAMEWORK DE CSS BOOTSTRAP</b></p>

## 🧮 Implementación dashboard 🧮

29\.- Se realiza la autenticación (login/logout) con <b>django.contrib.auth</b> para lo cual se añaden las rutas estándar de auth bajo la URL <b>/accounts/</b>, habilitando las URLs <b>/accounts/login/</b>, <b>/accounts/logout/</b>, <b>/accounts/password_change/</b> y otras.

Es evidente que se tendrán que ajustar ciertos parámetros en el archivo <b>settings.py</b>:<p align="center">```LOGIN_URL = "/accounts/login/"```</p>&nbsp;&nbsp;&nbsp;&nbsp;<p align="center">```LOGIN_REDIRECT_URL = "/"```</p>&nbsp;&nbsp;&nbsp;&nbsp;<p align="center">```LOGOUT_REDIRECT_URL = "/accounts/login/"```</p>

Respecto a las plantillas, se crean (o reutilizan) <b>templates/registration/login.html</b> y <b>templates/registration/logged_out.html</b>, incluyendo <b>{% csrf_token %}</b> en <b>login.html</b> para evitar ataques tipo CSRF.

30\.- Se reimplementa el campo <b>owner</b> en el modelo para que cada usuario vea solo sus tareas asignando de forma automática al propietario en <b>CreateView</b> y aislando consultas. En cualquier vista que liste u obtenga tareas, se filtra por <b>owner=self.request.user</b>.

31\.- Se procede a asignar permisos en vistas (propietario) y <b>LoginRequiredMixin</b> mediante los <b>mixins</b>  reutilizables de Django, aplicándolo a todas las vistas genéricas (<b>TaskListView</b>, <b>TaskDetailView</b>, <b>TaskCreateView</b>, <b>TaskUpdateView</b>, <b>TaskDeleteView</b>). 

Para <b>FBVs (function-based views)</b>, se usa el decorador <b>@login_required</b> y se filtra con <b>get_object_or_404(Task, pk=..., owner=request.user)</b> de forma más efectiva, evitando fallos y errores de carga.

32\.- Se activan los mensajes flash en <b>create</b>/<b>update</b>/<b>delete</b> y render en <b>base.html</b>. En este archivo <b>base.html</b> se inserta un bloque único que funcione con cualquier framework CSS (```class="alert alert-{{ message.tags|default:'info' }} mb-2" role="alert"```).

Al no saber cuántos mensajes vamos a tener que mostrar, se utiliza la estructura repetitiva for con la siguiente sintaxis: ```{% for message in messages %}```.

33\.- Se crean los filtros por estado, búsqueda y tamaño de página configurable. Además, se utiliza una <b>whitelist</b> para la ordenación segura, lo que nos ayudará a evitar ataques de <b>inyección SQL</b>:
    ```ALLOWED_ORDER = {"created": "created_at","-created": "-created_at","title": "title","-title": "-title","status": "status","-status": "-status",}``` 

Se realiza la construcción del queryset en la lista para las búsquedas y se prepara la barra superior (nav) para insertar el desplegable con los filtros en la plantilla que estamos utilizando, para lo cual se opta por utilizar un select común donde ```{% if request.GET.order == "created" %}selected{% endif %}``` nos permitirá recoger la selección que reliza el usuario en el momento de seleccionar el desplegable.

34\.- Creamos la característica avanzada de paginación con conservación de parámetros y contador, donde acaberemos <i>mostrando X–Y de Z</i>, es decir, se utiliza un tag utilitario para preservar parámetros en enlaces de paginación similar a ```page_obj.start_index / end_index dan el rango X–Y```.

Se utiliza el <b>tag</b> ```url_replace``` conserva <b>q</b>, <b>status</b>, <b>order</b>, <b>page_size</b>, etc., al cambiar de página. Además, con <b>get_paginate_by()</b> permite un tamaño de página configurable con límites sanos.

Al utilizar el código ```{% load querystring %}```, muy utilizado en las plantillas para importar un módulo de etiquetas personalizadas antes de poder usarlas (teniendo en cuenta que pertenece al sistema de etiquetas y filtros personalizados de Django, llamadas <b>template tags</b>), para poder usar dentro del HTML la etiqueta personalizada ```url_replace```.

35\.- La instrucción ```{% load form_extras %}```, al igual que ```{% load querystring %}```, se utiliza para importar un módulo de etiquetas y filtros personalizados dentro del sistema de plantillas de Django. 

En este caso, el archivo <b>form_extras.py</b> define un filtro llamado ```add_class```, registrado con ```@register.filter```, que permite agregar clases CSS a los campos de un formulario directamente desde la plantilla. 

Esta técnica ofrece una forma profesional y reutilizable de mejorar la presentación de los formularios, manteniendo la lógica de estilizado separada del código Python y promoviendo una arquitectura limpia, flexible y coherente con la estructura de trabajo de Django, orientada a la personalización del renderizado de formularios.

## 🏗️ Arranque y primer test

#### Creación de entorno virtual

- <b>Linux</b>: <p align="center">```python -m venv .venv```</p>&nbsp;&nbsp;&nbsp;&nbsp;<p align="center">```source .venv/bin/activate```</p>
- <b>Windows</b>: <p align="center">```.venv\Scripts\activate```</p>

#### En la terminal

- Instalación de librearías requeridas: <p align="center">```pip install -r requirements.txt```</p>
- Migración: <p align="center">```python manage.py migrate```</p>
- Arranque del servidor Django: <p align="center">```python manage.py runserver```</p>

#### Resultado visual
En la barra superior se tiene disponible:

- Si no hay sesión abierta, los botones <b>Entrar</b> y <b>Registrarse</b>
- Si el usuario ya está logeado, el texto <i>Hola, <u>username</u><i> y botón <b>Salir</b>
- Al iniciar sesión aparecerá un mensaje: <i>¡Bienvenido, admin! Has iniciado sesión correctamente.</i>
- Al cerrar sesión, aparecerá un mensaje: <i> Has cerrado sesión. ¡Hasta pronto!</i>

--- 

## Link de Interés
### 👉 <b>Badges</b> 
<div style="text-align:center; margin-top:1rem;">
    <a href="https://github.com/alexandresanlim/Badges4-README.md-Profile" target="_blank" rel="noopener noreferrer" class="btn btn-info">🔎 Generales</a>
    <a href="https://intergrav.github.io/devins-badges-docs/badges/" target="_blank" rel="noopener noreferrer" class="btn btn-info">💡 Profesionales</a>
    <a href="https://github.com/alexandresanlim/Badges4-README.md-Profile?tab=readme-ov-file#-dynamic" target="_blank" class="btn btn-info" rel="noopener noreferrer">🔥 Dinámicos</a>
    <a href="https://github.com/hehuapei/visitor-badge" target="_blank" class="btn btn-info" rel="noopener noreferrer">📊 Estadísticos</a>
    <a href="https://shields.io/badges" target="_blank" rel="noopener noreferrer" class="btn btn-info">💾 Desarrollo</a>
    <a href="https://www.chartjs.org/docs/latest/" target="_blank" rel="noopener noreferrer" class="btn btn-info">🚀 Awesome Badges</a><br><br>
</div>

### 💪 <b>MkDocs</b>
<div style="text-align:center; margin-top:1rem;">
    <a href="https://github.com/mkdocs/catalog" target="_blank" class="btn btn-info" rel="noopener noreferrer">📚 Catálogo MarkDown (themes...) </a>
    <a href="https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes" target="_blank" class="btn btn-info" rel="noopener noreferrer">🖥️ MkDocs Third Party Themes</a><br><br>
    <a href="https://markdown.es/" target="_blank" class="btn btn-info" rel="noopener noreferrer">	📑 Información MarkDown</a>
    <a href="https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax" target="_blank" class="btn btn-info" rel="noopener noreferrer">🖱️ Formato MD: toda la info (GitHub)</a>       
</div>

--- 
## ✅ <b>Badges</b>
![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)
[![Visitas a nuestro Github](https://hits.sh/github.com/diego-collado/Python_Projects.svg?style=flat-square&label=Visitas%20Github)](https://hits.sh/github.com/diego-collado/Python_Projects/)
