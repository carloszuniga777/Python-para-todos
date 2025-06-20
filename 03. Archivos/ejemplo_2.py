# Escribe un programa que solicite un nombre de archivo, lo abra y lo lea, buscando líneas con el formato:
#               X-DSPAM-Confidence: 0.8475
# Cuenta estas líneas, extrae los valores numéricos (decimales) de cada una 
# y calcula su promedio. Muestra el resultado como se indica a continuación. 

# No uses la función sum() ni una variable llamada sum en tu solución.

# Puedes descargar datos de ejemplo en: http://www.py4e.com/code3/mbox-short.txt. 
# Durante las pruebas, ingresa mbox-short.txt como nombre del archivo.

import os

# 1. Nombre del archivo
filename = input("Ingrese el nombre del archivo: ")
if len(filename) < 1:
    filename = 'mbox-short.txt'


#--------- Contruir la ruta del archivo--------------- 

# Obtiene la ruta del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construye la ruta al archivo independientemente de dónde se abra el proyecto
file_path = os.path.join(current_dir, filename)                       
file_path = os.path.abspath(file_path)

#------------------------------------------------------        

try:
    # 2. Abre el archivo
    with open(file_path, 'r') as file:
        
        total = 0.0            # Acumula los de valores 
        contador = 0           # Contador de lineas 

        #3. Itera cada linea del archivo
        for line in file:

            if not line.startswith("X-DSPAM-Confidence:"):
                continue
            
            #4. Extraer los numeros de cada linea
            word = line.split()
            numero = float(word[1])


            total += numero            
            contador += 1

        # 5. Realiza le calculo               
        if contador > 0:
            resultado = total / contador    
            print(f"Average spam confidence: {resultado}")

        #print(line)
        #print(numero)
    
except FileNotFoundError:
    print(f"Error: '{filename}' no existe en el directorio actual.")
except Exception as e:
    print(f"Error inesperado: {e}")