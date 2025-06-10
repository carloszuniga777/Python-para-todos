# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen         # Para obtener datos de una URL
from bs4 import BeautifulSoup              # Para analizar el HTML y hacer web scraping 
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Solicitar al usuario una URL a analizar
url = input('Ingrese una URL: ')
if len(url) < 1:
    url = 'https://www.py4e.com/materials'  # URL por defecto si no se ingresa ninguna

# Abrir la URL y leer su contendo
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")   # Crea un objeto BeautifulSoup para analizar el HTML

# Busca todos los enlaces de la pagina
tags = soup('a')

# Imprimir detalles de cada enlace encontrado
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)