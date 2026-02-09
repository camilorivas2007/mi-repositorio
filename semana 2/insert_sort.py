#Insertion sort descendente

def main():
    entrada = input("Ingrese los números que desea ordenar, separados por comas: ")
    lista = [int(x) for x in entrada.split(",")]
    for i in range(1, len(lista)):
        llave = lista[i]
        j = i - 1
        while j >= 0 and llave > lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = llave
    print("La lista ordenada es:", lista)

main()