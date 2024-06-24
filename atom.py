from interface import Draw                              # También se utilizará la interfaz
import math
import copy


class Atom:
    def __init__(self, pos, m, element):
        self.sta = pos                                  # Posición inicial, estática (static) sta
        self.mol = m                                    # Masa molar
        self.element = element                          # Elemento

        self.bonded = False                             # Posee enlace
        self.spring = 0                                 # Constante de resorte
        self.velocity = 0                               # Velocidad
        self.act = copy.deepcopy(self.sta)              # Posición dinámica (actual) act
        self.anchor = None                              # Ancla con otro objeto átomo
        self.d = 0                                      # Distancia entre dos átomos
        self.angle = 0                                  # Ángulo

    def draw(self, screen):
        Draw.atom(screen, self.act, 20, self.element)

    def sprivean(self, spring, velocity, anchor):       # Resorte-Velocidad-Ancla (SPRIng-VElocity-ANchor)
        self.spring = spring
        self.velocity = velocity
        self.anchor = anchor
        self.bonded = True                              # Notificar que tiene enlace y es el átomo en movimiento
        dx = self.anchor.act[0] - self.act[0]           # Distancia x
        dy = self.anchor.act[1] - self.act[1]           # Distancia y
        self.angle = math.atan(dy / dx)                 # Ángulo
        self.d = math.sqrt((dx ** 2) + (dy ** 2))       # Distancia entre los dos átomos

    def compute(self, time):
        dx = abs(self.anchor.sta[0] - self.sta[0])      # Distancia x
        dy = abs(self.anchor.sta[1] - self.sta[1])      # Distancia y
        if self.bonded:
            x = math.cos(self.angle) * (self.d - (math.sin(math.pi * time / 50) * 0.5)) - dx
            y = math.sin(self.angle) * (self.d - (math.sin(math.pi * time / 50) * 0.5)) - dy
            self.act = (x, y)
