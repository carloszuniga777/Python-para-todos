# Web services allow a program to access data available in a different server.

import json #Libreria para trabajar con JSON

# Un string JSON que representa un objeto
data ='''
{
  "name" : "Carlos",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
  }  
}
'''

# Convierte el string JSON a un objeto de Python
info = json.loads(data)   # Carga el JSON en un diccionario de Python

# Imprime los datos
print("Name:", info["name"])
print("Hide", info["email"]["hide"])