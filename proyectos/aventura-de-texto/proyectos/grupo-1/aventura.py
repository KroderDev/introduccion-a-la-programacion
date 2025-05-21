from funciones import imprimir_escenario_ascii, solicitar_opcion

inventario = []

def agregar_objeto(objeto):
    if len(inventario) < 2:
        inventario.append(objeto)
        print(f"Has añadido '{objeto}' a tu inventario.")
    else:
        print("Tu mochila está muy llena. No puedes llevar más objetos.")

def remover_objeto(objeto):
    if objeto in inventario:
        inventario.remove(objeto)

def bosque():
    titulo = "Bosque Encantado"
    mensaje = "El bosque está lleno de sonidos extraños y árboles altos. Encuentras una rama mágica en el suelo."
    opciones = ["Tomar la rama mágica", "Ignorar y seguir caminando"]
    imprimir_escenario_ascii(titulo, mensaje, opciones)
    eleccion = solicitar_opcion(opciones)

    if eleccion == 1:
        agregar_objeto("Rama mágica")
        claro()
    else:
        claro()

def claro():
    titulo = "Claro del bosque"
    mensaje = "Llegas a un claro donde hay una roca brillante y una cueva oscura."
    opciones = ["Investigar la roca", "Entrar en la cueva"]
    imprimir_escenario_ascii(titulo, mensaje, opciones)
    eleccion = solicitar_opcion(opciones)

    if eleccion == 1:
        if "Rama mágica" in inventario:
            print("¡La roca reacciona a la rama mágica! Se convierte en una espada legendaria.")
            remover_objeto("Rama mágica")
            agregar_objeto("Espada legendaria")
        else:
            print("La roca brilla pero no ocurre nada especial.")
        cueva()
    else:
        cueva()

def cueva():
    titulo = "Cueva misteriosa"
    mensaje = "Dentro de la cueva ves tres caminos: uno iluminado, otro oscuro, y una puerta sellada."
    opciones = ["Seguir el camino iluminado", "Ir por el camino oscuro", "Abrir la puerta con la llave dorada"]
    imprimir_escenario_ascii(titulo, mensaje, opciones)
    eleccion = solicitar_opcion(opciones)

    if eleccion == 1:
        final_bueno()
    elif eleccion == 2:
        if "Espada legendaria" in inventario:
            print("Usas tu espada para abrirte paso en la oscuridad y derrotar a una criatura. Logras escapar.")
            final_bueno()
        else:
            final_malo()
    else:
        if "Llave dorada" in inventario:
            puerta_secreta()
        else:
            print("La puerta no se abre. Tal vez necesitas una llave especial.")
            cueva()

def puerta_secreta():
    titulo = "Sala Secreta"
    mensaje = "Abres la puerta dorada y encuentras un tesoro escondido. Eres rico y famoso por tu hallazgo."
    opciones = ["Ver inventario", "Salir"]
    imprimir_escenario_ascii(titulo, mensaje, opciones)
    eleccion = solicitar_opcion(opciones)
    if eleccion == 1:
        print(f"Inventario final: {inventario}")
    print("Gracias por jugar. ¡Final Secreto!")

def final_bueno():
    titulo = "Santuario del Héroe"
    mensaje = "Encuentras un santuario donde te nombran héroe del bosque. ¡Felicidades!"
    opciones = ["Ver inventario", "Salir"]
    imprimir_escenario_ascii(titulo, mensaje, opciones)
    eleccion = solicitar_opcion(opciones)
    if eleccion == 1:
        print(f"Inventario final: {inventario}")
    print("Gracias por jugar.")

def final_malo():
    titulo = "Trampa del Olvido"
    mensaje = "Caes en una trampa y pierdes el conocimiento. Cuando despiertas, no recuerdas nada..."
    opciones = ["Ver inventario", "Salir"]
    imprimir_escenario_ascii(titulo, mensaje, opciones)
    eleccion = solicitar_opcion(opciones)
    if eleccion == 1:
        print(f"Inventario final: {inventario}")
    print("Fin de la historia.")

def easter_egg():
    print("¡Descubriste el easter egg! Un conejo parlante te da una llave dorada.")
    agregar_objeto("Llave dorada")

def inicio():
    titulo = "Inicio de la Aventura"
    mensaje = "Te despiertas al borde de un bosque encantado. ¿Qué quieres hacer?"
    opciones = ["Entrar al bosque", "Gritar 'conejo mágico'"]
    imprimir_escenario_ascii(titulo, mensaje, opciones)
    eleccion = solicitar_opcion(opciones)

    if eleccion == 1:
        bosque()
    else:
        easter_egg()
        bosque()

if __name__ == "__main__":
    inicio()
