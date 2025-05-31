# Ejemplo de uso de urllib para recuperar el contenido de una pagina web
import urllib.request, urllib.parse, urllib.error    # Para obtener datos de una URL

# Recupera el contenido de una pagina web
request = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

# Reaaliza el conteo de palabras y los alamacena en un diccionario
counts = dict()
for line in request:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
