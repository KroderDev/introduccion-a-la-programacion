notas = [float(input(f"Ingrese nota {i+1}: ")) for i in range(4)]
promedio = sum(notas) / len(notas)
print(f"El promedio es: {promedio:.2f}")