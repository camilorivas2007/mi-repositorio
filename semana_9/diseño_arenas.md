## DISEÑO ARENAS 
Se presentara el diseño de las arenas asiganadas, para ver el paso a paso por medio de un diagrama de flujo cada proceso y explicacion del codigo, adjuntando un video. 

## TREE 
Trata de calcular la altura de un árbol binario, es decir, el número de aristas desde la raíz hasta la hoja más lejana, el ejercicio da un árbol ya construido y se pide completar una función que retorne esa altura como un número entero, por ejemplo, un árbol con un solo nodo tiene altura 0 porque no hay aristas .

Por cada nodo se calcula la altura del subárbol izquierdo y derecho, y se queda con la mayor. 
altura = 1 + max(altura izquierda, altura derecha)

El caso base es cuando el nodo no existe, donde normalmente se retorna -1. 

Portanto, la función recorre todo el árbol y encuentra el camino más largo desde la raíz hasta una hoja.
# DIAGRAMA DE FLUJO

<img width="582" height="799" alt="image" src="https://github.com/user-attachments/assets/a164313b-3ade-447b-842c-09778d5af521" />


## BINARY SERCH TREE

Consiste en encontrar el (LCA) de dos nodos dentro de un árbol binario de búsqueda. 
se debe identificar el nodo más profundo del árbol que tenga a ambos valores como descendientes. 
Por ejemplo, si buscas dos nodos en el árbol, su LCA será el punto donde sus caminos desde la raíz se “unen” por última vez.

Aprovechamos la propiedad clave de los árboles binarios de búsqueda (BST): 
los valores menores van a la izquierda y los mayores a la derecha. Entonces, se empieza desde la raíz y se compara:
# DIAGRMA DE FLUJO

<img width="490" height="753" alt="image" src="https://github.com/user-attachments/assets/6b9f566f-2826-47d4-9eb9-50c69a4bc0d1" />

## IS THIS BINARY SERCH TREE?

Se debe analizar si para cada nodo se cumple que todos los valores del subárbol izquierdo son menores que él, y todos los del subárbol derecho son mayores. La función debe recibir la raíz del árbol y devolver true o false dependiendo de si el árbol cumple o no estas reglas.

la solución correcta usa recursión con límites, a cada nodo le pasas un valor mínimo y máximo permitido. Si el valor del nodo está fuera de ese rango, no es BST. 
Por tanto, para el subárbol izquierdo se utiliza el máximo, y para el derecho el mínimo.

# DIAGRAMA DE FLUJO
<img width="581" height="830" alt="image" src="https://github.com/user-attachments/assets/9470582b-c14b-4db3-996e-2dd1b9d7fb5c" />












