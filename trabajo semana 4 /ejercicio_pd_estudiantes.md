# Ejercicio Programacion Dinamica Estudiantes
En un comienzo el problema general trataba sobre: calcular un unico promedio global de una lista de estudiantes 
y mostrar quienes lo superan, ahora vamos a medir la complejidad utlizando programacion dinamica para este 
problema, bajando la complejidad bastante. 
## Requerimientos
| ID | Historia de usuario | aceptacion |
|----|--------|--------|
| HU-01 | Como usuario, quiero definir cuántos grupos existen para organizar a mis estudiantes | El sistema acepta N >= 1 grupos |
| HU-02 | Como usuario, quiero ingresar el tamaño de cada grupo, ya que pueden ser diferentes | Cada grupo tiene un número distinto de estudiantes.|
| HU-03 | Cada grupo tiene un número distinto de estudiantes. | Si la suma de un grupo ya fue calculada, se usa el valor guardado en memo.  |
| HU-04 | Como usuario, quiero ver qué estudiantes superan el promedio de su grupo. | Se muestran los estudiantes cuya nota > promedio del grupo. |

# Diagramas 
## Diagrma de flujo 
<img width="404" height="833" alt="image" src="https://github.com/user-attachments/assets/68d4d5f2-94ab-4a68-8f5e-8fa37d64b5b9" />

# Diagrama De Secuencia 
<img width="676" height="538" alt="image" src="https://github.com/user-attachments/assets/0bbbe88d-04f6-4986-9f6d-f0d4b585ffbe" />

# Diagrama de Caso de Uso
<img width="688" height="510" alt="image" src="https://github.com/user-attachments/assets/97025eac-49ac-4460-bb1d-a27254675c00" />

# Análisis de Complejidad
## Peor caso — O(n^2)
Sin memoización, con cada grupo se tendria que calcular de nuevo los resultados para confirmar el grupo y el promedio de los estudiantes.

<img width="542" height="281" alt="image" src="https://github.com/user-attachments/assets/8c4c6a33-1f32-4943-bc22-f39cfc029a28" />

## Mejor caso — O(n)
Todos los grupos ya están en memo. Solo se itera por grupos.

<img width="531" height="282" alt="image" src="https://github.com/user-attachments/assets/031f3878-e5bc-42ad-be8d-62194d4b8b7c" />


En conclusión con memorización la complejidad del código disminuye considerablemente respecto a no utilizarla, con esto nos acelera los procesos y no va a tener una complejidad muy alta.  






