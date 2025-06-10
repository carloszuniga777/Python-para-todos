# [Fase 1] Este script inicial consulta la API de OpenGeo (https://py4e-data.dr-chuck.net/opengeo)
# para recuperar información geográfica de las ubicaciones almacenadas en 'where.data'

# Almacena cada ubicación junto con la respuesta completa de la API en una tabla 'localización',
# la cual incluye datos como coordenadas geográficas en formato JSON (representado como cadena de texto) y la direccion


import urllib.request, urllib.parse, urllib.error
import http
import json
import time
import ssl
import sys
import os

#---------#Importar la conexion base de datos desde el directorio donde se encuentra --------------

# Calcular la ruta al directorio base (basededatos)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agregar al path de Python
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from conexion import get_connection

#------------------------------------------------------------


# https://py4e-data.dr-chuck.net/opengeo?q=Ann+Arbor%2C+MI
api = 'https://py4e-data.dr-chuck.net/opengeo?'



# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1


try:
    # Realiza la conexion con la base de datos Postgres
    with get_connection() as conn:
        
        # Abre un cursor para realizar operaciones de base de datos
        with conn.cursor() as cur:
            
            # Crea la tabla de localizacion si no existe
            cur.execute('''
                            CREATE TABLE IF NOT EXISTS Locations (
                                address TEXT, 
                                geodata TEXT
                            )
                        ''')
            

                        
            # Ignore SSL certificate errors | ignora los certificados SSL de paginas htpps
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE



            #--------- Contruir la ruta del archivo--------------- 

            # Obtiene la ruta del directorio actual del script
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Construye la ruta al archivo independientemente de dónde se abra el proyecto
            file_path = os.path.join(current_dir, "..", "..","..", "archivos", 'where.data')                       ## Subir solo 3 niveles (.. + .. + ..)
            file_path = os.path.abspath(file_path)

            #------------------------------------------------------



            # Abre el archivo where.data que contiene todas las ubicaciones que se desean buscar
            file = open(file_path)

            count = 0
            nofound = 0

            for line in file:

                # Termina la ejecucion si hay mas de 100 ubicaciones en el archivo where.data    
                if count > 100 :
                    print('Se recuperaron 100 ubicaciones, reinicie para recuperar más')
                    break


                # obtiene la direccion a buscar desde el archivo where.data   
                address = line.strip()
                
                print('')



                #Si la dirccion ya existe en la tabla de localizaciones, itera la siguiente linea 
                cur.execute("SELECT geodata FROM Locations WHERE address= %s", (address,))                            

                try:
                    data = cur.fetchone()[0]
                    print("Found in database", address)
                    continue
                except:
                    pass

                


                # Construye el query parametro para realizar la busqueda en la API 
                # Se obtiene la url final 
                parms = dict()
                parms['q'] = address

                url = api + urllib.parse.urlencode(parms)

                print('Recuperando URL:', url)






                # Realiza la peticion a la API y obtiene los datos
                request = urllib.request.urlopen(url, context=ctx)
                data = request.read().decode()
                
                print('Recuperando', len(data), 'characters', data[:20].replace('\n', ' '))
                count = count + 1



                #Convierte a JSON los datos y en caso de error, itera la siguiente linea
                try:
                    js = json.loads(data)
                except:
                    print(data)  # We print in case unicode causes an error
                    continue


                
                #----------Validacion para saber si tiene datos reales -----------------        

                # Si features no esta en el JSON detiene la ejecucion en el programa    
                if not js or 'features' not in js:
                    print('==== Download error ===')
                    print(data)
                    break


                # Si features esta vacio, suma contador nofound     
                if len(js['features']) == 0:
                    print('==== Object not found ====')
                    nofound = nofound + 1

                # ---------------------------------------------------------------------

                #Inserta en la tabla de localizacion, la direccion a buscar y la respuesta de la API
                cur.execute('''INSERT INTO Locations (address, geodata)
                               VALUES ( %s, %s )''',
                               (address, data)) 


                #Guarda los cambios    
                conn.commit()


                #Cada 10 peticiones realiza una pausa de 5 segundos    
                if count % 10 == 0 :
                    print('Pausing for a bit...')
                    time.sleep(5)

            if nofound > 0:
                print('Número de características para las que no se pudo encontrar la ubicación:', nofound)

            print("Ejecute geodump.py para leer los datos de la base de datos para que pueda visualizarlos en un mapa.")


except FileNotFoundError as e:
    print(f"Error archivo no encontrado: {e}")

except Exception as e:
    print(f"Error en la operación de base de datos: {e}")
    
finally:
    print("Operación completada")    






