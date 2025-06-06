#Definicion de la clase
class PartyAnimal:

    #Constructor
    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, 'constructed')

    #Metodos
    def party(self):
        self.x = self.x + 1
        print(f"{self.name}", "party count", self.x)


# Creando objeto
s = PartyAnimal("Sally")
s.party()

# Creando objeto
j = PartyAnimal("Jim")

j.party()
s.party()




