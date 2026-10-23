cabeza = None
cola = None
pagina_actual = None

def crear_nodo(dato):
    return {"dato": dato, "anterior": None, "siguiente": None}

def visitar(url):
    global cabeza, cola, pagina_actual
    nuevo = crear_nodo(url)

    if pagina_actual is None:
        cabeza = cola = pagina_actual = nuevo
        return

    pagina_actual["siguiente"] = None
    cola = pagina_actual

    nuevo["anterior"] = cola
    cola["siguiente"] = nuevo
    cola = nuevo
    pagina_actual = nuevo

def retroceder():
    global pagina_actual
    if pagina_actual is None or pagina_actual["anterior"] is None:
        return False
    pagina_actual = pagina_actual["anterior"]
    return True

def avanzar():
    global pagina_actual
    if pagina_actual is None or pagina_actual["siguiente"] is None:
        return False
    pagina_actual = pagina_actual["siguiente"]
    return True

def mostrar_actual():
    if pagina_actual is None:
        print("No has visitado ninguna página todavía.")
    else:
        print("Página actual:", pagina_actual["dato"])

def mostrar_historial():
    if cabeza is None:
        print("Historial vacío.")
        return
    nodo = cabeza
    partes = []
    while nodo is not None:
        texto = nodo["dato"]
        partes.append(f"[{texto}]" if nodo is pagina_actual else texto)
        nodo = nodo["siguiente"]
    print(" ↔ ".join(partes))

def menu():
    while True:
        print("=== Menú ===")
        print("1. Visitar página")
        print("2. Retroceder")
        print("3. Avanzar")
        print("4. Mostrar página actual")
        print("5. Ver historial")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            url = input("Página a visitar: ").strip()
            if url == "":
                print("Debes escribir el nombre de una página.")
            else:
                visitar(url)
                print("Visitando:", url)
        elif opcion == "2":
            if retroceder():
                mostrar_actual()
            else:
                print("No hay páginas anteriores.")
        elif opcion == "3":
            if avanzar():
                mostrar_actual()
            else:
                print("No hay páginas siguientes.")
        elif opcion == "4":
            mostrar_actual()
        elif opcion == "5":
            mostrar_historial()
        elif opcion == "0":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

menu()