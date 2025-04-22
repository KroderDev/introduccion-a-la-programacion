# Solicitar al usuario que ingrese su nota
nota = float(input("Ingrese su nota: "))
# Verificar si la nota es suficiente para aprobar
if nota >= 4.0:
    print("Aprobado")
else:
    print("Reprobado")