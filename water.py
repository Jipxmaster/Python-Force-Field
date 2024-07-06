from atom import Atom
from print import Print
from mol import Simkit
from draw import Draw
import math


def dec(n):
    n = int(n * 10000) / 10000
    return n


class Water:
    def __init__(self):                                     # Crear los átomos con posición, peso atómico y elemento
        self.h_1 = Atom([0.7570, -0.5859], 1.008, "H")
        self.h_2 = Atom([-0.7570, -0.5859], 1.008, "H")
        self.o_1 = Atom([0, 0], 15.9994, "O")
        self.va = []                                        # Velocidad actual
        self.cm = []                                        # Centro de masa
        self.vang = 0

    def set_temperature(self, temp):                        # Establecer temperatura con resorte constante
        temp = Simkit.velocity(temp, 1.008)                 # Dar velocidad según temperatura
        temp = Simkit.distribute(temp, 2)                   # Variar velocidad según cantidad de átomos (2)
        self.h_1.sprivean(312.6463, temp[0], self.o_1)
        self.h_2.sprivean(312.6463, temp[1], self.o_1)

    def compute(self, time):                                # Calcular la posición de los átomos que tengan resorte
        # --- Centro de masa ---
        h1 = self.h_1.pos                                   # Posiciones de los átomos
        h2 = self.h_2.pos
        o1 = self.o_1.pos
        mh, mo = self.h_1.mol, self.o_1.mol                 # Pesos de los átomos
        a = (h1[0] * mh) + (h2[0] * mh) + (o1[0] * mo)
        b = mh + mh + mo
        x = a / b                                           # Centro de masa en X
        a = (h1[1] * mh) + (h2[1] * mh) + (o1[1] * mo)
        y = a / b                                           # Centro de masa en Y
        self.cm = [x, y]                                    # Posición centro de masa

        # --- Cálculo de siguiente posición ---
        self.h_1.compute(time, self.cm)                     # Calcular posición de hidrógenos
        self.h_2.compute(time, self.cm)
        x = (self.h_1.va[0] + self.h_2.va[0]) / 10**5       # Sumar velocidades en X (angstroms / fs)
        y = (self.h_1.va[1] + self.h_2.va[1]) / 10**5       # Sumar velocidades en Y (angstroms / fs)
        self.va = [x, y]
        self.o_1.move(self.va)                              # Mover molécula según velocidades

        # --- Rotación ---
        ang = (self.h_1.vrot + self.h_2.vrot) * 100         # Rotación exagerada por 100
        self.vang = dec(ang)
        self.h_1.angle += ang
        self.h_2.angle += ang

    def draw(self, screen):                                 # Dibujar todos los átomos
        self.h_1.draw(screen)
        self.h_2.draw(screen)
        self.o_1.draw(screen)
        Draw.atom(screen, self.cm, 10, "C")                 # Dibujar centro de masa de la molécula

    def info(self, screen):
        Print("H_1 x [m/s]: " + str(dec(self.h_1.va[0])), 0, screen)        # Velocidad hidrógeno 1
        Print("H_1 y [m/s]: " + str(dec(self.h_1.va[1])), 1, screen)

        Print("H_2 x [m/s]: " + str(dec(self.h_2.va[0])), 3, screen)        # Velocidad hidrógeno 2
        Print("H_2 y [m/s]: " + str(dec(self.h_2.va[1])), 4, screen)

        Print("X [Å/fs]: " + str(dec(self.va[0])), 6, screen)               # Velocidad total
        Print("Y [Å/fs]: " + str(dec(self.va[1])), 7, screen)

        Print("W [rad/fs]: " + str(self.vang), 9, screen)                   # Velocidad angular
