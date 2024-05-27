import time
import os

def es_estado_valido(orilla):
    if "vikingo" not in orilla:
        if "lobo" in orilla and "caperucita" in orilla:
            return False, "💀El lobo se comió a la caperucita💀"
        if "caperucita" in orilla and "uvas" in orilla:
            return False, "🍴La caperucita se comió las uvas🍴"
    return True, ""

def cruzar_rio(orilla_izquierda, orilla_derecha, objeto, direccion):
    nueva_orilla_izquierda, nueva_orilla_derecha = orilla_izquierda.copy(), orilla_derecha.copy()
    mover_desde, mover_hacia = (nueva_orilla_izquierda, nueva_orilla_derecha) if direccion == "derecha" else (nueva_orilla_derecha, nueva_orilla_izquierda)
    mover_desde.remove("vikingo")
    mover_hacia.append("vikingo")
    if objeto != "nada":
        if objeto not in mover_desde:
            return None, None, f"El objeto {objeto} no está en la orilla {'izquierda' if direccion == 'derecha' else 'derecha'}."
        mover_desde.remove(objeto)
        mover_hacia.append(objeto)
    valido_izquierda, mensaje_izquierda = es_estado_valido(nueva_orilla_izquierda)
    valido_derecha, mensaje_derecha = es_estado_valido(nueva_orilla_derecha)
    if valido_izquierda and valido_derecha:
        return nueva_orilla_izquierda, nueva_orilla_derecha, ""
    return None, None, mensaje_izquierda if not valido_izquierda else mensaje_derecha

def imprimir_estado(orilla_izquierda, orilla_derecha):
    print(f"[{', '.join(map(lambda x: emojis[x], orilla_izquierda))}]🌊🌊🌊🌊🌊🌊[{', '.join(map(lambda x: emojis[x], orilla_derecha))}]")

def animar_cruce(objeto, direccion):
    for i in range(6, 0, -1) if direccion == "derecha" else range(1, 7):
        limpiar_pantalla()
        print(f"[{', '.join(map(lambda x: emojis[x], orilla_izquierda))}]🌊{'🌊' * (6-i if direccion == 'derecha' else 6-i)}🛶{emojis[objeto]}🧔🪓{'🌊' * (i if direccion == 'derecha' else i)}[{', '.join(map(lambda x: emojis[x], orilla_derecha))}]")
        time.sleep(0.5)

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

emojis = {
    "vikingo": "🧔🪓",
    "lobo": "🐺",
    "caperucita": "👧",
    "uvas": "🍇",
    "nada": "🛶"
}

def juego():
    global orilla_izquierda, orilla_derecha
    orilla_izquierda, orilla_derecha = ["vikingo", "lobo", "caperucita", "uvas"], []
    direccion = "derecha"
    while set(orilla_derecha) != {"vikingo", "lobo", "caperucita", "uvas"}:
        limpiar_pantalla()
        imprimir_estado(orilla_izquierda, orilla_derecha)
        objeto = input("¿Qué quieres llevar al otro lado? (lobo/caperucita/uvas/nada): ").strip().lower()
        if objeto not in {"lobo", "caperucita", "uvas", "nada"}:
            print("Objeto no válido, intenta de nuevo.")
            time.sleep(2)
            continue
        nueva_orilla_izquierda, nueva_orilla_derecha, mensaje_error = cruzar_rio(orilla_izquierda, orilla_derecha, objeto, direccion)
        if nueva_orilla_izquierda is None or nueva_orilla_derecha is None:
            print(f"Movimiento no válido: {mensaje_error} \n")
            time.sleep(2)
            continue
        animar_cruce(objeto, direccion)
        orilla_izquierda, orilla_derecha = nueva_orilla_izquierda, nueva_orilla_derecha
        direccion = "izquierda" if direccion == "derecha" else "derecha"
    limpiar_pantalla()
    imprimir_estado(orilla_izquierda, orilla_derecha)
    print("✨✨¡Felicidades! Has cruzado todos los objetos de manera segura.✨✨")

# Para jugar al juego, descomente la siguiente línea:
juego()
