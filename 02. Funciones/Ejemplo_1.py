# Escribe un programa que solicite al usuario las horas trabajadas 
# y la tarifa por hora usando input para calcular el salario bruto. 
# El pago debe ser la tarifa normal por las primeras 40 horas 
# y 1.5 veces la tarifa por hora para todas las horas extras trabajadas por encima de 40.

# Coloca la lógica de cálculo del pago en una función llamada computepay() 
# y usa esta función para realizar el cálculo. La función debe retornar el valor del cálculo.
#
# Prueba el programa con:
# 45 horas
# Tarifa de 10.50 por hora (El resultado debe ser 498.75)

#Instrucciones adicionales:
# 
# Usa input para leer los valores como cadenas y float() para convertirlos a números.
# No es necesario verificar errores en la entrada del usuario (asume que ingresarán números válidos).
# No uses la variable sum ni la función sum() en tu código.


def computepay(horas, tarifa):
    
    if horas > 40:
        horas_normales = 40
        horas_extra = horas - 40
        salario_bruto = (horas_normales * tarifa) + (horas_extra * tarifa * 1.5)
    else:
        salario_bruto = horas * tarifa    
    return salario_bruto


horas = int(input("Ingrese las Horas:"))
tarifa = float(input('Ingrese la tarifa'))

p = computepay(horas, tarifa)
print("Pay", p)