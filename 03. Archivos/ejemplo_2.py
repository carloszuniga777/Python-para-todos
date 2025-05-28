# Escribe un programa que solicite un nombre de archivo, lo abra y lo lea, buscando líneas con el formato:
#               X-DSPAM-Confidence: 0.8475
# Cuenta estas líneas, extrae los valores numéricos (decimales) de cada una 
# y calcula su promedio. Muestra el resultado como se indica a continuación. 

# No uses la función sum() ni una variable llamada sum en tu solución.

# Puedes descargar datos de ejemplo en: http://www.py4e.com/code3/mbox-short.txt. 
# Durante las pruebas, ingresa mbox-short.txt como nombre del archivo.


# 1. Nombre del archivo
filename = input("Ingrese el nombre del archivo: ")
if len(filename) < 1:
    filename = 'mbox-short.txt'

try:
    # 2. Abre el archivo
    with open("03. Archivos/" + filename, 'r') as file:
        
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
    print(f"Error: '{nameFile}' no existe en el directorio actual.")
except Exception as e:
    print(f"Error inesperado: {e}")