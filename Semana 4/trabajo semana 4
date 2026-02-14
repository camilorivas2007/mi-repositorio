# Problema baldosas
## Descripción del problema
Dada una tabla de tamaño 3 x n, se desea calcular cuántas formas distintas existen de cubrir completamente el tablero utilizando fichas de dominó de tamaño 2 x 1.
Las fichas pueden colocarse tanto de manera vertical como horizontal, pero deben cubrir exactamente toda la superficie sin solaparse ni dejar espacios vacíos.
## Requerimientos (Historias de Usuario)
- Como usuario, quiero ingresar el valor de n para conocer cuántas formas existen de cubrir el tablero.
- Como usuario, quiero que el sistema calcule el resultado de manera eficiente sin probar todas las combinaciones.
- Como usuario, quiero obtener el número total de configuraciones posibles para analizar el crecimiento del problema.
- Como estudiante, quiero aplicar programación dinámica para evitar cálculos repetidos.
## Análisis del problema
Si intentamos resolver el problema probando todas las combinaciones posibles, el costo computacional crece exponencialmente.
Sin embargo, el problema tiene una característica clave:
- Los resultados grandes dependen de resultados más pequeños.
- Esto permite usar programación dinámica, almacenando soluciones previas y reutilizándolas.
## Diseño de la solución
El algoritmo:
Verifica si n es impar.
Si es impar, retorna 0.
Crea un arreglo dp para guardar resultados ya calculados.
Inicializa los casos base.
Calcula iterativamente usando la relación de recurrencia.
Retorna el valor final sin recalcular nada.

- Complejidad temporal: O(n)
- Complejidad espacial: Se usa un arreglo de tamaño n → O(n)

## Relación de recurrencia
El número de formas de cubrir la tabla sigue la siguiente fórmula:
F(n) = 4 * F(n - 2) - F(n - 4)
Con los casos base:
- F(0) = 1
- F(2) = 3

Además:
Si n es impar → F(n) = 0
Porque un tablero de 3 x n con n impar no puede cubrirse completamente con dominós de tamaño 2 x 1.
## Ejemplo de cálculo manual
### Para n = 4:

F(4) = 4 * F(2) - F(0)
F(4) = 4 * 3 - 1
F(4) = 11
### Para n = 6:
F(6) = 4 * F(4) - F(2)
F(6) = 4 * 11 - 3
F(6) = 41
## Diagramas
### De flujo
<img width="492" height="469" alt="image" src="https://github.com/user-attachments/assets/11b7cc83-182e-4708-ba1d-5662dbf069be" />

### De Secuencia
<img width="588" height="679" alt="image" src="https://github.com/user-attachments/assets/f91f8f3b-bc03-44bd-8db9-27d7debdd674" />

### De casos de uso
<img width="845" height="647" alt="image" src="https://github.com/user-attachments/assets/80a9c9f9-ff5f-4236-800d-2eafa031d358" />
