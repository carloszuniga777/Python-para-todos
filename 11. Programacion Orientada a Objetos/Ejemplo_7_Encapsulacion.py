# A continuación veremos el decorador @property, que viene por defecto con Python, 
# y puede ser usado para modificar un método para que sea un atributo o propiedad.

#Tal vez te preguntes para que sirve esto, ya que el siguiente código hace exactamente 
# lo mismo sin hacer uso de decoradores.
# 
# Bien, la explicación no es sencilla, pero está relacionada con el concepto de encapsulación 
# de la programación orientada a objetos. 
#
#  Este concepto nos indica que en determinadas ocasiones es importante ocultar el estado interno
#  de los objetos al exterior, para evitar que sean modificados de manera incorrecta.
# 
#  Para la gente que venga del mundo de Java, esto no será nada nuevo, 
#  y está muy relacionado con los métodos set()y get() que veremos a continuación.
# 
# La primera diferencia que vemos entre los códigos anteriores 
# es el uso de __ antes de mi_atributo. Cuando nombramos una variable de esta manera, 
# es una forma de decirle a Python que queremos que se “oculte” 
# y que no pueda ser accedida como el resto de atributos.


#Definicion de una clase
class Perro:

    # Atributo de clase
    especie = 'mamífero'

    #Contructor
    def __init__(self, nombre, raza):
        # Atributo de instancia
        self.__nombre = nombre
        self.__raza = raza

    # Metodos
    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")

    #-----------Definicion de Getter------------- 
    @property
    def mi_nombre(self):
        return self.__nombre 
        
    @property
    def mi_raza(self):
        return self.__raza
    
    #------------Definicion de Setter-------------
    @mi_nombre.setter
    def mi_nombre(self, nombre):
        if nombre != '':
            print("Modificando el nombre")
            self.__nombre = nombre    
        else:    
            print('Error esta vacio')

        

    @mi_raza.setter
    def mi_raza(self, raza):
        if raza != '':
            print("Modificando la raza")
            self.__raza = raza    
        else:    
            print('Error esta vacio')

    



# Como si de un atributo normal se tratase, podemos acceder a el con el objeto . y nombre.

mi_perro = Perro('Firulais', 'Doberman')
print(f'Mi nombre es {mi_perro.mi_nombre} y mi raza es {mi_perro.mi_raza}')

# print(mi_perro.__nombre)  #Error, el atributo esta oculto

mi_perro.mi_nombre = 'Ingeniero Trochez'
mi_perro.mi_raza = 'Bulldog'

print(f'Mi nombre es {mi_perro.mi_nombre} y mi raza es {mi_perro.mi_raza}')
