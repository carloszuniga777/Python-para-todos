# Ejercicio: Escribe un programa que:
# 1. Solicite al usuario un nombre de archivo.
# 2. Abra el archivo, lea su contenido.
# 3. Imprima el contenido del archivo en MAYÚSCULAS.

# Prueba el programa con el archivo words.txt. Puedes descargar el archivo de ejemplo aquí:
# http://www.py4e.com/code3/words.txt
#
import os


#1. Escribir el nombre del archivo, usar el nombre words.txt
filename = input("Enter file name: ")
if len(filename) < 1:
    filename = 'words.txt'

#--------- Contruir la ruta del archivo--------------- 

# Obtiene la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta al archivo independientemente de dónde se abra el proyecto
file_path = os.path.join(current_dir, filename)                       
file_path = os.path.abspath(file_path)

#------------------------------------------------------    

try:
    #2. Abriendo el archivo
    with open(file_path, 'r') as file:
        
        #3 leyendo el archivo
        for linea in file:
            text = linea.upper().rstrip()
            print(text)

except FileNotFoundError:
    print(f"Error: '{nameFile}' no existe en el directorio actual.")
except Exception as e:
    print(f"Error inesperado: {e}")
