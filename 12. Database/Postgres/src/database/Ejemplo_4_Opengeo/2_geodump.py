# [Fase 2] En este script, lee los datos de la tabla localizaciones
# y luego los almacena en el archivo de javascript where.js

# Los datos incluyen cada ubicación con sus coordenadas,
# y servirán para mostrar estos puntos en el mapa de where.html.


import json
import codecs
import sys
import os

#---------#Importar la conexion base de datos --------------

# Calcular la ruta al directorio base (basededatos)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agregar al path de Python
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from conexion import get_connection

#------------------------------------------------------------



try:
    
    # Realiza la conexion con la base de datos Postgres
    with get_connection() as conn:
        
        # Abre un cursor para realizar operaciones de base de datos
        with conn.cursor() as cur:
            

            # Obtiene todas las direcciones de la base de datos
            cur.execute('SELECT * FROM Locations')



            #---- Obteniendo el path del archivo javascript: where.js en el directorio actual --------
            # Obtener la ruta del directorio actual del script
            script_dir = os.path.dirname(os.path.abspath(__file__))
  
            # Construir la ruta completa para la base de datos
            path = os.path.join(script_dir, 'where.js')

            #-------------------------------------------------

            # Abre el archivo where.js para escritura
            with codecs.open(path, 'w', "utf-8") as file:
                
                # Crea en el archivo where.js una variable llamada myData y abre corchetes => myData = [
                file.write("myData = [\n")

                count = 0

                # Recorre de uno en una las direcciones obtenidas de la base de datos        
                for row in cur:

                    # Obtiene la geodata en formato str
                    data = str(row[1])
                    
                    # Lo convierte a JSON, si falla itera la siguiente fila
                    try: 
                        js = json.loads(data)
                    except: continue

                    # Si no contiene nada, itera la siguiente fila
                    if len(js['features']) == 0: continue


                    # Obtiene la latitud, longitud y nombre_ubicacion        
                    try:
                        lat = js['features'][0]['geometry']['coordinates'][1]
                        lng = js['features'][0]['geometry']['coordinates'][0]
                        where = js['features'][0]['properties']['display_name']
                        where = where.replace("'", "")
                    except:
                        print('Unexpected format')
                        print(js)


                    #Escritura en el archivo js, si hay error itera la siguiente linea    
                    try :
                        #print(where, lat, lng)

                        count = count + 1
                        
                        #Si count es mayor a 1, escribe en el js un salto de linea
                        if count > 1 : file.write(",\n")

                        # Concatena la [latitud, longitud, lugar]    
                        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
                        
                        print(output)    

                        # Escribe en el archivo where.js
                        file.write(output)
                    except:
                        continue

                #Salto de linea y cierra corchetes => ]           
                file.write("\n];\n")
                
                print(count, "registros fueron escritos en where.js")
                print("Abrir where.html para ver la data in el navegador")


except FileNotFoundError as e:
    print(f"Error archivo no encontrado: {e}")

except Exception as e:
    print(f"Error en la operación de base de datos: {e}")
    
finally:
    print("Operación completada")    
