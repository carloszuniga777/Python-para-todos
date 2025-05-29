

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)




# import os

# # 1. Solicitar al usuario el nombrel del archivo a procesar: mbox-short.txt
# filename = input("Ingresar el nombre del archivo:")
# if len(filename) < 1:
#     filename = "mbox-short.txt"

#     # Construye la ruta dinámicamente
#     ruta_archivo = os.path.join(os.path.dirname(__file__), "06. Tuplas/", "mbox-short.txt")



# try:
#     # 2. Abrir el archivo en modo de Lectura
#     with open(ruta_archivo)  as file:

#          # 3. Leer el archivo linea por linea
#         for linea in file:
#             linea = linea.rstrip()
#             if linea.find(":") >= 0:
#                 print(linea) 
#                 print(linea.find(":") )
            
# except FileNotFoundError:
#     print(f"Error: '{filename}' no existe en el directorio actual.")
# except Exception as e:
#     print(f"Error inesperado: {e}")      