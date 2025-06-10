# En esta tarea, escribirá un programa de Python.
# El programa usará urllib para leer el HTML de los archivos de datos a continuación, 
# Extraiga el href= vaues de las etiquetas de anclaje, busque una etiqueta 
# que esté en una posición particular en relación con el primer nombre en la lista, 
# Siga ese enlace y repita el proceso varias veces y reporta el apellido que encuentres.

#Problema real: Comience en: http://py4e-data.dr-chuck.net/known_by_Neema.html
# Encuentre el enlace en la posición 18 (el primer nombre es 1). Siga ese enlace. Repite este proceso 7 veces. El La respuesta es el apellido que recuperas.
# Sugerencia: El primer carácter del nombre de la última página que vas a cargar es: D

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen    # Para obtener datos de una URL
from bs4 import BeautifulSoup         # Para analizar el HTML y hacer web scraping
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Ingresar una URL: ')
if len(url) < 1:
    url = 'https://py4e-data.dr-chuck.net/known_by_Neema.html'  # URL por defecto si no se ingresa ninguna

i = 0

while i < 7:

    # Abre la URL y lee el contenido HTML
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")       # Crea un objeto BeautifulSou para analizar el HTML, este objeto permite navegar por el HTML de manera sencilla

    #print(soup.prettify())

    # Busca todos los elementos <span> en el HTML
    tags = soup('a')

    posicion = 1

    # Itera sobre cada tag <span> y extrae el url de href en la posicion 18
    # esta url es la que se usara para la siguiente iteracion
    # y asi sucesivamente hasta llegar a la iteracion 7
    for tag in tags:
        
        if posicion == 18:
            url = tag.get('href', None)
            print(url)

        posicion += 1
    
    
    i+=1

# extrae el nombre del url de la ultima iteracion, usando expresiones regulares
nombre = re.findall('known_by_(.*).html', url)

print(f'El nombre encontrado es: {nombre[0]}')
