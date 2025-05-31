import urllib.request, urllib.parse, urllib.error   # Para obtener datos de una URL
from bs4 import BeautifulSoup                       # Para analizar el HTML y hacer web scraping
import ssl

# Ingnorar SSL certificados de error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Solicitar al usuario una URL a analizar
url = input('Ingrese URL: ')
if len(url) < 1:
    url = 'https://www.py4e.com/materials'  # URL por defecto si no se ingresa ninguna

html = urllib.request.urlopen(url, context=ctx).read()  # Recupera el contenido de la pagina web
soup = BeautifulSoup(html, 'html.parser')               # Crea un objeto BeautifulSoup para parsear el HTML | esta libreria permite extraer datos de archivos HTML y XML de manera sencilla 

# Extraer todos los enlaces de la pagina
tags = soup('a')
for tag in tags:
   print(f'URL buscada: {url}')
   print(tag.get('href', None))  # Imprime el atributo href de cada enlace encontrado