# MONGODB: Bases de datos NO relacionales

# ¿BBDD no relacionales? Quizás un problema, quizás una solución...
> NO tienen la tablas relacionadas entre sí, es decir, utilizaremos la estructura más próxima al concepto de JSON.

# Valiendo... Ahora, veamos "una" de conceptos básicos

## Características principales:
- FLEXIBLE: nos permite trabajar sin definir un esquema fijo, es decir, podemos tener documentos diferentes en los grupos del mismo tipo.
- ESCALABLE: está diseñado y parametrizado para el manejo de grandes cantidades de datos, pudiendo distribuir esa data en multitud de servidores (concepto de CDN - Content Delivery Network - https://www.hostinger.com/es/tutoriales/que-es-cdn -)
- ALTO RENDIMIENTO: gracias a su sistema de índices y diseño basado en documentos
- CONSULTAS HIPEREFICIENTES: permite la búsqueda, filtrado, agregación... Incluso operaciones geoespaciales
- INTEGRACIÓN SENCILLA: en cualquier lenguaje de programación (JAVA, Python...)

## Conceptos:

- Concepto importante 1 --> DOCUMENTO: es el equivalente a una fila SQL, pero en formato JSON
Ejemplo de JSON: {"_id":1, "nombre":"Diego", "edad": 48, "hobbies":["MTB","videojuegos", "otros"]}

- Concepto importante 2 --> COLECCIÓN: es el equivalente a una tabla SQL, es decir, un conjunto de documentos
Ejemplo colección: USUARIOS, que contiene muchos documentos del tipo anterior

- Concepto importante 3 --> BASE DE DATOS: agrupa varias colecciones

---

# Instalación de MongoDB:
1\.- Descarga para Windows: https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-8.2.1-signed.msi. También se puede instalar para otros sistemas operativos (existe un desplegable donde podemos seleccionar nuestro sistema operativo, incluso, despliegue en nube AWS y otras)

2\.- Se instala la versión COMPLETE, con la opción RUN SERVICE AS NETWORK SERVICE USER. Se ha de instalar la UI, la cual se denomina <b>MONGODB COMPASS</b>.

3\.- Para que MongoDB sea más eficiente y todo el sistema operativo "lo conozca", debemo agregar este servicio al PATH, es decir, desde cualquier sitio, se conocerá este nuevo servicio instalado.

Para ponerlo en el path, tenemos que ir a: <b>Panel de Control</b>, <b>Configuración avanzada del sistema</b>, <b>Variables de entorno</b>, donde editaremos la variable <b>Path</b>, agregando: ```C:\Program Files\MongoDB\Server\8.2\bin```

4\.- Atención: lo mejor es reiniciar cuando se hacen este tipo de instalaciones, para que el sistema coja absolutamente todo lo necesario para que MongoDB funcione a pleno rendimiento. Si no lo hacemos, es posible que algún subproceso este sin arrancar y nos perjudique en algún momento... A pesar de todo esto, Windows ya está preparado para trabajar sin reinicios, es decir, Plug&Play en los programas, con sus pros y contras.

Vamos a comprobar que la instalación está correcta, escribiendo en el CMD (modo adminsitrador): ```mongod --version```. Si todo está OK, aparecerá la información de la versión y subversión de MongoDB

# Primer contacto con MongoDB Compass:
a\.- Añadir nueva conexión con la URL: <b>mongodb://localhost:27017</b>
b\.- Al añadir un nombre <i>Tienda</b>, nos crea la conexión y 3 bases de datos que MongoDB necesita de forma interna para poder trabajar:

- <b>Admin</b>: BBDD administrativa principal de MongoDB donde:
    --> guardamos usuarios y roles con privilegios de administración
    --> guardado de usuarios con privilegios globales
    --> BBDD de ejecución y control de comandos de configuración (nivel server, es decir, creación de usuario, monitoreo de aplicaciones y usuarios, cambio de parámetros...)

EJEMPLO:
  use admin
  db.createUser({
    user:"adminUser",
    pwd:"pass12345",
    roles:"[root]"
  })

<u>SE PUEDE MODIFICAR, PERO CON CUIDADO</u>

- <b>Config</b>: configuración interna del <b>clúster</b> (replicación de datos entre los servidores) o <b>sharding</b> (distribución de datos entre nodos o servidores, es decir, un CDN). Contiene información como nombres de los servidores a los que se conecta, estado de la sincronización con estos servers, información de particionado y otras características de hardware de los servers... 

En la instalación LOCAL, podríamos ignorarla perooooooooo... Si está en un servidor al que tengo que acceder de forma remota, tengo que tenerla MUY en cuenta.

<u>SOLO LO UTILIZA MONGODB, NO SE TOCA</u>

- <b>Local</b>: contiene todos los datos específicos del servidor local donde está arrancado MongoDB. La cuestión es que:
    --> no se replica ni comparte entre servidores
    --> guarda:
        · información de réplicas
        · metadata de conexión
        · estadísticas del nodo local (servidor local)
        · y más...

<u>SOLO LO UTILIZA MONGODB, NO SE TOCA</u>

<b>HASTA AQUÍ, TODO ES UNA CONFIGURACIÓN PARECIDA AL XAMPP O SOFTWARE SIMILAR</b>


# "Cuestioncitas" de seguridad:
- Si necesitamos revisar el archivo log de MongoDB, está localizado en: ```C:\Program Files\MongoDB\Server\8.2\log```
- Si necesitamos reconfigurar el sistema, podemos hacerlo en: ```C:\Program Files\MongoDB\Server\8.2\bin```
- En la zona superior de nuestra conexión (derecha), tenemos 3 puntos (···) que nos abrirán un nuevo menú de herramientas en el que podemos ver las opciones:
    · edición, borrado, duplicación y añadir conexión a favoritos
    · desconectar
    · mostrado de información de conexión
    · visualización de métricas de rendimiento (visualización de gráficas de rendimiento)

- A la hora de abrir la URL mongodb://localhost:27017, nos aparecerá de nuevo el MongoDB Compass.

c\. Para la creación de un nueva BBDD y su correspondiente colección, hacemos clic en el botón <b>Create database</b>, acción que nos permite y obliga a crear la BBDD correspondiente y una colección asociada a esa BBDD. Así, nos aparecerá un símbolo de BBDD y una carpeta, la cual muestra que es una colección.

d\.- A la hora de añadir datos a la colección, podemos:
  - importar de un archivo JSON o CSV externo
  - añadir/insertar datos en la opción <b>insertar documentos</b>


# Tipos de datos en MongoDB
Las BBDD relacionales (MySQL, PostgreSQL,...) utilizan los formatos típicos JSON... En cambio, MongoDB utiliza un formato <i>ampliado</i> denominado <b>BSON (Binary JSON)</b>, el cual amplía los tipos de datos de JSON.
<u>TIPOS DE DATOS BÁSICOS MONGODB - BSON</u>

- String: cadena de texto (UTF-8 --> 8-bit Unicode Transformation Format, formato de codificación de caracteres Unicode e ISO 10646 que utiliza símbolos de longitud variable)
- Number (Int, Long, Double, Decimal128): números enteros/decimales. Varían según el tipo en su precisión
- Boolean: booleano (verdadero/falso)
- Date: fecha y hora (ISODate --> formato de fecha/hora basado en el estándar ISO 8601, que proporciona una representación numérica unificada y sin ambigüedades para fechas y tiempos, especialmente útil en entornos internacionales y para el intercambio de datos entre sistemas)
- Object/Document: subdocumento u objeto/estructura anidado. --> Ejemplo: "dirección": ["ciudad":"Toledo","CP":"45593"]
- Array: lista ordenada de valores
- ObjectId: Identificador único generado por MongoDB, como un UUID en las BBDD relacionales
- Null: valores nulos
- RegExp: Expresiones Regulares (preformateado para ciertos campos como CP, teléfono...)
- Binary Data: datos binarios (imágenes, archivos en general, hashes...)
- TimeStamp: marcas de tiempo internas, utilizadas para replicación de datos, logs y mucho
- JavaScript Code: código JS, muy poco comunes
- Minkey/Maxkey: valores muy especiales utilizados en las comparaciones

Como dijo Jack, <i>vamos por partes</i>:
<u>TIPOS NUMÉRICOS</u>
                      bytes                       uso                            rangos aproximados
- int32________________ 4 _______________ contadores pequeños _______________ -2147483648 a 2147483648
- int64 (long)_________ 8 _______________ contadores grandes/timestamps _____ -9e18 a 9e18
- double_______________ 8 _______________ valores decimales genéricos _______ 64-bit IEEE
- Decimal128___________ 16 ______________ precisiones exactas (128bits) _____ de alta precisión (finanzas, monedas, geo)

<u>TIPOS MENOS COMUNES</u>
                      alias                           uso                                       ejemplo
- Binary Data ________ binData ___________ almacenamiento binario archivos ____________ "archivo":BinData(0,"BASE64"...)
- Timestamp __________ timestamp _________ marca de tiempo interna (logs...) __________ "ts": Timestamp(1731128371,1)
- RegExp _____________ regex _____________ búsqueda de patrones mediante RegExp _______ "email":/@gmail\\.com$/
- JavaScript _______ javascriptWithScope _ igual RegExp, con variables adjuntas_ "val":Code("function(){return true;}")
- Symbol _____________ symbol ____________ cadena (tipo antiguo y obsoleto) ___________ "etiqueta": Symbol("v1")
- Minkey _____________ minKey ____________ valor más bajo (comparaciones) _____________ "campo":MinKey
- Maxkey _____________ maxKey ____________ valor más alto (comparaciones) _____________ "campo":MaxKey
- Undefined __________ undefined _________ valor indefinido (obsoleto) ________________ "foo":undefined

<u>TIPOS INTERNOS/DE SISTEMA</u>
Tipo Bson        Tipo de dato numérico
0 _____________________ Double
1 _____________________ String
2 _____________________ Object
3 _____________________ Array
4 _____________________ Binary Data
5 _____________________ Undefined - ya obsoleto
6 _____________________ ObjectId
7 _____________________ Boolean
8 _____________________ Date
9 _____________________ Null
10 ____________________ RegExp
11 ____________________ DBPointer - ya obsoleto
12 ____________________ JavaScript
13 ____________________ Symbol - ya obsoleto
14 ____________________ JavaScript with scope
15 ____________________ Int32
16 ____________________ Timestamp
17 ____________________ Int64
18 ____________________ Decima128
255 ___________________ MinKey
127 ___________________ MaxKey

Ejemplo completo: ver MongoDB Compass
BSON:
```{
  "_id": 1,
  "name": { "first" : "John", "last" : "Backus" },
  "contribs": [ "Fortran", "ALGOL", "Backus-Naur Form", "FP" ],
  "awards": [
    {
      "award": "W.W. McDowell Award",
      "year": 1967,
      "by": "IEEE Computer Society"
    }, {
      "award": "Draper Prize",
      "year": 1993,
      "by": "National Academy of Engineering"
    }
  ]
}``` 

