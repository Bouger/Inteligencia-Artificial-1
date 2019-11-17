# Ejercicio A* - Inteligencia Artificial I

Implementar un agente basado en objetivos que dado un punto de inicio y un punto destino, encuentre el camino óptimo.

• *Las acciones posibles del agente son: (arriba, abajo, izquierda, derecha).*

• *El agente deberá ser capaz de resolver el problema planteado mediante un algoritmo de búsqueda A**.

Proponer una heurística admisible y consistente para el problema.

## Cálculo de Heuristica
Por cada posibilidad ortogonal la función a calcular será **C = 1 + H**, donde **H = |Bx-Ax| +|By-Ay|**

Siendo **A = (x,y)** (cada nodo vecino) y **B = (x,y)** las representaciones de sus posiciones.
# Ejemplos

Grilla de **20x20** con **100** muros con **A** en **[0,0]** y **B** en **[16,18]**

![alt text](https://i.gyazo.com/a72e5ce6f0ad92126d2a4f60bd341fec.png)

Grilla de **50x50** con **500** muros con **A** en **[0,0]** y **B** en **[36,40]**

![alt text](https://i.gyazo.com/1a1673fbc2b427265e58ea95f5932146.png)

Grilla de **100x100** con **2500** muros con **A** en **[0,0]** y **B** en **[65,72]**


![alt text](https://i.gyazo.com/44498bc8f888eaa8860787323b4b3456.png)



## Detalles

A la hora de poner muchos obstáculos, el algoritmo entra en un bucle sin salida el cual no he podido solucionar.