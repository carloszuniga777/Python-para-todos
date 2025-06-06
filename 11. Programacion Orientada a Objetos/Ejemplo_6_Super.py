# La función super() nos permite acceder a los métodos de la clase padre desde una de sus hijas.

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad        
    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)


# Tal vez queramos que nuestro 'Perro' tenga un parámetro extra en el constructor, 
# como podría ser el dueño. Para realizar esto tenemos dos alternativas:
# 
# 1. Podemos crear un nuevo __init__ y guardar todas las variables una a una.
# 2. O podemos usar super() para llamar al __init__ de la clase padre que ya aceptaba la especie 
# y edad, y sólo asignar la variable nueva manualmente.

class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        # Alternativa 1
        # self.especie = especie
        # self.edad = edad
        # self.dueño = dueño

        # Alternativa 2 (Recomendada)
        super().__init__(especie, edad)   
        self.dueño = dueño


# Creando objeto

mi_perro = Perro('mamífero', 7, 'Luis')
print(mi_perro.especie)
print(mi_perro.edad)
print(mi_perro.dueño)