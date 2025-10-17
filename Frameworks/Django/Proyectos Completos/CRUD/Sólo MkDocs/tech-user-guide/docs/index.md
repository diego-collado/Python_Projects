# CRUD Tareas

## 🎯 <b>Resumen</b> 🎯
Esta aplicación web está desarrollada con Django 5 y tiene como objetivo ofrecer una plataforma funcional, modular y extensible para la gestión de tareas (CRUD completo), con autenticación de usuarios y un panel de control (dashboard) que muestra métricas de actividad y del sistema en tiempo real.

Su estructura sigue las buenas prácticas del framework, con separación clara entre modelo, vista y plantilla (MVT), uso de variables de entorno para configuración segura, y una interfaz moderna basada en Bootstrap 5 y Chart.js para la visualización de datos.

---

## ⚙️ Características principales ⚙️

### 🔐 <b>Autenticación & permisos</b>
- Registro de usuarios con validación por correo electrónico (integración con django-allauth).
- Inicio y cierre de sesión protegidos por token CSRF (Cross-Site Request Forgery -- Falsificación de peticiones en sitios cruzados).
- Gestión de acceso según el estado del usuario autenticado.
- Formularios adaptados con Bootstrap 5.

### 📝 <b>CRUD de tareas</b>
- Operaciones completas: crear, leer, actualizar y eliminar tareas.
- Campos como título, descripción, estado (hecha/pendiente) y fecha de creación.
- Búsqueda, ordenación y paginación avanzada con django-filter.
- Validación de datos y retroalimentación mediante mensajes flash.

### 📊 Dashboard de usuario
- Gráfico de logins por día y por hora (Chart.js).
- Distribución de tareas completadas vs. pendientes.
- KPIs con totales de tareas, logins y métricas clave.
- **Actualización dinámica de los gráficos mediante AJAX/fetch, sin recargar la página**.

### 💻 Estadísticas del sistema
- Recolección de métricas del servidor 
- Visualización de % de uso de CPU, memoria RAM, disco y memoria del proceso de Django (MB)
- **Actualización automática cada pocos segundos (5)** para visualizar el rendimiento del servidor.

### 🔧 Estructura técnica 
- Framework: **Django 5**
- Frontend: **HTML5 + CSS3 + Bootstrap 5 + Chart.js**
- ORM: **Django ORM con soporte SQLite**
- Estilo y validación: **django-crispy-forms, django-widget-tweaks**
- Filtros y paginación: **django-filter**
- Métricas del sistema: **psutil**

### 🛠️ Requisitos de sistema
- <b>FRONT-END</b><br>
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

- <b>BACK-END</b><br>
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

