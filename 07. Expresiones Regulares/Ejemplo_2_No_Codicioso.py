
# Ejemplo de uso de expresiones regulares con el modificador no codicioso ?
# ^: El simbolo ^ indica el inicio de la cadena
# .: El simbolo . indica cualquier caracter excpto un salto de linea
# +: El simbolo + indica uno o mas caracteres
# ?: El simbolo ? indica a + y . que sean no codiciosos, es decir, 
#    que intenten coincidir con la menor cantidad de caracteres posibles

#Los simbolos . y + son codiciosos por defecto, 
# lo que significa que intentan coincidir la mayor cantidad de caracteres posibles
# Para hacerlo no codicioso, se utiliza el modificador ?

import re
x = 'From: Using the : character'
y =  re.findall('^F.+?:', x)
print(y)
