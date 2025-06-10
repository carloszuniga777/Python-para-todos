# Ejercicios de Web Scraping con BeautifulSoup

![Python 3.8+](https://img.shields.io/badge/Python-3.8%252B-blue) ![BeautifulSoup 4.9.3](https://img.shields.io/badge/BeautifulSoup-4.9.3-green) ![Web Scraping](https://img.shields.io/badge/Web-Scraping-orange) 


Este repositorio contiene ejercicios prácticos de web scraping utilizando la biblioteca BeautifulSoup en Python. A continuación, encontrarás las instrucciones para configurar tu entorno de desarrollo.

---

## 📋 Prerequisitos

- Python 3.6 o superior instalado

- Visual Studio Code

## ⚙️ Configuración inicial

### 1. Crear un entorno virtual 
```bash
python -m venv venv
```

### 2. Activar el entorno virtual

`Opcion 1:`

- Abrir un ejercicio de Python (.py) en VS Code
   - Presionar `Ctrl + Shift + P` para abrir la paleta de comandos
   - Buscar y seleccionar "Python: Select Interpreter"
   - Seleccionar "Enter interpreter path"
   - Navegar a la carpeta del entorno virtual: `/Web Scraping/venv/Scripts/python.exe`

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
---

## 🗂️ Estructura del proyecto

```
Web Scrapiing
├── src/          # Carpeta con los ejercicios
│   ├── ejercicio1.py
│   ├── ejercicio2.py
│   └── ...
├── venv/               # Entorno virtual (se crea con python -m venv)
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo
```

### ▶️ Ejecutar ejercicios
- 1. Activa tu entorno virtual
- 2. Abrir el script en VS Code
- 3. Ejecutar con `F5` o desde terminal::

```bash
python nombre_del_script.py
```

### 📦 Dependencias principales
- beautifulsoup4

### 🔍 Archivo requirements.txt

```bash
beautifulsoup4==4.13.4
soupsieve==2.7
typing_extensions==4.14.0
```

### Recursos de aprendizaje

[Documentación oficial de BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 

### ⚠️ Notas importantes
- Verificar términos de servicio antes de hacer scraping
- Usar time.sleep() entre solicitudes
- Respetar robots.txt de los sitios
- El entorno virtual debe recrearse si se borra la carpeta /venv
