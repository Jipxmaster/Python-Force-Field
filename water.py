from atom import Atom
from print import Print
from mol import Simkit


def dec(n):
    n = int(n * 10000) / 10000
    return n


class Water:
    def __init__(self):                                     # Crear los átomos con posición, peso atómico y elemento
        self.h_1 = Atom([0.7570, -0.5859], 1.008, "H")
        self.h_2 = Atom([-0.7570, -0.5859], 1.008, "H")
        self.o_1 = Atom([0, 0], 15.9994, "O")
        self.va = []                                        # Es una herramienta sorpresa que nos ayudará más tarde

    def set_temperature(self, temp):                        # Establecer temperatura con resorte constante
        temp = Simkit.velocity(temp, 1.008)                 # Dar velocidad según temperatura
        temp = Simkit.distribute(temp, 2)                   # Variar velocidad según cantidad de átomos (2)
        self.h_1.sprivean(312.6463, temp[0], self.o_1)
        self.h_2.sprivean(312.6463, temp[1], self.o_1)

    def compute(self, time):                                # Calcular la posición de los átomos que tengan resorte
        self.h_1.compute(time)
        self.h_2.compute(time)
        x = (self.h_1.va[0] + self.h_2.va[0]) / 10**5       # Sumar velocidades en X (angstroms / fs)
        y = (self.h_1.va[1] + self.h_2.va[1]) / 10**5       # Sumar velocidades en Y (angstroms / fs)
        self.va = [x, y]
        self.o_1.move(self.va)                              # Mover molécula según velocidades

    def draw(self, screen):                                 # Dibujar todos los átomos
        self.h_1.draw(screen)
        self.h_2.draw(screen)
        self.o_1.draw(screen)

    def info(self, screen):
        Print("H_1 x [m/s]: " + str(dec(self.h_1.va[0])), 0, screen)        # Velocidad hidrógeno 1
        Print("H_1 y [m/s]: " + str(dec(self.h_1.va[1])), 1, screen)

        Print("H_2 x [m/s]: " + str(dec(self.h_2.va[0])), 3, screen)        # Velocidad hidrógeno 2
        Print("H_2 y [m/s]: " + str(dec(self.h_2.va[1])), 4, screen)

        Print("X [Å/fs]: " + str(dec(self.va[0])), 6, screen)               # Velocidad total
        Print("Y [Å/fs]: " + str(dec(self.va[1])), 7, screen)