- <b>IMPLEMENTACIÓN APLICACIÓN</b><br>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- <b>IDEs/VERSIONADO</b><br>
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000?logo=pycharm&logoColor=fff)
![Sublime Text](https://img.shields.io/badge/Sublime%20Text-%23575757.svg?logo=sublime-text&logoColor=important)
![github](https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/compact-minimal/available/github_vector.svg)

---

## 🧱 Arquitectura 🧱
    CRUDSITE/   # carpeta raíz (/) carpeta principal de configuración del proyecto

        crudsite/   # app controladora del proyecto completo (zona de administración)
            __init__.py  # marca la carpeta donde se encuentre como un paquete de Python
            asgi.py      # ASGI (Asynchronous Server Gateway Interface), compatible con Websocket
            urls.py      # define el mapa de navegación, conecta las URLs con las vistas (views)
            wsgi.py      # configura la interfaz WSGI (Web Server Gateway Interface), ejecutando en los servidores web
            settings.py  # contiene toda la configuración de tu proyecto Django 
                            # => Qué apps están instaladas (INSTALLED_APPS)
                            # => Cómo se conecta la base de datos (DATABASES)
                            # => Dónde están las plantillas (TEMPLATES)
                            # => Idioma, zona horaria, archivos estáticos (STATIC_URL)
                            # => Seguridad y claves (SECRET_KEY, DEBUG, ALLOWED_HOSTS)


        tareas/          # app: Crud de gestión de tareas

            migrations/  # contiene los archivos de migraciones de BBDD, es decir, los cambios y backups de esos cambios
                admin.py    # registra los modelos para que aparezcan en el panel de administración de Django (/admin)
                apps.py     # contiene la configuración de la app que se está creando
                models.py   # define las tablas de BBDD (modelos): class es 1 tabla SQL y cada atributo, 1 columna
                tests.py    # sirve para escribir tests automáticos (pruebas)
                urls.py     # define las rutas específicas de la app
                views.py    # contiene las vistas, la lógica que decide qué mostrar o hacer cuando se visita una URL

        templates/       # carpeta que contiene todas las plantillas HTML (renderización de páginas)
            base.html       # plantilla principal del proyecto, que define una estructura común

            tareas/      # plantillas HTML específicas del módulo de tareas (CRUD)
                task_list.html            # muestra la lista de tareas (la vista principal)
                task_form.html            # formulario para crear o editar tareas.
                task_detail.html          # muestra los detalles de una tarea individual
                task_confirm_delete.html  # página de confirmación antes de borrar una tarea

            registration/                 # plantillas HTML relacionadas con la autenticación
                login.html                # muestra el formulario de inicio de sesión
                logged_out.html           # mostraría la pantalla de finalización (se redirecciona al login)
                signup.html               # muestra el formulario de registro de nuevos usuarios
                register.html             # muestra el formulario de registro de nuevos usuarios


            manage.py   # es el control central de Django, sirve para ejecutar comandos administrativos del proyecto
            readme.md   # archivo de documentación (en formato Markdown .md)
            db.sqlite3  # base de datos del proyecto SQLite3

        static/     # carpeta donde se guardan archivos estáticos (no cambian en el tiempo ni dependen de la BBDD)
            img/          # carpeta donde se guardan las imágenes que se utilizarán para logotipos y otras imágenes
                logo.png  # imagen del logo, a insertar en el HTML
            ...     # otras carpetas utilizadas para código JavaScript, CSS y otros tipos de archivos
--- 

## 🧭 Flujo general de uso 🧭
La aplicación sigue un flujo sencillo pero completo, que combina el ciclo de autenticación de usuarios con la gestión de datos (CRUD de tareas) y la visualización de métricas personalizadas:

### <br>🔹 <u>1. Acceso y registro de usuario</u>

Al acceder por primera vez a la aplicación, el usuario accede a la página de inicio o listado de tareas.
Si no está autenticado, se le redirige automáticamente al formulario de inicio de sesión (login), desde donde se puede:
<ul>
    <li>Iniciar sesión con un usuario ya existente</li>
    <li>Registrarse en la aplicación mediante el formulario de registro (signup)</li>
    <li>El registro se gestiona con <b>django-allauth</b>, que:
        <ul>
            <li>Crea la cuenta del nuevo usuario</li>
            <li>Envía un correo electrónico de verificación de email (dependiendo de la configuración del entorno)</li>
            <li>Impide el acceso completo al sistema hasta que el email haya sido validado</li>
            <li>Una vez confirmado el correo, el usuario puede iniciar sesión y acceder a su entorno personal</li>
        </ul>
    </li>
</ul>

### <br>🔹 <u>2. Inicio de sesión y autenticación</u>

Cuando el usuario envía el formulario de login:
<ul>
    <li>Django autentica las credenciales (usuario y contraseña)</li>
    <li>Si son correctas, se crea una sesión segura en el servidor</li>
    <li>Se genera un mensaje flash de bienvenida (ej. <i>¡Bienvenido, admin! Has iniciado sesión correctamente</i>)</li>
</ul>
El sistema registra el evento de login en la base de datos, con información del usuario y la hora exacta de conexión, lo que podría permitir posteriormente generar estadísticas de uso en el dashboard (por día y por hora).

### <br>🔹 <u>3. Acceso al CRUD de tareas</u>

Una vez autenticado, el usuario es redirigido a la vista principal de gestión de tareas, donde se podría:
<ul>
    <li>Crear una nueva tarea completando un formulario con título, descripción y estado</li>
    <li>Leer la lista de tareas existentes, filtrarlas o buscarlas por texto</li>
    <li>Editar una tarea para actualizar su estado (hecha/pendiente) o modificar los datos</li>
    <li>Eliminar tareas que ya no necesita</li>
</ul>
El CRUD está construido con las vistas genéricas de Django (<i>ListView</i>, <i>CreateView</i>, <i>UpdateView</i>, <i>DeleteView</i>), lo que simplifica la lógica del backend y mantiene el código limpio y mantenible.

En el caso de los formularios, se implementan con Bootstrap 5 (vía <b>django-crispy-forms</b>) para mejorar la presentación visual y asegurar coherencia en toda la interfaz.

Además, el sistema dispone de las siguientes mejoras:
<ul>
    <li>Se muestran mensajes flash (éxito o error) tras cada operación (por ejemplo: <i>Tarea creada correctamente</i> o <i>Tarea eliminada</i>)</li>
    <li>Se incluye paginación automática para evitar sobrecargar la página si hay muchas tareas</li>
    <li>Se aplican filtros dinámicos mediante <b>django-filter</b>, permitiendo búsquedas rápidas sin recargar toda la interfaz</li>
</ul>

### <br>🔹 <u>4. Interacción con el Dashboard</u>

En cualquier momento, el usuario puede acceder a su dashboard personal, a través del botón correspondiente en la barra de navegación, justo al lado del botón de salida. Después de la carga del dashboard, en esta vista, se muestran varios elementos de análisis y seguimiento:
<ul>
    <li>KPIs generales (indicadores clave):
    <ul>
        <li>Total de tareas registradas</li>
        <li>Número de tareas completadas</li>
        <li>Número de tareas pendientes</li>
        <li>Total de logins registrados en el sistema</li>
    </ul>
    <li>Gráficos de actividad (<b>Chart.js</b>):</i>
    <ul>
        <li>Logins por día: línea temporal que muestra el número de veces que el usuario se ha conectado en los últimos N días</li>
        <li>Logins por hora: gráfico de barras que representa los accesos recientes segmentados por hora</li>
        <li>Distribución de tareas: gráfico tipo <i>donut</i> que compara visualmente tareas completadas vs. pendientes</li>
    </ul>
</ul>
Estos gráficos se cargan de manera <b>asíncrona (AJAX)</b> mediante la <b>función fetch()</b> de JavaScript, que realiza llamadas a las <b>APIs REST</b> definidas en Django:
<ul>
    <li><b>/api/metrics/logins/daily/</b></li>
    <li><b>/api/metrics/logins/hourly/</b></li>
    <li><b>/api/metrics/tasks/summary/</b></li>
</ul>
Cada vez que el usuario cambia los filtros, el dashboard se actualiza sin necesidad de recargar la página, gracias al uso de JavaScript dinámico y <b>Chart.js</b>.

### <br>🔹 <u>5. Visualización de estadísticas</u>

En la parte inferior del dashboard, el sistema muestra información técnica del servidor obtenida en tiempo real gracias a la librería <b>psutil</b>.
Estos datos incluyen:
<ul>
    <li>Porcentaje de uso de CPU</li>
    <li>Porcentaje de memoria RAM ocupada</li>
    <li>Porcentaje de disco utilizado</li>
    <li>Memoria usada por el proceso de Django (en MB)</li>
</ul>
El sistema actualiza estas métricas automáticamente cada cada 5 segundos, haciendo peticiones AJAX al endpoint (<b>/api/metrics/system/live/</b>), lo que permite al usuario o administrador ver el rendimiento en modo LIVE del servidor, sin recargar la página.

### <br>🔹 <u>6. Cierre de sesión</u>

Cuando el usuario decide salir de la aplicación, pulsa el botón <i>Salir</i> en la barra de navegación. El el cierre de sesión se realiza mediante un <b>formulario POST</b> (protegido contra ataques de tipo <b>CSRF</b>), cumpliendo con las nuevas políticas de seguridad de Django 5 (que ya no se permite logout por método <b>GET</b>). Así, tras cerrar sesión:
<ul>
    <li>Se destruye la sesión activa</li>
    <li>Se muestra un mensaje flash informativo: <i>Has cerrado sesión. ¡Hasta pronto!</i></li>
    <li>El usuario es redirigido a la página de inicio o login</li>
</ul>

### <br>🔹 <u>7. Comportamiento general y UX</u>

Toda la interfaz mantiene un diseño limpio (adaptado con <b>Bootstrap 5</b>), además de incluir el sistema de mensajes disponible en Django, el cual muestra mensajes de feedback visual (alertas, badges, etc.) para informar al usuario de cada acción o problema, como en el caso de los errores de validación, los cuales se gestionan desde los formularios de Django, evitando inconsistencias o accesos indebidos por error, garantizando la seguridad de las rutas, de modo que:
<ul>
    <li>Las vistas del CRUD y dashboard solo son accesibles a usuarios autenticados</li>
    <li>Los endpoints API de métricas están protegidos con LoginRequiredMixin</li>
</ul>

--- 

## 📝 <b>Documentación oficial</b> 📝
<div style="text-align:center; margin-top:1rem;">
    <a href="https://docs.djangoproject.com/es/5.2/" target="_blank" class="btn btn-info" rel="noopener noreferrer">🐍 Django 5.2</a>
    <a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/" target="_blank" class="btn btn-info" rel="noopener noreferrer">🚀 Bootstrap 5.3</a>
    <a href="https://www.chartjs.org/docs/latest/" target="_blank" rel="noopener noreferrer" class="btn btn-info">📊 Chart.js</a>
</div>

--- 

## ✅ <b>Badges</b>
![Badge en Desarollo](https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green)
[![Visitas a nuestro Github](https://hits.sh/github.com/diego-collado/Python_Projects.svg?style=flat-square&label=Visitas%20Github)](https://hits.sh/github.com/diego-collado/Python_Projects/)