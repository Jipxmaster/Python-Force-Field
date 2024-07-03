from atom import Atom
from print import Print
from mol import Simkit


class Water:
    def __init__(self):                                     # Crear los átomos con posición, peso atómico y elemento
        self.h_1 = Atom((0.7569503273, -0.5858822766), 1.008, "H")
        self.h_2 = Atom((-0.7569503273, -0.5858822766), 1.008, "H")
        self.o_1 = Atom((0, 0), 15.9994, "O")

    def set_temperature(self, temp):                        # Establecer temperatura con resorte constante
        temp = Simkit.velocity(temp, 1.008)
        temp = Simkit.distribute(temp, 2)
        self.h_1.sprivean(312.6463, temp[0], self.o_1)
        self.h_2.sprivean(312.6463, temp[1], self.o_1)

    def compute(self, time):                                # Calcular la posición de los átomos que tengan resorte
        self.h_1.compute(time)
        self.h_2.compute(time)

    def draw(self, screen):                                 # Dibujar todos los átomos
        self.h_1.draw(screen)
        self.h_2.draw(screen)
        self.o_1.draw(screen)

    def info(self, screen):
        Print("Velocidades [m/s]", 0, screen)                       # Velocidades
        Print("Hidrógeno izquierdo", 2, screen)
        Print("V[sta] = " + str(self.h_1.v0), 3, screen)
        Print("V[act] = " + str(int(self.h_1.va)), 4, screen)

        Print("Hidrógeno derecho", 6, screen)
        Print("V[sta] = " + str(self.h_2.v0), 7, screen)
        Print("V[act] = " + str(int(self.h_2.va)), 8, screen)

        Print("H_1 amplitude: " + str(self.h_1.a), 10, screen)    # Posición de ancla en angstroms
        Print("H_2 amplitude: " + str(self.h_2.a), 11, screen)

        Print("H_1 distance: " + str(self.h_1.d), 13, screen)       # Distancia de enlace en angstroms
        Print("H_2 distance: " + str(self.h_2.d), 14, screen)

        Print("H_1 angle: " + str(self.h_1.angle), 16, screen)      # Ángulo de enlace en radianes
        Print("H_2 angle: " + str(self.h_2.angle), 17, screen)
