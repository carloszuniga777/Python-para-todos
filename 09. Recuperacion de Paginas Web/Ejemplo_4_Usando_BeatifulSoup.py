
# Ejemplo 4: Usando BeautifulSoup para extraer enlaces de una pagina web
# Web Scraping usando BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Ingrese URL: ')
if len(url) < 1:
    url = 'http://www.dr-chuck.com/page1.html'  # URL por defecto si no se ingresa ninguna

html = urllib.request.urlopen(url).read()  # Recupera el contenido de la pagina web
soup = BeautifulSoup(html, 'html.parser')  # Crea un objeto BeautifulSoup para parsear el HTML | esta libreria permite extraer datos de archivos HTML y XML de manera sencilla 

# Extraer todos los enlaces de la pagina
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))  # Imprime el atributo href de cada enlace encontrado
