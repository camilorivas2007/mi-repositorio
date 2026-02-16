def encontrar_faltante(numeros):
    for i in range(1, len(numeros) + 1):
        if i not in numeros:
            print(f"El número faltante es: {i}")
            return
        
    print("No falta ningún número.")

def main():
    numeros = input("Ingrese sus números separados por una coma (,): ").split(",")
    numeros = list(int, numeros)
    numeros.sort()
    encontrar_faltante(numeros)

main()
