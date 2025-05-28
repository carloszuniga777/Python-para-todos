# Ejercicio: Escribe un programa que:
# 1. Solicite al usuario un nombre de archivo.
# 2. Abra el archivo, lea su contenido.
# 3. Imprima el contenido del archivo en MAYÚSCULAS.

# Prueba el programa con el archivo words.txt. Puedes descargar el archivo de ejemplo aquí:
# http://www.py4e.com/code3/words.txt
#

#1. Escribir el nombre del archivo, usar el nombre words.txt
nameFile = input("Enter file name: ")
if len(nameFile) < 1:
    nameFile = 'words.txt'

try:
    #2. Abriendo el archivo
    with open("03. Archivos/" + nameFile, 'r') as file:
        
        #3 leyendo el archivo
        for linea in file:
            text = linea.upper().rstrip()
            print(text)

except FileNotFoundError:
    print(f"Error: '{nameFile}' no existe en el directorio actual.")
except Exception as e:
    print(f"Error inesperado: {e}")
