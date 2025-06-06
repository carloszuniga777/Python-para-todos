#Definicion de la clase
class PartyAnimal:

    #Constructor
    def __init__(self):
        self.x = 0
        print('I am constructed')

    #Metodos
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    #Destructor es opcional, solo para efectos de ver como se destruye
    def __del__(self):
        print('I am destructed', self.x)    



# Creando objeto
an = PartyAnimal()

#invocando metodos
an.party()
an.party()
an.party()

#Ciclo de vida: El objeto se se destruye
#En este ejemplo al declarar an = 42 el objeto se destruye, y crea una variable
an = 42
print('an contanis', an)



#Uso de Type and Dir:

#print("Type", type(an))      # Muestra el tipo de objeto   
#print("Dir", dir(an))        # Muestra los metodos de un objeto
#print("Type", type(an.x))
#print("Type", type(an.party))

