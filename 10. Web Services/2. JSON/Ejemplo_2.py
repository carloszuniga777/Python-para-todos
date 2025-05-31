import json #Libreria para trabajar con JSON

# Un string JSON que representa un objeto
data ='''[
{
  "id" : "001",
  "x" : "2",
  "name" : "Carlos"
},  
{
  "id" : "009",
  "x" : "7",
  "name" : "Rocky"
}
]'''

# Convierte el string JSON a un objeto de Python
info = json.loads(data)   # Carga el JSON en un diccionario de Python

print('User count:', len(info))

#imprime los datos
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x']) 
