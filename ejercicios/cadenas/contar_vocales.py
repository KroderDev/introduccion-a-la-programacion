texto = input("Ingrese una frase: ").lower()
vocales = "aeiou"
conteo = sum(texto.count(v) for v in vocales)
print(f"Cantidad de vocales: {conteo}")