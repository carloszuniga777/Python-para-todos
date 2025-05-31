# Ejemplo de uso de urllib para recuperar el contenido de una pagina web
import urllib.request, urllib.parse, urllib.error    # Para obtener datos de una URL

# Recupera el contenido de una pagina web
request = urllib.request.urlopen("http://www.dr-chuck.com/page1.html")

#imprime el contenido de la pagina web
for line in request:
    print(line.decode().strip())
