# En este ejemplo, se lee un archivo de Excel Tack.cvs que contiene una lista de canciones
# Lo que se hizo fue crear las tablas relacionadas y luego leer ese archivo para insertar 
# esa informacion en dichas tablas 

from conexion import get_connection #Conexion.py
import re
import os

# Documentacion: https://www.psycopg.org/psycopg3/docs/basic/usage.html

v_comment = ''

try:
    # Realiza la conexion con la base de datos Postgres
    with get_connection() as conn:

        # Abre un cursor para realizar operaciones de base de datos
        with conn.cursor() as cur:

            #Crea las tablas        
            cur.execute('''
                        DROP TABLE IF EXISTS Track CASCADE;
                        DROP TABLE IF EXISTS Album CASCADE;
                        DROP TABLE IF EXISTS Genre CASCADE;
                        DROP TABLE IF EXISTS Artist CASCADE;

                        CREATE TABLE Artist (
                            id  SERIAL PRIMARY KEY,
                            name    TEXT UNIQUE
                        );


                        CREATE TABLE Genre (
                            id SERIAL PRIMARY KEY,
                            name    TEXT UNIQUE
                        );

                        CREATE TABLE Album (
                            id  SERIAL PRIMARY KEY,
                            artist_id  INTEGER REFERENCES Artist(id),
                            title   TEXT UNIQUE
                        );

                        CREATE TABLE Track (
                            id  SERIAL PRIMARY KEY,
                            title TEXT,
                            album_id INTEGER REFERENCES Album(id),
                            genre_id INTEGER REFERENCES Genre(id),
                            len INTEGER, 
                            rating INTEGER, 
                            count INTEGER,
                            UNIQUE (title, album_id) 
                        );
             ''')
            

            #--------- Contruir la ruta del archivo--------------- 

            # Obtiene la ruta del directorio actual del script
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Construye la ruta al archivo independientemente de dónde se abra el proyecto
            file_path = os.path.join(current_dir, "..", "..", "archivos", 'tracks.csv')                       ## Subir solo 2 niveles (.. + ..)
            file_path = os.path.abspath(file_path)

            #------------------------------------------------------

            
            # Abre el archivo
            with open(file_path, 'r') as file:

                #Lee el archivo linea por linea    
                for line in file:

                    # obtiene la linea y crea un arreglo, 
                    # si el tamano del arreglo es menor a 6 itera la siguiente fila    
                    line = line.strip()
                    pieces = line.split(',')
                    if len(pieces) < 6 : continue

                    #obtiene el nombre, artista, album, count, rating, length    
                    name = pieces[0]
                    artist = pieces[1]
                    album = pieces[2]
                    count = pieces[3]
                    rating = pieces[4]
                    length = pieces[5]
                    genero = pieces[6]

                    print(name, artist, album, count, rating, length, genero)



                    v_comment = 'Error en insert Artist'

                    #Inserta el nombre de artista en la tabla de artista    
                    cur.execute('''
                                INSERT INTO Artist (name) 
                                VALUES ( %s )
                                ON CONFLICT (name) DO NOTHING
                                RETURNING id''', 
                                ( artist, ))
                    



                    v_comment = 'Error en artist_id'

                    #Se obtiene el id del artista    
                    if cur.rowcount == 0:
                        cur.execute(''' SELECT id FROM Artist WHERE name = %s''',  (artist, ))

                    artist_id = cur.fetchone()[0]
                       
                    
                    
                    
                    v_comment = 'Error en insert Album'          

                    #Inserta el nombre del album junto con el id del artista
                    cur.execute('''
                                INSERT INTO Album (title, artist_id) 
                                VALUES ( %s, %s )
                                ON CONFLICT (title) DO NOTHING
                                RETURNING id''', 
                                ( album, artist_id ) 
                                )
                    


                    v_comment = 'Error album_id'
                    
                    # Se obtiene el id del album
                    if cur.rowcount == 0:
                        cur.execute(''' SELECT id FROM Album WHERE title = %s''', (album, ))

                    album_id = cur.fetchone()[0]



                    cur.execute('''INSERT INTO Genre(name)
                                   VALUES( %s)
                                   ON CONFLICT (name) DO NOTHING
                                   RETURNING id  
                                ''', (genero,))
                    
                    if cur.rowcount == 0:
                        cur.execute('SELECT id FROM Genre where name = %s', (genero,))
                    
                    id_genero = cur.fetchone()[0]




                    v_comment = 'Error en insert Track'

                    # Se inserta/actualiza los atributos de la cancion junto con el id del album
                    cur.execute('''
                                INSERT INTO Track (title, album_id, genre_id, len, rating, count) 
                                VALUES ( %s, %s, %s, %s, %s, %s )
                                ON CONFLICT (title, album_id) DO UPDATE SET
                                    len = EXCLUDED.len,
                                    rating = EXCLUDED.rating,
                                    count = EXCLUDED.count''', 
                                ( name, album_id, id_genero, length, rating, count ))
                    

                #Guarda los cambios
                conn.commit()

 
except FileNotFoundError as e:
    print(f"Error archivo no encontrado: {e}")

except Exception as e:
    print(f"Error en la operación de base de datos: {e} | {v_comment}")
    
finally:
    print("Operación completada")