# Interfaces informales
# Los interfaces informales pueden ser definidos con una simple clase que no implementa los métodos.
# Volviendo al ejemplo de nuestro interfaz mando a distancia

#Definicion de la interfaz informal
class Control:
    def siguiente_canal(self):
        pass
    def canal_anterior(self):
        pass
    def subir_volumen(self):
        pass
    def bajar_volumen(self):
        pass

#Herencia:

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


  # Como hemos dicho, esto es una solución perfectamente válida en la mayoría de los casos, 
  # pero existe un problema con el que entenderás perfectamente porqué lo llamamos 
  # interfaz informal.
  # 
  # Al heredar de la clase Control, no se obliga a ControlSamsung o ControlLG 
  # a implementar todos los métodos. 
  # Es decir, ambas clases podrían no tener código para todos los métodos, 
  # y esto es algo que puede causar problemas.
  # 
  # El razonamiento es el siguiente. Si Mando es un interfaz que como tal no implementa 
  # ningún método (tan sólo define los métodos), 
  # ¿no sería acaso importante asegurarse de que las clases que usan dicho 
  # interfaz implementan los métodos?
  # 
  # Si un método queda sin implementar, podríamos tener problemas en el futuro, 
  # ya que al llamar a dicho método no tendríamos código que ejecutar.       