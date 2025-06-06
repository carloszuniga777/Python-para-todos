# Los interfaces formales pueden ser definidos en Python utilizando 
# el módulo por defecto llamado ABC (Abstract Base Classes). 
# Los abc fueron añadidos a Python en la PEP3119.
# 
# Simplemente definen una forma de crear interfaces (a través de metaclases) 
# en los que se definen unos métodos (pero no se implementan) 
# y donde se fuerza a las clases que usan ese interfaz a implementar los métodos. 
# 
# Veamos unos ejemplos.

from abc import abstractmethod
from abc import ABCMeta

class Control(metaclass=ABCMeta):
    @abstractmethod
    def siguiente_canal(self):
        pass

    @abstractmethod
    def canal_anterior(self):
        pass

    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass

#Herencia

# Sin embargo si que podemos heredar de Control para crear una clase ControSamsung. 
# Es muy importante que implementemos todos los métodos, o de lo contrario tendremos un error. 
# Esta es una de las diferencias con respecto a los interfaces informales

class ControlSamsung(Control):
    def siguiente_canal(self):
        print("Samsung->Siguiente")
    def canal_anterior(self):
        print("Samsung->Anterior")
    def subir_volumen(self):
        print("Samsung->Subir")
    def bajar_volumen(self):
        print("Samsung->Bajar")


class ControlLG(Control):
    def siguiente_canal(self):
        print("LG->Siguiente")
    def canal_anterior(self):
        print("LG->Anterior")
    def subir_volumen(self):
        print("LG->Subir")
    def bajar_volumen(self):
        print("LG->Bajar")

#Creando un objeto
control_lg = ControlLG()
control_lg.bajar_volumen()
