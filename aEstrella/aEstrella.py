import linkedlist

class aEstrella:
    def __init__(self, grilla, agent):
        self.grilla = grilla
        self.agent = agent
        #print("A = [",self.agent.posicionX,"][",self.agent.posicionY,"]")
        self.grilla.grilla[agent.posicionX][agent.posicionY] = -2
        self.grilla.grilla[agent.objetivoPosicionX][agent.objetivoPosicionY] = -3
        self.grilla.generarObstaculos()
        self.grilla.mostrarGrilla()
        self.caminoHecho = linkedlist.LinkedList()
        self.comenzarCamino()

    def calculoheuristica(self):
        for i in range(0, len(self.agent.decisiones)):

            if (i == 0):
                # Chequeamos que el calculo sea posible. Es decir, que el nodo pertenezca a la grilla y que además, no sea un obstáculo.

                if ((self.agent.posicionX -1) >= 0 and
                        self.grilla.grilla[self.agent.posicionX - 1][self.agent.posicionY] != -1):
                    self.agent.decisiones[i] = 1 + abs(self.agent.objetivoPosicionX - (self.agent.posicionX - 1) + abs(
                        self.agent.objetivoPosicionY - self.agent.posicionY))
                else:
                    self.agent.decisiones[i] = -1
                    continue
            elif (i == 1):
                if ((self.agent.posicionX + 1) <= self.grilla.x-1 and
                        self.grilla.grilla[self.agent.posicionX + 1][self.agent.posicionY] != -1):
                    self.agent.decisiones[i] = 1 + abs(self.agent.objetivoPosicionX - (self.agent.posicionX + 1)) + abs(
                        self.agent.objetivoPosicionY - self.agent.posicionY)
                else:
                    self.agent.decisiones[i] = -1
                    continue
            elif (i == 2):
                if ((self.agent.posicionY - 1) >= 0 and
                        self.grilla.grilla[self.agent.posicionX][self.agent.posicionY - 1] != -1):
                    self.agent.decisiones[i] = 1 + abs(self.agent.objetivoPosicionX - self.agent.posicionX) + abs(
                        self.agent.objetivoPosicionY - (self.agent.posicionY - 1))
                else:
                    self.agent.decisiones[i] = -1
                    continue
            else:
                if ((self.agent.posicionY + 1) <= self.grilla.y-1 and
                        self.grilla.grilla[self.agent.posicionX][self.agent.posicionY + 1] != -1):
                    self.agent.decisiones[i] = 1 + abs(self.agent.objetivoPosicionX - self.agent.posicionX) + abs(
                        self.agent.objetivoPosicionY - (self.agent.posicionY + 1))
                else:
                    self.agent.decisiones[i] = -1
                    continue
    def mejorCamino(self):
        menorValor = 0
        ultimaPosicion = -555 # En caso de que se necesite ir a la ultima posición, se la guarda.
        seEncontroComparacion = False
        seEncontroPosicion = False
        for i in range(0, len(self.agent.decisiones)):
            if (self.agent.decisiones[i] != -1):
                if (self.agent.ultimaPosicion != i):
                    #print("Empezando por ",i)
                    menorValor = i
                    seEncontroComparacion = True
                    break
                else:
                    ultimaPosicion = i
        if (seEncontroComparacion == False):
            menorValor = ultimaPosicion
        for i in range(menorValor + 1, len(self.agent.decisiones)):
            if (self.agent.decisiones[i] < self.agent.decisiones[menorValor] and self.agent.decisiones[i] != -1):
                if (self.agent.ultimaPosicion != i):
                     menorValor = i
                     seEncontroPosicion = True
                else:
                     #print("Guardando ultimaposicion: ", i)
                     ultimaPosicion = i
        if (seEncontroPosicion == False):
            if (seEncontroComparacion == False):
                #print("Se necesita la ultima posicion: ", i, ", reemplazando: ", menorValor)
                menorValor = ultimaPosicion


        self.guardarUltimaUbicacion(menorValor)
        if (menorValor == 0):
            #print("arriba", " menorvalor: " , menorValor)
            self.agent.posicionX = self.agent.posicionX - 1
        elif (menorValor == 1):
           # print("abajo", " menorvalor: " , menorValor)
            self.agent.posicionX = self.agent.posicionX + 1
        elif (menorValor == 2):
            #print("izq", " menorvalor: " , menorValor)
            self.agent.posicionY = self.agent.posicionY - 1
        else:
           # print("der" , " menorvalor: " , menorValor)
            self.agent.posicionY = self.agent.posicionY + 1


        # Las siguientes LinkedList son utilizadas para guardar las posiciones donde debe mostrarse una flecha por donde pasa el Agente.
        L = linkedlist.LinkedList()
        newNode = linkedlist.Node()
        newNode.value = self.agent.posicionX
        L.head = newNode
        newNode2 = linkedlist.Node()
        newNode2.value = self.agent.posicionY
        L.head.nextNode = newNode2
        newNode3 = linkedlist.Node()
        newNode3.value = menorValor
        L.head.nextNode.nextNode = newNode3
        linkedlist.add(self.caminoHecho,L)
    def guardarUltimaUbicacion(self,valor):
        ''' 0 = arriba, 1 = abajo, 2 = izquierda, 3 = derecha '''
        # Si el el valor es por ejemplo 0 (que significa "arriba"), hay que guardar el opuesto (abajo)
        if (valor == 0):
            self.agent.ultimaPosicion = 1
        elif (valor == 1):
            self.agent.ultimaPosicion = 0
        elif (valor == 2):
            self.agent.ultimaPosicion = 3
        else:
            self.agent.ultimaPosicion = 2


    def comenzarCamino(self):
        print("\033[0m")
        print("Generando caminos...")
        while (
                self.agent.posicionX != self.agent.objetivoPosicionX or self.agent.posicionY != self.agent.objetivoPosicionY):
            self.calculoheuristica()
            self.mejorCamino()

            #print("[", self.agent.posicionX, "][", self.agent.posicionY, "]")
        print("El agente ha llegado a la posición deseada")
        self.grilla.insertarFlechas(self.caminoHecho)
        self.grilla.grilla[self.agent.objetivoPosicionX][self.agent.objetivoPosicionY] = -3
        self.grilla.mostrarGrilla()

