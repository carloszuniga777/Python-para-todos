# Abre el archivo mbox-short.txt y léelo línea por línea. 
# Cuando encuentres una línea que comience con 'From ' (como la siguiente):
# 
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Debes dividir la línea usando split() e imprimir la segunda palabra 
# (es decir, la dirección completa de la persona que envió el mensaje). 
# Al final, muestra la cantidad total de estas líneas.
# 
# Nota:
# Asegúrate de no incluir líneas que comiencen con 'From:' (con dos puntos).
# Observa la última línea del ejemplo para ver cómo mostrar el contador.
# 
# Puedes descargar los datos de ejemplo en: http://www.py4e.com/code3/mbox-short.txt.


# 1. Ingresa el nombre del archivo: mbox-short.txt
filename = input("Ingrese el nombre del archivo: ")
if len(filename) < 1:
    filename = "mbox-short.txt"

try:
    # 2. Abre el archivo
    with open(f"04. Listas/{filename}") as file:
        count = 0

        for linea in file:
            
            # 3. Verifica si la linea comienza con 'From:'
            if linea.startswith("From:"):

                # 4. Divide la linea en palabras y obtiene la segunda palabra    
                palabras = linea.rstrip().split()
                print(palabras[1])
                count += 1   
                

        print("There were", count, "lines in the file with From as the first word")


except FileNotFoundError:
    print(f"Error: '{filename}' no existe en el directorio actual.")
except Exception as e:
    print(f"Error inesperado: {e}")