from funciones import imprimir_escenario_ascii, solicitar_opcion

def main():
    titulo = "Inicio de la Aventura"
    mensaje = "Te despiertas en un bosque misterioso. ¿Qué harás?"
    opciones = ["Explorar el bosque", "Esperar ayuda", "Gritar pidiendo auxilio"]

    imprimir_escenario_ascii(titulo, mensaje, opciones)
    eleccion = solicitar_opcion(opciones)
    print(f"Elegiste: {opciones[eleccion - 1]}")

if __name__ == "__main__":
    main()
