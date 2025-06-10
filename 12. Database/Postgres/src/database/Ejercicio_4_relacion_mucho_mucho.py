
# En este ejemplo, se procesa un archivo JSON (roster_data.json) que contiene
# una lista de asociaciones entre usuarios y cursos. 
# 
# Para modelar esta relación, se crearon las tablas correspondientes utilizando 
# una tabla de unión llamada Member, que gestiona la relación muchos a muchos 
# entre usuarios y cursos.
#  
# Finalmente, se lee el archivo y se inserta la información en las tablas mencionadas.
#
# Por ultimo se realiza un cruce de las tablas y se obtiene el numero hexadecimal 
# del primer registro: XYZZY416172746869736933303130



from conexion import get_connection #Conexion.py
import json
import os

# Documentacion: https://www.psycopg.org/psycopg3/docs/basic/usage.html

v_comment = ''

try:
    # Realiza la conexion con la base de datos Postgres
    with get_connection() as conn:

        # Abre un cursor para realizar operaciones de base de datos
        with conn.cursor() as cur:

            # Crea las tablas        
            cur.execute('''
                        
                        DROP TABLE IF EXISTS Member CASCADE;
                        DROP TABLE IF EXISTS "User" CASCADE;
                        DROP TABLE IF EXISTS Course CASCADE;

                        
                        CREATE TABLE "User" (
                            id     SERIAL PRIMARY KEY,
                            name   TEXT UNIQUE
                        );

                        CREATE TABLE Course (
                            id     SERIAL PRIMARY KEY,
                            title  TEXT UNIQUE
                        );

                        CREATE TABLE Member (
                            user_id     INTEGER REFERENCES "User"(id),
                            course_id   INTEGER REFERENCES Course(id),
                            role        INTEGER,
                            PRIMARY KEY (user_id, course_id)
                        )
             ''')
            
            # Solicita al usuario que ingrese el nombre del archivo                       
            filename = input('Enter file name: ')
            if len(filename) < 1:
                filename = 'roster_data.json'


            #--------- Contruir la ruta del archivo--------------- 
            
            # Obtiene la ruta del directorio actual del script
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Construye la ruta al archivo independientemente de dónde se abra el proyecto
            file_path = os.path.join(current_dir, "..", "..", "archivos", filename)                       ## Subir solo 2 niveles (.. + ..)
            file_path = os.path.abspath(file_path)

            #------------------------------------------------------    

            # Abre el archivo json y obtiene un string            
            str_data = open(file_path).read()

            # Convierte el string a un objeto json de python    
            json_data = json.loads(str_data)   

            # Itera linea a linea del json
            for entry in json_data:

                # Obtiene el nombre, el titulo del curso y el rol
                name = entry[0]  
                title = entry[1]
                rol = entry[2]

                #print((name, title, rol))

                # Inserta el nombre en la tabla User
                cur.execute('''INSERT INTO "User" (name)
                               VALUES ( %s )
                               ON CONFLICT (name) DO NOTHING
                               RETURNING id 
                            ''', ( name, ))
                
                # Obtiene el id del usuario
                if cur.rowcount == 0:
                    cur.execute('SELECT id FROM "User" WHERE name = %s ', (name, ))

                user_id = cur.fetchone()[0]




                # Inserta el titulo del curso en la tabla Course 
                cur.execute(''' INSERT INTO Course (title)
                                VALUES ( %s )
                                ON CONFLICT(title) DO NOTHING   
                                RETURNING id
                            ''', ( title, ) )
                
                # Obtiene el id del curso
                if cur.rowcount == 0:
                    cur.execute('SELECT id FROM Course WHERE title = %s ', (title, ))

                course_id = cur.fetchone()[0]





                # Inserta el id del curso y el id del usuario en la tabla UNION (MUCHOS A MUCHOS) llamada Member
                cur.execute('''INSERT INTO Member (user_id, course_id, role) 
                               VALUES ( %s, %s, %s )
                               ON CONFLICT (user_id, course_id) DO UPDATE
                                SET
                                    role = EXCLUDED.role
                            ''', ( user_id, course_id, rol ) )
                

            
            #Imprime el numero hexadecimal del primer registro: "XYZZY416172746869736933303130"
            cur.execute(''' 
                            SELECT 'XYZZY' || upper(encode(convert_to("User".name || Course.title || Member.role, 'UTF8'), 'hex')) AS X
                            FROM "User" 
                            JOIN Member 
                                ON "User".id = Member.user_id
                            JOIN Course 
                                ON Member.course_id = Course.id
                                ORDER BY x LIMIT 1
                        ''')
            
            
            print(cur.fetchone())

            conn.commit()


except FileNotFoundError as e:
    print(f"Error archivo no encontrado: {e}")

except Exception as e:
    print(f"Error en la operación de base de datos: {e} | {v_comment}")
    
finally:
    print("Operación completada")