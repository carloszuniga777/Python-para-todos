
# En esta tarea, escribirá un programa de Python. 
# El programa solicitará una URL, leerá los datos JSON de esa URL usando urllib 
# y luego analizará y extraerá los recuentos de comentarios de los datos JSON,
#  Calcule la suma de los números en el archivo e ingrese la suma a continuación:

import urllib.request, urllib.parse   # Para obtener datos de la API
import http, json, ssl 


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api = 'https://py4e-data.dr-chuck.net/comments_2230572.json'

request = urllib.request.urlopen(api, context=ctx)
data = request.read().decode()                          #Decodifica los datos obtenidos a un formato string

try:
    # Convierte el string JSON a un objeto de Python`
    jsonData = json.loads(data)

    #Imprime el JSON formateado
    #print(json.dumps(jsonData, indent=4))

    sum = 0
    for i in jsonData['comments']:
        sum += int(i['count'])

    print('Suma de los recuentos de comentarios:', sum)

except:
    jsonData = None
    if not jsonData or 'comments' not in jsonData:
        print('Error al recuperar los datos o formato JSON incorrecto')
        exit()

    if len(jsonData['comments']) == 0:
      print('No se encontraron resultados')
      
         
