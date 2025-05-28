# Escribe un programa que lea el archivo mbox-short.txt 
# y determine la distribución de mensajes por hora del día. 
# 
# Para ello, extrae la hora de las líneas que comienzan con 'From ', 
# buscando el campo de tiempo y dividiendo la cadena nuevamente usando los dos puntos (:).
# 
# Ejemplo de línea:
#               From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# 
# Una vez acumulados los conteos por hora, 
# imprime los resultados ordenados por hora como se muestra abajo.


# 1. Solicitar al usuario el nombrel del archivo a procesar: mbox-short.txt
filename = input("Ingresar el nombre del archivo:")
if len(filename) < 1:
    filename = "mbox-short.txt"

try:
    # 2. Abrir el archivo en modo de Lectura
    with open(f"06. Tuplas/{filename}", 'r')  as file:

        diccionario_horas = dict()

         # 3. Leer el archivo linea por linea
        for linea in file:
            linea = linea.rstrip()
            
            # Verificar si la linea comienza con "From" y termina con "2008"
            if linea.startswith("From") and linea.endswith("2008"):
               palabras = linea.split()                                         #Obtiene una lista de palabras
               hora = palabras[5][:2]                                           # Obtiene la hora (primeros dos caracteres del campo de tiempo)                      
               diccionario_horas[hora] = diccionario_horas.get(hora, 0) + 1     # Actualiza el conteo de mensajes por hora
               

        # 4. Ordenar el diccionario por horas e imprime el resultado
        # print( sorted([ (hora, conteo) for hora, conteo in diccionario_horas.items()]))  

        for hora, cantidad in sorted(diccionario_horas.items()):
            print(f"{hora} {cantidad}")


except FileNotFoundError:
    print(f"Error: '{filename}' no existe en el directorio actual.")
except Exception as e:
    print(f"Error inesperado: {e}")  