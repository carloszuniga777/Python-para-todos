# Escribe un programa que solicite al usuario las horas trabajadas y la tarifa por hora utilizando input para calcular el salario bruto. 
# Paga la tarifa normal por las primeras 40 horas y 1.5 veces la tarifa por hora para todas las horas trabajadas 
# por encima de 40. 
# 
# Usa 45 horas y una tarifa de 10.50 por hora para probar el programa (el pago debería ser 498.75). 
# Debes usar input para leer una cadena y float() para convertirla a número. 
# No te preocupes por verificar errores en la entrada del usuario: asume que el usuario ingresa números correctamente.

try:
    horas = float(input("Ingresar horas:"))
    tarifa = float(input('Ingresar tarifas'))

    if horas >= 40:
        horas_normales = 40
        horas_extra = horas - 40
        salario_bruto = (horas_normales * tarifa) + (horas_extra * tarifa * 1.5)
    else:
        salario_bruto = horas * tarifa
        
    print(salario_bruto)
except:
    print("Error: debes ingresar un numero")
