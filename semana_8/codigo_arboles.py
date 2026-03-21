# Codigo para arboles AVL 
# David Aldana, Gian Arroyo, Camilo Rivas

# ---------- NODO ----------

"""Crea un nodo como diccionario con valor, referencias a hijos izquierdo y derecho, y altura."""
def crear_nodo(valor):
    return {
        "valor": valor,
        "izq": None,
        "der": None,
        "altura": 1
    }


# ---------- UTILIDADES ----------

"""Funciones para calcular la altura de un nodo y el balance del árbol."""

def altura(nodo):
    if nodo is None:
        return 0
    return nodo["altura"]


def balance(nodo):
    if nodo is None:
        return 0
    return altura(nodo["izq"]) - altura(nodo["der"])


# ---------- ROTACIONES ----------

"""Diccionarios para rotar a la derecha e izquierda, actualizando alturas después de cada rotación."""

def rotar_derecha(y):
    x = y["izq"]
    t2 = x["der"]

    x["der"] = y
    y["izq"] = t2

    y["altura"] = 1 + max(altura(y["izq"]), altura(y["der"]))
    x["altura"] = 1 + max(altura(x["izq"]), altura(x["der"]))

    return x


def rotar_izquierda(x):
    y = x["der"]
    t2 = y["izq"]

    y["izq"] = x
    x["der"] = t2

    x["altura"] = 1 + max(altura(x["izq"]), altura(x["der"]))
    y["altura"] = 1 + max(altura(y["izq"]), altura(y["der"]))

    return y


# ---------- OPERACIONES ----------

""" Inserta un valor en el árbol AVL, actualiza alturas y realiza rotaciones \
si es necesario para mantener el balance."""
def insertar(nodo, valor):

    if nodo is None:
        return crear_nodo(valor)

    if valor < nodo["valor"]:
        nodo["izq"] = insertar(nodo["izq"], valor)

    elif valor > nodo["valor"]:
        nodo["der"] = insertar(nodo["der"], valor)

    else:
        print(f"El valor {valor} ya existe y no se insertará.")
        return nodo

    nodo["altura"] = 1 + max(altura(nodo["izq"]), altura(nodo["der"]))

    b = balance(nodo)

    if b > 1 and valor < nodo["izq"]["valor"]:
        return rotar_derecha(nodo)

    if b < -1 and valor > nodo["der"]["valor"]:
        return rotar_izquierda(nodo)

    if b > 1 and valor > nodo["izq"]["valor"]:
        nodo["izq"] = rotar_izquierda(nodo["izq"])
        return rotar_derecha(nodo)

    if b < -1 and valor < nodo["der"]["valor"]:
        nodo["der"] = rotar_derecha(nodo["der"])
        return rotar_izquierda(nodo)

    return nodo


def buscar(nodo, valor):

    if nodo is None:
        return False

    if valor == nodo["valor"]:
        return True

    if valor < nodo["valor"]:
        return buscar(nodo["izq"], valor)

    return buscar(nodo["der"], valor)


# ---------- RECORRIDOS ----------

"""Diccionarios para realizar recorridos inorden, preorden y postorden, \
    imprimiendo los valores de los nodos en el orden correspondiente."""

def inorden(nodo):
    if nodo:
        inorden(nodo["izq"])
        print(nodo["valor"], end=" ")
        inorden(nodo["der"])


def preorden(nodo):
    if nodo:
        print(nodo["valor"], end=" ")
        preorden(nodo["izq"])
        preorden(nodo["der"])


def postorden(nodo):
    if nodo:
        postorden(nodo["izq"])
        postorden(nodo["der"])
        print(nodo["valor"], end=" ")


def imprimir(nodo, prefijo="", es_izq=True):
    if nodo is None:
        return
    imprimir(nodo["der"], prefijo + ("│   " if es_izq else "    "), False)
    print(prefijo + ("└── " if es_izq else "┌── ") + str(nodo["valor"]))
    imprimir(nodo["izq"], prefijo + ("    " if es_izq else "│   "), True)


# ---------- ENTRADA SEGURA ----------

"""Valida la entrada del usuario para asegurarse de que se ingresen números enteros"""

def leer_varios_numeros():
    while True:

        entrada = input(
            "\nIngrese uno o varios códigos separados por espacio o coma\n"
            "Ejemplo: 50 30 70 20\n"
            ">> "
        )

        entrada = entrada.replace(",", " ").split()

        numeros = []
        error = False

        for x in entrada:
            try:
                numeros.append(int(x))
            except ValueError:
                print(f"'{x}' no es un número válido.")
                error = True
                break

        if not error and numeros:
            return numeros

        print("Intente nuevamente.\n")


def leer_un_numero():
    while True:
        entrada = input("Ingrese el código del computador: ")
        try:
            return int(entrada)
        except ValueError:
            print("Debe ingresar un número entero.")


# ---------- MENÚ ----------

"""Muestra un menú interactivo para gestionar el inventario de computadores utilizando un árbol AVL"""

def menu():

    raiz = None

    print("====================================")
    print(" SISTEMA DE INVENTARIO DE COMPUTADORES")
    print(" Basado en Árbol AVL (Auto balanceado)")
    print("====================================")

    while True:

        print("\nMENU")
        print("1 Insertar uno o varios computadores")
        print("2 Buscar computador")
        print("3 Mostrar recorrido INORDEN")
        print("4 Mostrar recorrido PREORDEN")
        print("5 Mostrar recorrido POSTORDEN")
        print("6 Ver árbol visual")
        print("7 Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            numeros = leer_varios_numeros()

            for n in numeros:
                raiz = insertar(raiz, n)

            print("Inserción completada.")

        elif opcion == "2":

            valor = leer_un_numero()

            if buscar(raiz, valor):
                print("El computador existe en el inventario.")
            else:
                print("El computador NO está registrado.")

        elif opcion == "3":

            if raiz is None:
                print("El árbol está vacío.")
            else:
                print("Recorrido Inorden (ordenado):")
                inorden(raiz)
                print()

        elif opcion == "4":

            if raiz is None:
                print("El árbol está vacío.")
            else:
                print("Recorrido Preorden:")
                preorden(raiz)
                print()

        elif opcion == "5":

            if raiz is None:
                print("El árbol está vacío.")
            else:
                print("Recorrido Postorden:")
                postorden(raiz)
                print()

        elif opcion == "6":

            if raiz is None:
                print("El árbol está vacío.")
            else:
                print("\nÁrbol (la raíz queda al centro-izquierda):")
                imprimir(raiz)
                print()

        elif opcion == "7":

            print("Programa finalizado.")
            break

        else:

            print("Opción inválida. Seleccione una opción del 1 al 7.")


if __name__ == "__main__":
    menu()
