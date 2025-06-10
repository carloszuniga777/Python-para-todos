# Ejercicios de Conexión a PostgreSQL con Python

![Python 3.8+](https://img.shields.io/badge/Python-3.8-blue) ![PostgresSQL](https://img.shields.io/badge/PostgresSQL-gree)

Este repositorio contiene ejercicios prácticos para conectarse a bases de datos PostgreSQL desde Python. Incluye configuración de variables de entorno y manejo de conexiones.

## 📋 Prerequisitos
- Python 3.8 o superior
- PostgreSQL 12+ instalado y funcionando
- Visual Studio Code (recomendado) o cualquier editor de texto
- Extensiones VS Code recomendadas:
  - Python
  - PostgreSQL

## ⚙️ Configuración inicial

### 1. Crear entorno virtual
```bash
python -m venv .venv
```

### 2. Activar entorno virtual


`Opcion 1:`

- Abrir un ejercicio de Python (.py) en VS Code
   - Presionar `Ctrl + Shift + P` para abrir la paleta de comandos
   - Buscar y seleccionar "Python: Select Interpreter"
   - Seleccionar "Enter interpreter path"
   - Navegar a la carpeta del entorno virtual: `/Postgres/venv/Scripts/python.exe`

`Opcion 2:`

Windows (CMD/PowerShell):

```
.\venv\Scripts\activate
```

Linux/macOS:

```
source venv/bin/activate
```


### 3. Instalar dependencias
```
pip install -r requirements.txt
```
___

## 🔧 Configuración de variables de entorno

#### 1. Copiar la plantilla de variables de entorno:

```
cp env.template .env
```
#### 2. Editar el archivo .env con tus credenciales:

```
env

DB_HOST=localhost        # IP del servidor o localhost
DB_PORT=5432             # Puerto de PostgreSQL
DB_NAME=                 # Nombre de la base de datos
DB_USER=postgres         # Usuario de PostgreSQL
DB_PASSWORD=             # Contraseña del usuario
```

##### Importante:

- Nunca subas el archivo `.env` al control de versiones

- Mantén `env.template` actualizado con las variables necesarias

- El archivo `.env` debe estar en el directorio raíz del proyecto

## 🗂️ Estructura del proyecto

```
├── Postgres/          
│   ├──src/
|       ├──database/
|               | conexion.py  #Archivo de conexion a la base de datos
│               ├── Ejemplo_1.py
│               └── ...
├── .venv/                # Entorno virtual (ignorar en Git)
├── .env                  # Variables de entorno (NO SUBIR)
├── env.template          # Plantilla para variables de entorno
├── requirements.txt      # Dependencias
└── README.md             # Este archivo
```
## ▶️ Ejecutar ejercicios
- 1. Activar entorno virtual
- 2. Abrir el script en VS Code
- 3. Ejecutar con `F5` o desde terminal:

```
python ejercicios/nombre_script.py
```

 ## 📦 Dependencias principales (requirements.txt)

 ```
psycopg==3.2.9
psycopg-binary==3.2.9
psycopg-pool==3.2.6
python-dotenv==1.1.0
typing_extensions==4.14.0
tzdata==2025.2
```

## Recursos de aprendizaje


[Documentación oficial de Psycopg](https://www.psycopg.org/psycopg3/docs/) 