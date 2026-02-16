# Diseño del Algoritmo  
##  Estudiantes sobre el Promedio  
**Paradigma:** Divide y Vencerás  

---

##  1. Descripción del Problema

Dada una lista de estudiantes con sus respectivas notas, se requiere:

- Calcular el promedio de todas las notas.
- Identificar y mostrar los estudiantes cuya nota sea mayor o igual al promedio.
- Implementar la solución utilizando el paradigma **Divide y Vencerás**.

---

##  2. Requerimientos (Historias de Usuario)

###  Historia de Usuario 1: Entrada de Datos

**Como** usuario del sistema,  
**quiero** ingresar una lista de estudiantes con sus notas,  
**para que** el sistema pueda procesarlas.

#### Criterios de aceptación:

- El formato de entrada debe ser:

```bash
nombre1 nota1 nombre2 nota2 ...
```

- Las notas deben ser valores numéricos válidos.
- Debe haber al menos un estudiante en la lista.

---

###  Historia de Usuario 2: Cálculo del Promedio

**Como** usuario del sistema,  
**quiero** que se calcule automáticamente el promedio de notas,  
**para que** sirva como referencia de comparación.

####  Criterios de aceptación:

- El promedio debe calcularse usando **Divide y Vencerás**.
- El cálculo debe ser preciso (permitir números decimales).
- Debe sumar todas las notas y dividir por la cantidad de estudiantes.

---

###  Historia de Usuario 3: Filtrado de Estudiantes

**Como** usuario del sistema,  
**quiero** ver únicamente los estudiantes con nota sobre el promedio,  
**para que** pueda identificar a los estudiantes destacados.

#### Criterios de aceptación:

- Mostrar solo estudiantes con nota **≥ promedio**.
- Utilizar **Divide y Vencerás** para el filtrado.
- Imprimir el nombre de cada estudiante que cumple la condición.

---

# 📈 3. Análisis de Complejidad

## ⏱️ 3.1 Complejidad Temporal y Espacial (Big O)

| Función                      | Complejidad Temporal | Complejidad Espacial |
|------------------------------|----------------------|----------------------|
| `sumar_notas()`              | O(n)                 | O(log n)             |
| `mostrar_sobre_promedio()`   | O(n)                 | O(log n)             |
| **Total del Programa**       | **O(n)**             | **O(log n)**         |

---

##  3.2 Justificación del Análisis

###  Complejidad Temporal: **O(n)**

Aunque el algoritmo utiliza recursión y divide el problema en mitades, cada elemento se procesa exactamente una vez.

Relación de recurrencia:

```
T(n) = 2T(n/2) + O(1)
```

Aplicando el Teorema Maestro:

```
O(n)
```

---

###  Complejidad Espacial: **O(log n)**

El espacio adicional utilizado corresponde a la pila de recursión.

Como la profundidad máxima del árbol de recursión es:

```
log₂(n)
```

El espacio requerido es:

```
O(log n)
```

---

##  3.3 Mejor Caso, Peor Caso y Caso Promedio

- **Mejor Caso:** O(n)  
- **Peor Caso:** O(n)  
- **Caso Promedio:** O(n)  

El algoritmo siempre procesa todos los elementos de la lista, por lo que su complejidad no depende del orden de los datos.
