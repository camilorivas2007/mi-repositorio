def estudiantes_promedio():
    x = input("Ingrese nombre y nota del estudiante: ")
    datos = x.split()
    i = 0
    notas = []
    nombres = []
    suma = 0

    while i < len(datos):
        nombre = datos[i]
        nota = float(datos[i+1]) 
        notas.append(nota)
        nombres.append(nombre)
        suma += notas
        promedio = suma/len(notas)

    print("Estudiantes con nota mayor o igual al promedio:")
    for i in range(len(notas)):
        if notas[i] >= promedio:
            print(nombres[i])