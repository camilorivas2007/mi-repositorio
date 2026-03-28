## 1. Requerimientos del sistema

### 1.1 Requerimientos funcionales

| ID | Descripción |
|----|-------------|
| RF-01 | Mostrar el grafo visualmente en consola usando caracteres ASCII con nodos y aristas. |
| RF-02 | Ejecutar el recorrido BFS (anchura) desde el nodo A, mostrando la cola y visitas paso a paso. |
| RF-03 | Ejecutar el recorrido DFS (profundidad) desde el nodo A de forma recursiva, mostrando el árbol de exploración. |
| RF-04 | Mostrar una comparación conceptual entre BFS y DFS explicando sus diferencias y usos. |
| RF-05 | Agregar el nodo I al grafo con conexiones a E y H, sin permitir duplicados. |
| RF-06 | Ejecutar BFS y DFS antes y después de agregar el nodo I para comparar los recorridos. |
| RF-07 | Mostrar la interpretación del grafo como red de bodegas con sus aplicaciones. |
| RF-08 | Ordenar los vecinos de cada nodo en orden alfabético al iniciar y al modificar el grafo. |

### 1.2 Requerimientos no funcionales

| ID | Descripción |
|----|-------------|
| RNF-01 | El programa debe ejecutarse en Python 3 sin dependencias externas (solo módulos estándar). |
| RNF-02 | El menú debe validar entradas inválidas e informar al usuario sin detener la ejecución. |
| RNF-03 | El grafo visual debe adaptarse dinámicamente a la adición de nuevos nodos. |
| RNF-04 | El código debe estar organizado en funciones independientes y reutilizables. |

---

## 2. Historial de usuario

**Actor:** Estudiante

| ID | Historia de usuario |
|----|---------------------|
| HU-01 | Como estudiante, quiero ver el grafo representado gráficamente en consola para entender su estructura de nodos y conexiones sin necesidad de leer el código fuente. |
| HU-02 | Como estudiante, quiero ejecutar BFS desde el nodo A para observar cómo el algoritmo recorre el grafo por niveles y ver el estado de la cola en cada paso. |
| HU-03 | Como estudiante, quiero ejecutar DFS desde el nodo A para observar cómo el algoritmo explora en profundidad y ver el árbol de exploración recursivo. |
| HU-04 | Como estudiante, quiero ver una comparación entre BFS y DFS para entender cuándo conviene usar cada uno según el problema a resolver. |
| HU-05 | Como estudiante, quiero agregar el nodo I al grafo para ver cómo se expande la red y verificar que el sistema no permite duplicados. |
| HU-06 | Como estudiante, quiero ejecutar los recorridos antes y después de agregar I para analizar el impacto del nuevo nodo en los resultados de BFS y DFS. |
| HU-07 | Como estudiante, quiero ver la interpretación del grafo como red de bodegas para relacionar la teoría de grafos con un caso de uso real. |

### Criterios de aceptación comunes

- El sistema muestra los resultados paso a paso en consola.
- El sistema no lanza excepciones ante entradas inválidas ni nodos duplicados.
- Cada función puede ejecutarse de forma independiente desde el menú.

---

## 3. Diagramas

### 3.1 Diagrama de flujo
<img width="680" height="860" alt="diagrama_flujo" src="https://github.com/user-attachments/assets/ed5f4d52-f6ce-4d2f-bbd3-d5bf3804874f" />

### 3.2 Diagrama de casos de uso
<img width="680" height="580" alt="diagrama_casos_uso" src="https://github.com/user-attachments/assets/8d19b98c-7b0e-45e2-a2f6-75c67b04cc6e" />

### 3.3 Diagrama de secuencia
<img width="680" height="700" alt="diagrama_secuencia" src="https://github.com/user-attachments/assets/158ff0b4-3be4-4524-9a42-21595bbe0d1a" />
