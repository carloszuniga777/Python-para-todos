# Ejemplo de uso de urllib para abrir un archivo en línea y leer su contenido
import urllib.request, urllib.parse, urllib.error   # Para obtener datos de una URL

#Se abre un archivo en línea y se lee su contenido
request = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

#imprime el contenido de la pagina web
for line in request:
    print(line.decode().strip())
