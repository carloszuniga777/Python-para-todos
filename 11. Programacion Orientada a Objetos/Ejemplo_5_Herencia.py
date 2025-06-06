#Creacion de clase generica
class PartyAnimal:

    def __init__(self,nam):
        self.x = 0
        self.name = nam
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


#Creacion de clase que hereda de PartyAnimal
class FootballFan(PartyAnimal):

    def __init__(self, nam):
        super().__init__(nam)  #Se inicializa el contructor de la clase padre para poder setear 'nam'
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()                                #Invanco clase heredada
        print(self.name, "points", self.points)


#Invando objetos:

s = PartyAnimal("Sally")
s.party()


j = FootballFan("Jim")
j.party()
j.touchdown()