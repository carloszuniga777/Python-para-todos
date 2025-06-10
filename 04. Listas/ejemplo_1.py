# Abre el archivo romeo.txt y léelo línea por línea. 
# Para cada línea, divide la línea en una lista de palabras usando el método split(). 
# El programa debe construir una lista de palabras. 
# 
# Para cada palabra en cada línea, verifica si ya está en la lista y, si no, agrégala.
#  Al finalizar, ordena la lista (con el método sort() de Python)
#  e imprime las palabras en orden alfabético, como se muestra en el ejemplo.
# 
# 
# Puedes descargar los datos de ejemplo en: http://www.py4e.com/code3/romeo.txt.

import os

#. 1. Ingresa el nombre del archivo: romeo.txt'
filename = input("Ingrese nombre del archivo: ")

if len(filename) < 1:
    filename = 'romeo.txt'


#--------- Contruir la ruta del archivo--------------- 

# Obtiene la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta al archivo independientemente de dónde se abra el proyecto
file_path = os.path.join(current_dir, filename)                       
file_path = os.path.abspath(file_path)

#------------------------------------------------------        

try:

    #2. Abre el archivo
    with open(file_path, 'r') as file:
        
        lista_palabras = list()      #Lista

        #3. Lee el archivo    
        for linea in file:

            #4. Obtiene un array de palabras por cada linea    
            palabras = linea.rstrip().split()

            #5. Itera el arreglo y si encuentra una palabra que no existe en la lista la guarda  
            for palabra in palabras:
                if palabra not in lista_palabras:
                    lista_palabras.append(palabra)

        lista_palabras.sort()
        print(lista_palabras)


except FileNotFoundError:
    print(f"Error: '{filename}' no existe en el directorio actual.")
except Exception as e:
    print(f"Error inesperado: {e}")