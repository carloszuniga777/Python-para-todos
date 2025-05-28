# Escribe un programa que lea el archivo mbox-short.txt 
# y determine quién ha enviado la mayor cantidad de mensajes de correo. 
# 
# El programa debe buscar líneas que comiencen con 'From ', 
# tomar la segunda palabra de esas líneas (la dirección del remitente) 
# y crear un diccionario de Python que asocie cada dirección de correo 
# con el número de veces que aparece. Una vez construido el diccionario,
#  el programa debe usar un bucle de máximo para encontrar al remitente con más mensajes.
# 
# Puedes descargar el archivo de ejemplo en: http://www.py4e.com/code3/mbox-short.txt.


# 1. Solicitar al usuario el nombrel del archivo a procesar: mbox-short.txt
filename = input("Ingresar el nombre del archivo:")
if len(filename) < 1:
    filename = "mbox-short.txt"

try:
    # 2. Abrir el archivo en modo de Lectura
    with open(f"05. Diccionarios/{filename}", 'r')  as file:

        diccionario_correo = dict()  # Diccionario para almacenar correos y sus conteos

        # 3. Leer el archivo linea por linea
        for linea in file:
            
            #4. Procesar las lineas que comiencen con "From:"
            if linea.startswith("From:"):

                # 5. Crear un lista de palabras por cada linea
                palabras = linea.split()
 
                if(len(palabras) > 1):
                    correo = palabras[1]                                                    #Tomar el correo del remitente
                    diccionario_correo[correo] = diccionario_correo.get(correo, 0) + 1      # Almacenar en diccionario y aumentar el conteo

        # 6. Encontrar el remitente con mas mensajes
        maximo = None
        for key, value in diccionario_correo.items():
            if maximo is None or value > maximo[1]:
                maximo = (key, value)
        
        print(f"El remitente con mas mensajes es: {maximo[0]} con {maximo[1]} mensajes.")
        #print(f"{maximo[0]} {maximo[1]}")


except FileNotFoundError:
    print(f"Error: '{filename}' no existe en el directorio actual.")
except Exception as e:
    print(f"Error inesperado: {e}")  