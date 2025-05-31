#Notas: Esta libreria no es seguro para analizar XML de fuentes no confiables.
# Para eso se recomienda usar lxml, xmltodict (Si prefieres trabajar con JSON) o defusedxml 
# que son alternativas mas seguras y robustas


#Conclusión práctica:
# ✅ Usa xml.etree.ElementTree solo si:
#   --El XML es de fuente 100% confiable (ej. generado internamente).
#   --No procesas datos de usuarios, APIs externas o sistemas desconocidos.
#
# 🚫 Nunca lo uses para:
#   --API que reciben XML arbitrario.
#   --Procesamiento de archivos subidos por usuarios.
#   --Integraciones con sistemas externos.

import xml.etree.ElementTree as ET #Para trabajar con XML

# Carga la candena XML
input ='''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Carlos</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Juan</name>
            </user>
        </users>
    </stuff>
'''

stuff = ET.fromstring(input)                       # Convierte la candena XML en un objeto ElementTree
lista_usuarios = stuff.findall('users/user')        # Encuentra todos los elementos 'user' dentro de 'users'
print('Cantidad de usuarios:', len(lista_usuarios))

for item in lista_usuarios:
    print('Name:', item.find('name').text)  # Accede al elemento 'name' dentro de 'user'
    print('Id', item.find('id').text)       # Accede al elemento 'id' dentro de 'user'
    print('Attribute', item.get('x'))       # Accede al atributo 'x' dentro de 'user'

