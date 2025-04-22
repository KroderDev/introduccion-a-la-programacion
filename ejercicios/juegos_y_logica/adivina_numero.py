import random
numero = random.randint(1, 10)
intento = int(input("Adivina un número del 1 al 10: "))
if intento == numero:
    print("¡Adivinaste!")
else:
    print(f"No, era {numero}")