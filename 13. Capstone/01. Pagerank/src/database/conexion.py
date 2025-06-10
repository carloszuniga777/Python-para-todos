# ORM para PostgresSQL en Python
import psycopg
from psycopg import OperationalError

#variables de entorno
import os
from dotenv import load_dotenv


#Se invoca las variables de entorno para que sean leidas
load_dotenv()


def get_connection():

    try:
        conn = psycopg.connect(
            host = os.getenv("DB_HOST"),            # Cambia si tu DB está en otro servidor
            dbname = os.getenv("DB_NAME"),          # Nombre de la base de datos    
            user = os.getenv("DB_USER"),            # Usuario    
            password = os.getenv("DB_PASSWORD"),    # Agrega tu contraseña si es necesaria
            port = os.getenv("DB_PORT")             # Puerto por defecto de PostgreSQL
        )
        print("✅ Conexión exitosa a PostgreSQL")

        return conn
    
    except OperationalError  as e:
        print(f"❌ Error de conexión: {e}")
        raise  # Relanza la excepción para manejo externo
    except Exception as e:
        print('Error no identificado database:', e)
        raise       

