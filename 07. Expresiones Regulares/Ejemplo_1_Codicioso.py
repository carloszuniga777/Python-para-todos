
# Ejemplo de uso de expresiones regulares con el modificador codicioso
# ^: El simbolo ^ indica el inicio de la cadena
# .: El simbolo . indica cualquier caracter excpto un salto de linea
# +: El simbolo + indica uno o mas caracteres

#Los simbolos . y + son codiciosos por defecto, 
# lo que significa que intentan coincidir la mayor cantidad de caracteres posibles

# Por tanto, el resultado de la expresion regular da: 'From: Using the :
# Y no From:

# Porque en este caso, va a buscar hasta el segunto caracter : 
import re
x = 'From: Using the : character'
y =  re.findall('^F.+:', x)
print(y)
