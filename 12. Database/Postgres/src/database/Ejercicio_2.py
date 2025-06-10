# En este ejemplo, el sistema lee los correos electrónicos del archivo mbox-short.txt
#
# Realiza un conteo de cuántas veces aparece una organizacion en el archivo
# y la organizacion junto con su cantidad en la tabla "Counts" de la base de datos


from conexion import get_connection #Conexion.py
import re
import os

# Documentacion: https://www.psycopg.org/psycopg3/docs/basic/usage.html

try:
    # Realiza la conexion con la base de datos Postgres
    with get_connection() as conn:

        # Abre un cursor para realizar operaciones de base de datos
        with conn.cursor() as cur:
            
            # Elimina la tabla counts si existe
            cur.execute("DROP TABLE IF EXISTS Counts")

            # Crea la tabla Counts    
            cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

            # Solicita al usuario ingresar el nombre de un archivo    
            filename = input('Ingresar el nombre del archivo: ')
            if(len(filename) < 1): filename = 'mbox.txt'

            #--------- Contruir la ruta del archivo--------------- 
            
            # Obtiene la ruta del directorio actual del script
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Construye la ruta al archivo independientemente de dónde se abra el proyecto
            file_path = os.path.join(current_dir, "..", "..", "archivos", filename)                       ## Subir solo 2 niveles (.. + ..)
            file_path = os.path.abspath(file_path)

            #------------------------------------------------------

            # Abre el archivo
            with open(file_path, 'r') as file:
                
                # Itera en cada linea del archivo
                for line in file:

                    # Si linea no empieza con 'FROM' itera a la siguiente linea
                    if not line.startswith('From: '): continue

                    pieces = line.split()  # La linea la convierte en array
                    org = re.findall(r'@(.*)',pieces[1])[0]      # Obtiene la organizacion del mail 
                    
                    
                    #Pasa los datos de los email como filtro, 
                    #Usar siempre %s, esta sintaxis escapa automáticamente los valores, evitando ataques de inyección SQL. 
                    cur.execute('SELECT count FROM Counts WHERE org = %s', (org,))

                    # Recupera la siguiente fila, en este caso recupera el primer registro
                    # pero si se vuelve a ejecutar fetchone, recuperaria el segundo registro    
                    row = cur.fetchone()

                    # Si no encuentra el correo en la tabla, inserta en la tabla Counts un registro nuevo con el correo
                    # De lo contrario, solo suma al contador    
                    if row is None:
                         cur.execute('''
                                 INSERT INTO Counts(org, count)  
                                 VALUES(%s, 1)''', 
                                 (org,)
                                 )
                    else:
                         cur.execute('''UPDATE Counts 
                                            SET count = count + 1
                                        WHERE org = %s''',
                                        (org,)
                                     )  
                                        
                #Guarda los cambios
                conn.commit()


                # #Leer los datos de la tabla
                cur.execute('''SELECT org, 
                                     count 
                                FROM Counts 
                                ORDER BY count DESC''')

                for row in cur:
                    print((row[0]), row[1]) 


                # Hacer que los cambios en la base de datos sean persistentes
                conn.commit()
 
except FileNotFoundError as e:
    print(f"Error archivo no encontrado: {e}")

except Exception as e:
    print(f"Error en la operación de base de datos: {e}")
    
finally:
    print("Operación completada")