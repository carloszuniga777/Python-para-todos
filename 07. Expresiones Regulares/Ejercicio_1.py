import re
import os

# Construye la ruta dinámicamente

ruta_archivo = os.path.join(os.path.dirname(__file__),  "regex_sum_2230567.txt")

try:
    with open(ruta_archivo, 'r')  as file:
        # Busca todos los numeros en el archivo y los suma
        print( sum([ float(numeros) for numeros in re.findall('[0-9]+', file.read())  ]) )

except FileNotFoundError:
    print(f"Error: '{ruta_archivo}' no existe en el directorio actual.")
except Exception as e:
    print(f"Error inesperado: {e}")  


