# Aspirador - Inteligencia Artificial I



## Ejercicios C y D
Desempe�o del Agente no aleatorio:
 
![alt text](https://i.gyazo.com/3b69684bd734707b504cd7423de1e7ee.png)

Desempe�o del Agente Aleatorio:
 
![alt text](https://i.gyazo.com/50acf8d8534c929657ab9db6e336010e.png)

# Ejercicio E
## 2.9)
### Considere una versi�n modificada del entorno de la aspiradora del Ejercicio 2.7, en el que se penalice al agente con un punto en cada movimiento.

#### a) �Puede un agente reactivo simple ser perfectamente racional en este medio? Expl�quese.

Si el agente no conoce el entorno, no lo creo, ya que un agente reactivo simple no guarda estados anteriores por lo que no podr�a saber por ejemplo, si est� en una esquina,ya que para saberlo deber�a chocarse con dos lados y nunca sabr� si se choco con un lado anteriormente, ya que no guarda estados, solo reacciona. En caso de que el agente sepa las proporciones del entorno puede saber donde est� parado y seguir distintas direcciones.

#### b) �Qu� suceder�a con un agente reactivo con estado? Dise�e este agente.

Al tener un estado, podr�a saber perfectamente si se encuentra en una esquina, por lo que se podr�a generar un camino. Hay que llevar al agente hasta la esquina superior izquierda, cuando choque con alguna pared (lo guarda como estado) , y luego se choque con otra, es decir, la pared de arriba y la pared de la izquierda, significa que se encuentra en una esquina. Luego empieza a recorrer en filas hasta llegar a la esquina inferior derecha.

#### c) �C�mo se responder�an las preguntas a y b si las percepciones proporcionan al agente informaci�n sobre el nivel de suciedad/limpieza de todas las cuadr�culas del entorno?

En el primer caso simplemente har�a el camino por cada slot sucio sin problemas.
El segundo caso ser�a el mismo o podr�a ser m�s eficiente dependiendo de donde aparezca la suciedad.

## 2.10)
### Considere una versi�n modificada del entorno de la aspiradora del Ejercicio 2.7, en el que la geograf�a del entorno (su extensi�n, l�mites, y obst�culos) sea desconocida, as� como, la disposici�n inicial de la suciedad. (El agente puede ir hacia arriba, abajo, as� como, hacia la derecha y a la izquierda.)

#### a) �Puede un agente reactivo simple ser perfectamente racional en este medio? Expl�quese.

No lo creo, como dije en el punto 2.9) a) , si desconoce el entorno, es dif�cil saber qu� camino tomar�.

#### b) �Puede un agente reactivo simple con una funci�n de agente aleatoria superar a un agente reactivo simple? Dise�e un agente de este tipo y medir su rendimiento en varios medios.

Dependiendo del tama�o, en matrices sumamente peque�as, el agente aleatorio puede tener ventaja.

#### c) �Se puede dise�ar un entorno en el que el agente con la funci�n aleatoria obtenga una actuaci�n muy pobre? Muestre los resultados.

Si, los entornos muy grandes pueden provocar rendimientos pobres, en un entorno de 128x128 con un porcentaje de 10% de suciedad, la aspiradora tiene un 0.026% de rendimiento (etapas/puntos).

#### d) �Puede un agente reactivo con estado mejorar los resultados de un agente reactivo simple? Dise�e un agente de este tipo y medir su eficiencia en distintos medios. �Se puede dise�ar un agente racional de este tipo?

Yo creo que en �ste caso, lograr�a los mismos resultados.

