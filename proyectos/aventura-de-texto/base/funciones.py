def imprimir_escenario_ascii(titulo, mensaje, opciones):
    print("=" * 40)
    print(f"== {titulo} ==")
    print("=" * 40)
    print(mensaje)
    print()
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    print()

def solicitar_opcion(opciones, memoria=None):
    while True:
        try:
            eleccion = int(input("Elige una opción: "))
            if 1 <= eleccion <= len(opciones):
                return eleccion
            else:
                print("Opción inválida. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número.")
