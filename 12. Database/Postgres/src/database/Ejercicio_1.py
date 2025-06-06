# Este ejercicio, crea una tabla llamada Ages 
# y se inserta los datos dados previamente en el ejercicio
# Luego, busca el hexadecimal del primer registro: 4A61656C796E3338


from conexion import get_connection #Conexion.py


# Documentacion: https://www.psycopg.org/psycopg3/docs/basic/usage.html

try:
    # Realiza la conexion con la base de datos Postgres
    with get_connection() as conn:

        # Abre un cursor para realizar operaciones de base de datos
        with conn.cursor() as cur:
            
            # Elimina la tabla counts si existe
            cur.execute("DROP TABLE IF EXISTS Ages")

            # Crea la tabla     
            cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

            # Inserta todos estos registros
            cur.executemany('''
                INSERT INTO Ages (name, age) 
                VALUES (%s, %s)''',
                [
                    ('Jasveer', 38),    
                    ('Keegan', 22),
                    ('Rhia', 14),
                    ('Morvyn', 23),
                    ('Jaelyn', 38),
                    ('Reece', 39),
                ] 
            )

            # Guarda cambios
            conn.commit()


            #Imprime el numero hexadecimal del primer registro: 4A61656C796E3338
            cur.execute('''
                SELECT upper(encode(convert_to(name || age::text, 'UTF8'), 'hex')) AS X 
                FROM Ages 
                ORDER BY X'''
            )

            print(cur.fetchone())
            
            # Hacer que los cambios en la base de datos sean persistentes
            conn.commit()
 
except FileNotFoundError as e:
    print(f"Error archivo no encontrado: {e}")

except Exception as e:
    print(f"Error en la operación de base de datos: {e}")
    
finally:
    print("Operación completada")