# Ahorro Programado
# ¿Quién hizo esto?
Juan Esteban Marín Villegas
Tomás Mercado Ramos

# ¿Quien hizo la interfaz gráfica?

* Juan José Becerra Bedoya
* Simon Correa Bravo

# ¿Qué es y para qué es?
El proposito de este proyecto es ayudarle a las persona a calcular de una manera más fácil y práctica el monto que van ahorrar con el ahorro programado

# ¿Cómo lo hago funcionar?
Prerrequisitos: 

Antes de correr el proyecto debes tener el conocimiento de la couta que se va dar mensual, el interés que se va aplicar y el numero de cuotas que se darán.

Ejecución:
Ubicados en la carpeta raiz del proyecto, ejecute:

py src\view\console.py

Ejecucion de interfaz grafica: 

python3 -m src.view.kivy_ahorro_programado

donde se corre como modulo para que funcione de manera correcta sus importaciones

# ¿Cómo está hecho?
La organización de los módulos es la siguiente:

En la carpeta src tenemos otras sub carpetas que son controller, model y view. Model contiene dos archivos, el obligatorio que es _init.py y app.py que es donde está toda la lógica del proyecto. Controller solo contiene el archivo obligatorio __init_.py. Y view tiene un archivo que se llama console.py que contiene todo el código para tener interacción con el usuario por medio de la consola.

En la carpeta tests hay dos archivos casos de pruebas.xlsx y Tests.py. Casos de pruebas.xlsx es un excel con todos los casos de pruebs que nos fueron solicitados. Y Tests.py tiene todas las pruebas unitarias con sabe en esos casos de prueba.

# Estructura sugerida
Carpeta src: Codigo fuente de la logica de la aplicación. Tiene subcarpetas por cada capa de la aplicacion
Carpeta tests: Pruebas Unitarias

# Uso
Para ejecutar las pruebas unitarias, desde la carpeta raiz, use el comando

py tests\Tests.py 

Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

import sys sys.path.append("src")

BASES DE DATOS

Prerrequisitos
Tener Python 3.8+ instalado.

Instalar el paquete psycopg2 para conectarse a PostgreSQL:

pip install psycopg2
Tener acceso a una base de datos PostgreSQL, con:

Nombre de la base de datos

Usuario y contraseña

Puerto y host

Configuración del Proyecto
Clonar o copiar este proyecto en tu máquina.

Ir a la carpeta src/config/ y copiar el archivo de muestra:

cp SecretConfig-sample.py SecretConfig.py

Editar SecretConfig.py y completar con los datos de tu base de datos:

python
Copiar
Editar
# src/config/SecretConfig.py

DB_CONFIG = {
    "host": "localhost",
    "dbname": "ahorro_db",
    "user": "tu_usuario",
    "password": "tu_contraseña",
    "port": 5432
}
 Configuración de la Base de Datos
Este proyecto requiere que esté creada una tabla llamada savings, donde se almacenarán los ahorros programados.

Antes de ejecutar la aplicación o las pruebas unitarias, debes crear las tablas necesarias.

Usa el siguiente comando para ejecutar el script de creación:

bash
Copiar
Editar
python src/test/crear_tablas.py
Este comando ejecutará el archivo sql/crear-savings.sql, que crea la siguiente tabla:

sql
Copiar
Editar
CREATE TABLE IF NOT EXISTS savings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    amount DECIMAL NOT NULL,
    interest DECIMAL NOT NULL,
    period DECIMAL NOT NULL,
    total DECIMAL NOT NULL
);
🧪 Pruebas Unitarias Iniciales
Para asegurar que las tablas se hayan creado correctamente y la base de datos funcione, puedes correr:

bash
Copiar
Editar
python src/test/crear_tablas.py
Esto sirve como prueba inicial y fixture para la base de datos.

🚀 Ejecución de la Aplicación
Una vez creada la base de datos, puedes ejecutar la aplicación desde consola con:

bash
Copiar
Editar
python src/view/console.py
Verás un menú con las opciones:

Crear ahorro programado

Modificar ahorro programado

Buscar ahorro programado

Salir

 Estructura del Proyecto
bash
Copiar
Editar
ahorro-programado-mvc/
│
├── src/
│   ├── view/                
│   │   └── console.py
│   ├── controller/          
│   │   └── saving_controller.py
│   ├── model/               
│   │   └── app.py
│   ├── config/              
│   │   ├── SecretConfig.py
│   │   └── SecretConfig-sample.py
│   └── test/                
│       └── crear_tablas.py
│
├── sql/
│   ├── crear-savings.sql    #
│   └── ...otros archivos...
│
└── README.md (esto mismo)