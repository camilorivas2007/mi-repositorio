
*Autores:* David Aldana · Gian Franco · Camilo Rivas

---


## 📚 Contexto del Laboratorio

### Objetivo General

Comprender la estructura y funcionamiento de los árboles en informática, identificando sus componentes, realizando recorridos y aplicando operaciones básicas en árboles binarios de búsqueda (BST) y árboles AVL mediante un caso aplicado al inventario de computadores.

### Objetivos Específicos

- Identificar los elementos de un árbol (raíz, nodos y hojas).
- Comprender el funcionamiento de un árbol binario de búsqueda.
- Aplicar recorridos del árbol: preorden, inorden y postorden.
- Insertar datos en un árbol binario de búsqueda.
- Reconocer cuándo un árbol se desbalancea.
- Comprender la utilidad de los árboles AVL.

---

##  Requerimientos Funcionales

| ID | Nombre | Descripción | Prioridad |
|---|---|---|---|
| RF-01 | Insertar nodo | El sistema debe permitir insertar uno o varios valores enteros (códigos de computadores) en el árbol AVL. | Alta |
| RF-02 | Validar duplicados | El sistema debe detectar valores duplicados e informar al usuario sin realizar la inserción. | Alta |
| RF-03 | Autobalanceo | Tras cada inserción, el árbol debe reequilibrarse automáticamente mediante rotaciones simples y dobles. | Alta |
| RF-04 | Buscar nodo | El sistema debe permitir buscar un valor e indicar si existe o no en el árbol. | Alta |
| RF-05 | Recorrido Inorden | El sistema debe mostrar los valores del árbol en recorrido inorden (ascendente). | Media |
| RF-06 | Recorrido Preorden | El sistema debe mostrar los valores en recorrido preorden (raíz primero). | Media |
| RF-07 | Recorrido Postorden | El sistema debe mostrar los valores en recorrido postorden (raíz al final). | Media |
| RF-08 | Visualización árbol | El sistema debe imprimir una representación visual del árbol en consola usando caracteres ASCII. | Media |
| RF-09 | Validar entrada | El sistema debe rechazar entradas no numéricas e informar el error al usuario. | Alta |
| RF-10 | Menú interactivo | El sistema debe ofrecer un menú de opciones numeradas para navegar las funcionalidades. | Alta |

---

##  Requerimientos No Funcionales

| ID | Categoría | Descripción | Prioridad |
|---|---|---|---|
| RNF-01 | Rendimiento | Las operaciones de inserción y búsqueda deben ejecutarse en O(log n). | Alta |
| RNF-02 | Usabilidad | El menú debe ser claro y autodescriptivo para usuarios sin conocimiento técnico. | Media |
| RNF-03 | Robustez | El sistema no debe detenerse ante entradas inválidas; debe capturar excepciones y continuar. | Alta |
| RNF-04 | Mantenibilidad | El código debe estar organizado en funciones separadas por responsabilidad (nodo, rotaciones, operaciones, recorridos, menú). | Media |
| RNF-05 | Portabilidad | El sistema debe ejecutarse en cualquier entorno con Python 3.x sin dependencias externas. | Alta |
| RNF-06 | Escalabilidad | La estructura debe soportar la inserción de grandes volúmenes de nodos sin degradar el balance. | Media |

---

## Historias de Usuario

---

### HU-01 — Registrar computadores en el inventario

| Campo | Detalle |
|---|---|
| **Rol** | Administrador de inventario |
| **Quiero** | Registrar uno o varios computadores ingresando su código |
| **Para** | Tener el inventario actualizado sin necesidad de buscar manualmente la posición de inserción |
| **Requerimientos** | RF-01, RF-02, RF-09 |
| **Prioridad** | Alta |

**Criterios de aceptación:**
- El sistema acepta múltiples códigos separados por espacio o coma.
- Los duplicados son notificados sin interrumpir la carga del resto.
- Las entradas no numéricas muestran un mensaje de error claro.

---

### HU-02 — Verificar si un equipo está registrado

| Campo | Detalle |
|---|---|
| **Rol** | Técnico de soporte |
| **Quiero** | Buscar si un código de computador está registrado |
| **Para** | Saber rápidamente si un equipo pertenece al inventario sin revisar toda la lista |
| **Requerimientos** | RF-04 |
| **Prioridad** | Alta |

**Criterios de aceptación:**
- El sistema responde con un mensaje claro indicando si el equipo existe o no.
- La búsqueda no modifica el árbol.

---

### HU-03 — Ver todos los equipos en orden ascendente

| Campo | Detalle |
|---|---|
| **Rol** | Auditor de sistemas |
| **Quiero** | Ver el listado de todos los computadores en orden ascendente |
| **Para** | Verificar que los códigos estén bien registrados y no haya saltos inesperados |
| **Requerimientos** | RF-05 |
| **Prioridad** | Alta |

**Criterios de aceptación:**
- El recorrido inorden imprime los valores de menor a mayor.
- Si el árbol está vacío, se muestra un mensaje indicativo.

---

### HU-04 — Validar la estructura interna del árbol

| Campo | Detalle |
|---|---|
| **Rol** | Docente / evaluador |
| **Quiero** | Ver los recorridos preorden y postorden del árbol |
| **Para** | Validar que la estructura interna del árbol AVL es correcta según los criterios del laboratorio |
| **Requerimientos** | RF-06, RF-07 |
| **Prioridad** | Media |

**Criterios de aceptación:**
- Los recorridos preorden y postorden están disponibles como opciones separadas en el menú.
- Se imprime el orden de visita de los nodos en cada recorrido.

---

### HU-05 — Visualizar la jerarquía del árbol

| Campo | Detalle |
|---|---|
| **Rol** | Estudiante / desarrollador |
| **Quiero** | Visualizar la forma gráfica del árbol en consola |
| **Para** | Entender la estructura jerárquica y verificar que el balanceo se aplica correctamente |
| **Requerimientos** | RF-08 |
| **Prioridad** | Media |

**Criterios de aceptación:**
- El árbol se imprime con caracteres `┌──`, `└──`, `│` para mostrar jerarquía.
- La raíz aparece al centro-izquierda de la representación visual.

---

### HU-06 — Navegar el sistema mediante un menú

| Campo | Detalle |
|---|---|
| **Rol** | Usuario general |
| **Quiero** | Interactuar con el sistema mediante un menú numérico claro |
| **Para** | Usar el sistema sin necesidad de leer documentación técnica |
| **Requerimientos** | RF-10, RNF-02 |
| **Prioridad** | Alta |

**Criterios de aceptación:**
- El menú muestra 7 opciones numeradas.
- Las opciones inválidas muestran un mensaje de error y el menú se vuelve a mostrar sin cerrar el programa.

---

## Diagrama de flujo
<img width="1167" height="760" alt="image" src="https://github.com/user-attachments/assets/b4f5147a-0566-45ae-9a9f-8493b48a7840" />

---

## Diagrama casos de uso
<img width="690" height="503" alt="image" src="https://github.com/user-attachments/assets/2a6528ac-3e01-4f98-a5a2-d7a5177b49b9" />

---

## Diagrama de secuencia
<img width="730" height="686" alt="image" src="https://github.com/user-attachments/assets/a3ab6182-1620-48ef-ade4-484a35a48381" />
