import math
# Solicitar un número al usuario
numero = float(input("Ingrese un número: "))
# Verificar si el número es no negativo
if numero >= 0:
    raiz_cuadrada = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")
else:
    print("El número ingresado no tiene raíz cuadrada real.")