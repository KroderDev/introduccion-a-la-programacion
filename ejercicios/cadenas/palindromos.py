entrada = input("Ingrese una palabra o frase: ")
# Eliminar espacios y convertir a minúsculas
texto_limpio = ''.join(entrada.split()).lower()
# Verificar si es un palíndromo
if texto_limpio == texto_limpio[::-1]:
    print("Es un palíndromo: Sí")
else:
    print("Es un palíndromo: No")