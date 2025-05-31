# Escribir un programa de Python 
# El programa solicitará una ubicación, 
# se pondrá en contacto con un servicio web 
# y recuperará JSON para el servicio web y analice esos datos, 
# y recupere los primeros plus_code del JSON. 
# 
# Un código de ubicación abierta es un identificador textual 
# que es otra forma de dirección basada en la ubicación de la dirección.

# El programa solicita al usuario que ingrese una ubicacion
# y el programa devolvera el plus_code de la ubicacion

import urllib.request, urllib.parse   # Para obtener datos de la API
import http, json, ssl 


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

 # URL de la API de OpenStreetMap 
 # Si se quiere usar la API real se puede usar Geopify https//www.geopify.com/ 
 # el cual tiene una capa gratuita, y se requiere estar registrado
 # Geopify se encarga de tomar los datos OpenStreetMap y convertirlos en API
serviceURL = 'https://py4e-data.dr-chuck.net/opengeo?'


while True:
    
    # Solicita al usuario una localizacion: 
    # Ingresar => Buenos Aires, Argentina
    address = input('Ingresar una localizacion: ')
    if len(address) < 1: break

    # Elimina espacios en blanco al inicio y al final de la cadena 
    address = address.strip()

    # Crea un diccionario con los parametros de la solicitud 
    parms = dict()
    parms['q'] = address

   # Se construye la URL con los parametros  
    url = serviceURL + urllib.parse.urlencode(parms)
    print('URL:', url)

    # Realiza la solicitud a la API y obtiene los datos en formato string JSON
    request = urllib.request.urlopen(url, context=ctx)
    data = request.read().decode()                      #Decodifica los datos obtenidos a un formato string
    print('Datos recibidos:', len(data), 'caracteres')

    try:
        # Convierte el string JSON a un objeto de Python`
        jsonData = json.loads(data)

        #Imprime el JSON formateado
        #print(json.dumps(jsonData, indent=4))

        # Obtiene la longitud, latitud y localizacion del JSON
        plus_code = jsonData['features'][0]['properties']['plus_code']
        print('plus_code: ', plus_code)
    
    except:
        jsonData = None

        if not jsonData or 'features' not in jsonData:
            print('Error al recuperar los datos o formato JSON incorrecto')
            continue
        
        if len(jsonData['features']) == 0:
            print('No se encontraron resultados para la localizacion:', address)
            continue

    


