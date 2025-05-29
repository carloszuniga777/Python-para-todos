
# Ejemplo de uso de expresiones regulares
# ( ): Indica la parte de la cadena que se desea extraer, en este ejemplo es el correo electronico
#[^ ]: Indica que se desea extrear todo lo que no sea espacio en blanco 
# *: Indica que se desea extreer todo 0 o mas veces caracteres que no sean espacios en blanco

import re
x = 'From stephen.marquard@uct.act.za Sat Jan 5 09:14:16 2008'

#y =  re.findall('@([^ ]*)', x)
y =  re.findall('^From .*@([^ ]*)', x)

print(y)
