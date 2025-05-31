import urllib.request                # Para obtner datos de una URL   
import xml.etree.ElementTree as ET   # Para trabajar con XML

# Solicitar al usuario una URL para procesar
url = input('Ingresar una URL: ')
if len(url) < 1 : 
    url = 'https://py4e-data.dr-chuck.net/comments_2230571.xml'

print('URL:', url)

# Abrir la URL y leer los datos
uh = urllib.request.urlopen(url)
data = uh.read()
print('Recuperando:', len(data),'characters')

# Parsear los datos a XML
tree = ET.fromstring(data)

# Buscar todos los elmeentos <count> del XML
counts = tree.findall('.//count')   #  Punto inicial: indica que se busca desde el nodo raiz, 
                                    # '//': indica que busca en todos los nodos hijos
                                    # count: es el nombre del elemento XML que se desea encontrar

nums = list()

# Itera sobre los elementos <count> encontrados y extrae el texto y los covierte a enteros
# para agregarlos a la lista
for result in counts:
    # Debug print the data :)
    # print(result.text)
    nums.append(int(result.text)) #Convertir el texto a entero y agregarlo a la lista

print('Count:', len(nums))
print('Sum:', sum(nums))
