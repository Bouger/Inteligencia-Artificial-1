import Grilla
import Agent
import aEstrella

# Los primeros 2 parámetros representan el tamaño de la grilla, el tercer parámetro es al cantidad de obstaculos a generar
grilla = Grilla.grilla(50,50, 500)
# Los primeros 2 parámetros representan las coordenas X e Y respectivamente del Agente A y los 2 parámetros restantes de la posición B a llegar.
agent = Agent.agent(0, 0, 36, 37)
x = aEstrella.aEstrella(grilla, agent)
