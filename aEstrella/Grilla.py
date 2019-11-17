import numpy as np
import random

class grilla:
    def __init__(self, x, y,obstaculos):
        self.grilla = np.zeros((x, y))
        self.obstaculos = obstaculos
        self.x = x
        self.y = y
    def generarObstaculos(self):
        for i in range(0,self.obstaculos):
            x = random.randint(0,self.x-1)
            y = random.randint(0,self.y-1)
            if (self.grilla[x][y] != -1 and self.grilla[x][y] != -2 and self.grilla[x][y] != -3):
                self.grilla[x][y] = -1
    def insertarFlechas(self, linkedlist):
        currentNode = linkedlist.head
        while (currentNode != None):
            x = currentNode.value.head.value
            y = currentNode.value.head.nextNode.value
            flecha = currentNode.value.head.nextNode.nextNode.value
            if (flecha == 0):
                self.grilla[x][y] = -4
            elif (flecha == 1):
                self.grilla[x][y] = -5
            elif (flecha == 2):
                self.grilla[x][y] = -6
            else:
                self.grilla[x][y] = -7
            currentNode = currentNode.nextNode

    def mostrarGrilla(self):
        #print('\n' * 5)
        for a in range(0, self.x):
            print("\033[90m|", end=' ')
            for b in range(0, self.y):
                if (int(self.grilla[a][b]) == -2):
                    print("\033[95mA", end=' ')
                elif (int(self.grilla[a][b]) == -3):
                    print("\033[95mB\033[91m", end=' ')
                elif (int(self.grilla[a][b]) == -1):
                    print("\033[91m■\033[90m", end=' ')
                elif (int(self.grilla[a][b]) == -4):
                    print("\033[92m↑\033[90m", end=' ')
                elif (int(self.grilla[a][b]) == -5):
                    print("\033[92m↓\033[90m", end=' ')
                elif (int(self.grilla[a][b]) == -6):
                    print("\033[92m←\033[90m", end=' ')
                elif (int(self.grilla[a][b]) == -7):
                    print("\033[92m→\033[90m", end=' ')
                else:
                    print("\033[90m□\033[90m", end=' ')
            print("|")
