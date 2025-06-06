
#Definicion de una clase
class Perro:

    # Atributo de clase
    especie = 'mamífero'

    #Contructor
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")
        
        # Atributo de instancia
        self.nombre = nombre
        self.raza = raza

    # Metodos
    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")
        
    # Por lo tanto el uso de los métodos estáticos pueden resultar útil para indicar 
    # que un método no modificará el estado de la instancia ni de la clase. 
    #   
    # En otras palabras, los métodos estáticos se podrían ver como funciones normales, 
    # con la salvedad de que van ligadas a una clase concreta.  
    @staticmethod
    def metodoestatico(a, b):
        return f"Método estático: {a+b}"


#Creacion de un objeto
miPerro = Perro("Tooby", "Bulldog")
print(type(miPerro))

#Imprimiendo atributos
print(miPerro.nombre)   # Toby
print(miPerro.raza)     # Bulldog
print(miPerro.especie)  # mamífero

#Invocando metodos
miPerro.ladra()
miPerro.camina(10)

print(miPerro.metodoestatico(1,2))