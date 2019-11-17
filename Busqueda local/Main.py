import random
import AlgoritmosGeneticos
import HillClimbing
import SimulatedAnnealing


# En n se establece la cantidad de reinas para cada algoritmo
n =10
valores = {}
# En el arreglo se tiene que igualar la cantidad de 0s con n, ejemplo: Si hay 8 reinas, se pondrán 8 ceros.
arreglo = [0,0,0,0,0,0,0,0,0,0]

# Algoritmo que genera aleatoriedad en el arreglo para ser posteriormente manipulado por los distintos algoritmos.
for i in range(0,n):
    aleatorio = random.randint(0, n-1)
    if (aleatorio in valores.values()):
        while (True):
            if (aleatorio in valores.values()):
                aleatorio = random.randint(0, n-1)
            else:
                arreglo[i] = aleatorio
                valores[i] = aleatorio
                break
    else:
        arreglo[i] = aleatorio
        valores[i] = aleatorio
print("Para el arreglo: ",arreglo)

# Descomentar la linea dependiendo del algoritmo a utilizar:

# Algoritmos Genéticos
# AlgoritmosGeneticos.AlgoritmosGeneticos(arreglo)

# SimulatedAnnealing
# SimulatedAnnealing.SimulatedAnnealing(arreglo)

# Hill Climbing
# HillClimbing.HillClimbing(arreglo)




