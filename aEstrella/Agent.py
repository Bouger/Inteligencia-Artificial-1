from numpy import array


class agent:
    def __init__(self, posicionX, posicionY, objetivoPosicionX, objetivoPosicionY):
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.objetivoPosicionX = objetivoPosicionX
        self.objetivoPosicionY = objetivoPosicionY
        self.decisiones = array([1, 1, 1, 1])
        self.ultimaPosicion = 0
    # Arreglo que representa los posibles movimientos con valor, donde para
    # cada valor = heuristica + Esfuerzo. [0,0,0,0]
    # Donde cada slot representa en orden: [arriba,abajo,izquierda,derecha]
