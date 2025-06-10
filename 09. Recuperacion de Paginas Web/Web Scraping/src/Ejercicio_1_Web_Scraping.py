# Raspar números de HTML usando BeautifulSoup. 
# En esta tarea, escribirá un programa de Python. 
# El programa usará urllib para leer el HTML de los archivos de datos a continuación 
# y analizar los datos, extraer números y calcular la suma de los números en el archivo.



# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen  # Para obtener datos de una URL
from bs4 import BeautifulSoup       # Para analizar el HTML y hacer web scraping
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Ingresar una URL: ')
if len(url) < 1:
    url = 'https://py4e-data.dr-chuck.net/comments_2230569.html'  # URL por defecto si no se ingresa ninguna

# Abre la URL y lee el contenido HTML
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#print(soup.prettify())

# Busca todos los elementos <span> en el HTML
tags = soup('span')

suma = 0
contador = 0

# Itera sobre cada tag <span>
for tag in tags:
    # Look at the parts of a tag
    suma += int(tag.contents[0]) # Obtiene el contenido del tag y lo convierte a entero, para sumarlo
    contador += 1

print(f'La suma de los numeros es {suma}')
print(f'El total de registros encontrados es {contador}')