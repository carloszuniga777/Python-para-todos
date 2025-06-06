
#Clase generica Animal, que generaliza las características y funcionalidades que todo animal puede tener
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)


#---Clase especializada que heredan de 'animal' ---

# 1. Clase 'Perro' hereda de 'Animal'
class Perro(Animal):

    #Metodo heredado pero con nueva implementacion
    def hablar(self):
        print("Guau!")

     #Metodo heredado pero con nueva implementacion
    def moverse(self):
        print("Caminando con 4 patas")



# 2. Clase 'Vaca' hereda de 'Animal'
class Vaca(Animal):
    #Metodo heredado pero con nueva implementacion    
    def hablar(self):
        print("Muuu!")

    #Metodo heredado pero con nueva implementacion    
    def moverse(self):
        print("Caminando con 4 patas")



# 3. Clase 'Abeja' hereda de 'Animal'
class Abeja(Animal):
     #Metodo heredado pero con nueva implementacion    
    def hablar(self):
        print("Bzzzz!")

     #Metodo heredado pero con nueva implementacion        
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")


# Creando objetos
mi_perro = Perro('mamífero', 10)
mi_vaca = Vaca('mamífero', 23)
mi_abeja = Abeja('insecto', 1)

mi_perro.hablar()     # Guau!
mi_vaca.hablar()      # Muuu!
mi_vaca.describeme()  # Soy un Animal del tipo Vaca
mi_abeja.describeme() # Soy un Animal del tipo Abeja 
mi_abeja.picar()      # Picar!