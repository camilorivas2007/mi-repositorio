# Progranma grafos
# Gian Arroyo, Camilo Rivas, David Aldana

# =========================
# LABORATORIO GRAFOS 
# =========================

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "G"],
    "F": ["C", "H"],
    "G": ["E", "H"],
    "H": ["F", "G"]
}

# -------- Ordenar vecinos --------
def ordenar_grafo():
    for nodo in grafo:
        grafo[nodo].sort()

# -------- Mostrar grafo --------
def mostrar_grafo():
    posiciones = {
        "A": (10, 0),
        "B": (4,  3), "C": (16, 3),
        "D": (1,  6), "E": (7,  6), "F": (16, 6),
        "G": (10, 9), "H": (19, 9), "I": (4,  9)
    }

    FILAS, COLS = 11, 42
    grilla = [[" "] * COLS for _ in range(FILAS)]

    # Aristas
    aristas = set()
    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            if nodo not in posiciones or vecino not in posiciones:
                continue
            par = tuple(sorted([nodo, vecino]))
            if par in aristas:
                continue
            aristas.add(par)
            x1, y1 = posiciones[nodo]
            x2, y2 = posiciones[vecino]
            dx = x2 - x1
            dy = y2 - y1
            pasos = max(abs(dx), abs(dy))
            for i in range(1, pasos):
                ix = x1 + round(dx * i / pasos)
                iy = y1 + round(dy * i / pasos)
                if 0 <= iy < FILAS and 0 <= ix < COLS and grilla[iy][ix] == " ":
                    if abs(dx) < abs(dy) * 0.4:    c = "|"
                    elif abs(dy) < abs(dx) * 0.4:  c = "-"
                    else: c = "/" if (dx > 0) != (dy > 0) else "\\"
                    grilla[iy][ix] = c

    # Nodos
    for nodo, (x, y) in posiciones.items():
        if nodo not in grafo:
            continue
        if 0 <= y < FILAS and 0 <= x + 2 < COLS:
            grilla[y][x]     = "("
            grilla[y][x + 1] = nodo
            grilla[y][x + 2] = ")"

    print("\nGRAFO")
    print("=" * COLS)
    for fila in grilla:
        print("".join(fila))
    print("=" * COLS)

# -------- BFS --------
def bfs(inicio):
    visitados = []
    cola = [inicio]

    print("\nBFS (Recorrido por niveles)")
    print("Inicio en:", inicio)

    while cola:
        print("\nCola actual:", cola)

        nodo = cola.pop(0)

        if nodo not in visitados:
            print("Visitando:", nodo)
            visitados.append(nodo)

            for vecino in grafo[nodo]:
                if vecino not in visitados and vecino not in cola:
                    cola.append(vecino)

    print("\n Recorrido final BFS:", visitados)
    return visitados

# -------- DFS --------
def dfs_recursivo(nodo, visitados):
    print("Visitando:", nodo)
    visitados.append(nodo)

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            print("  ↳ Explorando desde", nodo, "hacia", vecino)
            dfs_recursivo(vecino, visitados)

def dfs(inicio):
    visitados = []
    print("\nDFS (Recorrido en profundidad)")
    print("Inicio en:", inicio)

    dfs_recursivo(inicio, visitados)

    print("\nRecorrido final DFS:", visitados)
    return visitados

# -------- Comparación --------
def comparacion():
    print("\nCOMPARACIÓN BFS vs DFS")
    print("- BFS recorre por niveles (encuentra caminos más cortos).")
    print("- DFS profundiza primero (explora toda la red).")

# -------- Agregar nodo I --------
def agregar_nodo_I():
    if "I" not in grafo:
        grafo["I"] = ["E", "H"]
        grafo["E"].append("I")
        grafo["H"].append("I")
        ordenar_grafo()
        print("\nNodo I agregado correctamente.")
        mostrar_grafo()   
    else:
        print("\nEl nodo I ya fue agregado.")
        mostrar_grafo() 

# -------- Comparar antes vs después --------
def comparar_antes_despues():
    print("\n=========== ANTES ===========")
    bfs("A")
    dfs("A")

    print("\nAgregando nodo I...")
    agregar_nodo_I()

    print("\n=========== DESPUÉS ===========")
    bfs("A")
    dfs("A")

# -------- Interpretación --------
def interpretacion():
    print("\nINTERPRETACIÓN")
    print("- El grafo representa bodegas y conexiones.")
    print("- BFS permite encontrar rutas con menos conexiones.")
    print("- DFS permite explorar toda la red.")
    print("- Programar evita errores y es más eficiente.")
    print("- Aplicaciones: redes sociales, mapas, internet.")

# -------- MENÚ --------
def menu():
    ordenar_grafo()

    while True:
        print("\n==============================")
        print("     MENÚ PRINCIPAL")
        print("==============================")
        print("1. Mostrar grafo")
        print("2. Ejecutar BFS desde A")
        print("3. Ejecutar DFS desde A")
        print("4. Comparar BFS y DFS")
        print("5. Agregar nodo I")
        print("6. Comparar ANTES vs DESPUÉS")
        print("7. Interpretación")
        print("8. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            mostrar_grafo()

        elif opcion == "2":
            bfs("A")

        elif opcion == "3":
            dfs("A")

        elif opcion == "4":
            comparacion()

        elif opcion == "5":
            agregar_nodo_I()

        elif opcion == "6":
            comparar_antes_despues()

        elif opcion == "7":
            interpretacion()

        elif opcion == "8":
            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción inválida.")


# -------- EJECUCIÓN --------
menu()
