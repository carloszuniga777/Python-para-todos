
# Ejemplo de uso de expresiones regulares 
# ^: El simbolo ^ indica el inicio de la cadena
# ( ): Indica la parte de la cadena que se desea extraer, en este ejemplo es el correo electronico
# \S: indica cualquier caracter que no sea un espacio en blanco
# +: indica uno o mas caracteres que no sean espacios en blanco

import re
x = 'From stephen.marquard@uct.act.za Sat Jan 5 09:14:16 2008'
y =  re.findall(r'^From (\S+@\S+)', x)
print(y)
