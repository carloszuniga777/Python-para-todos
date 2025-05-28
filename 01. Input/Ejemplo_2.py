# Escribe un programa que solicite al usuario las horas trabajadas y la tarifa por hora utilizando input
# para calcular el salario bruto.
# Utiliza 35 horas y una tarifa de 2.75 por hora para probar el programa (el resultado debe ser 96.25).
# Debes usar input para leer una cadena y float() para convertirla en un número.
# No te preocupes por validar errores o datos incorrectos del usuario.

try:
    horas = float(input("Ingrese las horas trabajadas:"))
    tarifa = float(input("Ingrese la tarifa por hora:"))
    salarioBruto = horas * tarifa
    print("Pay:", salarioBruto)
except:
    print("Error: debes ingresar un numero")
