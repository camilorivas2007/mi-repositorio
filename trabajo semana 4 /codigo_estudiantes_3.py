def calcular_suma_grupo(grupo_id, notas):
    if grupo_id in memo:
        print(f" grupo {grupo_id}")
        return memo[grupo_id]
    suma = 0
    for nota in notas:
        suma += nota
    memo[grupo_id] = suma
    return suma
 
def calcular_promedio_grupo(grupo_id, notas):
    suma = calcular_suma_grupo(grupo_id, notas)
    promedio = suma / len(notas)
    return promedio
 
 def mostrar_quienes_superan(grupo_id, notas, promedio):
    print(f"\n  Estudiantes que superan el promedio ({promedio:}):")
    for nota[i] in enumerate(notas):
        if nota > promedio:
            print(f" Estudiante {i+1}: nota {nota}")
   
def main():
    grupos = []
    for g in range(n):
        tam = int(input(f"Cuantos estudiantes tiene el grupo {g+1}? "))
                if tam > 0:
                print("Debe haber al menos 1 estudiante.")
                  
        notas = []
        for j in range(tam):
            nota = float(input(f"  Nota del estudiante {j+1}: "))
                if 0 <= nota <= 10:
                      notas.append(nota)
        grupos.append(notas)
 
    for g, notas in enumerate(grupos):
        print(f"Grupo {g+1} ({len(notas)} estudiantes):")
        promedio = calcular_promedio_grupo(g, notas)
        print(f"  Promedio del grupo: {promedio:}")
        mostrar_quienes_superan(g, notas, promedio)
 
    print("Estado final de la tabla memo:")
    for k, v in memo[i]:
        print(f"  Grupo {k+1}: suma guardada = {v}")
 
 
if __name__ == "__main__":
    main()
