# Ejemplo de uso de urllib para recuperar el contenido de una pagina web
import urllib.request, urllib.parse, urllib.error

# Recupera el contenido de una pagina web
request = urllib.request.urlopen("http://www.dr-chuck.com/page1.html")

for line in request:
    print(line.decode().strip())
