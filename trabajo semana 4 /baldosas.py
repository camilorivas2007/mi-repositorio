def contar_baldosas(n):
    if n % 2 == 1:
        return 0
    maneras = [0] * (n + 1)
    maneras[0] = 1
    
    if n >= 2:
        maneras[2] = 3

    for i in range(4, n + 1, 2):
        maneras[i] = 4 * maneras[i - 2] - maneras[i - 4]

    return maneras[n]


def main():
    n = int(input("Ingrese el ancho (n): "))
    if n < 0:
        print("El ancho debe ser un número positivo.")
        return
    else:
        resultado = contar_baldosas(n)
        print(f"El número de maneras de cubrir un piso de 2 x {n} es: {resultado}")
        if n % 2 == 1:
            print("No es posible cubrir un piso de ancho impar con baldosas de 2x1.")

main()
