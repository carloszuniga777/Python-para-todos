# Web services allow a program to access data available in a different server.

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

import xml.etree.ElementTree as ET  #Para trabajar con XML

# Carga la cadena XML
data = '''
    <person>
        <name>Carlos</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''

# Convierte la cadena XML en un objeto ElementTree
tree = ET.fromstring(data)

# Accede a los elementos del XML y los imprime
print('Name', tree.find('name').text)
print('Atrr:', tree.find('email').get('hide'))
