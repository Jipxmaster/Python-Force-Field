from interface import Draw                              # También se utilizará la interfaz
import mol                                              # Para la constante de avogadro
import math                                             # Funciones trigonométricas
import copy                                             # Odio que python no copie completamente un arreglo


class Atom:
    def __init__(self, pos, m, element):
        self.sta = pos                                  # Posición inicial, estática (static) sta
        self.mol = m                                    # Masa molar
        self.element = element                          # Elemento

        self.bonded = False                             # Posee enlace
        self.k = 0                                      # Constante de resorte
        self.v0 = 0                                     # Velocidad inicial
        self.act = copy.deepcopy(self.sta)              # Posición dinámica (actual) act
        self.anchor = None                              # Ancla con otro objeto átomo
        self.d = 0                                      # Distancia entre dos átomos
        self.angle = 0                                  # Ángulo

        self.a = 0                                      # Amplitud
        self.w = 0                                      # Velocidad angular (ANgular Velocity)

        self.va = 0                                     # Velocidad actual

    def draw(self, screen):                             # Simplemente muestra la coordenada actual
        if self.bonded:                                 # Crear enlace si el valor bonded es verdadero
            Draw.bond(screen, self.act, self.anchor)
        Draw.atom(screen, self.act, 40, self.element)   # Dibujar átomo de todas maneras

    def sprivean(self, spring, velocity, anchor):       # Resorte-Velocidad-Ancla (SPRIng-VElocity-ANchor)
        self.k = spring                                 # Resorte
        self.v0 = velocity                              # Velocidad
        self.anchor = anchor.sta                        # Ancla
        self.bonded = True                              # Notificar que tiene enlace y es el átomo en movimiento

        dx = self.anchor[0] - self.act[0]               # Distancia x
        dy = self.anchor[1] - self.act[1]               # Distancia y
        self.d = math.sqrt((dx ** 2) + (dy ** 2))       # Distancia entre los dos átomos

        # Obtención de los ángulos
        if dx < 0:                                      # Si distancia x es negativo
            self.angle = math.atan(dy / dx)
        elif dx > 0:                                    # Si distancia x es positivo
            self.angle = math.atan(dy / dx) + mol.pi
        elif dx == 0 and dy < 0:                        # Si distancia x = 0 y distancia y negativo
            self.angle = mol.pi/2
        elif dx == 0 and dy > 0:                        # Si distancia x = 0 y distancia y positivo
            self.angle = (3 * mol.pi) / 2

        self.w = math.sqrt(self.k/(self.mol/mol.avg))   # Obtención de velocidad angular
        self.a = (self.v0 / self.w)

    def compute(self, time):
        if self.bonded:                                 # Solo funcionará si tiene los parámetros de enlace
            a = self.a * (10 ** 10)
            w_mod = self.w / (5 * (10**13))             # 20 femtosegundos por fotograma
            x = math.cos(self.angle) * (self.d - (math.sin(w_mod * time) * a))
            y = math.sin(self.angle) * (self.d - (math.sin(w_mod * time) * a))
            self.va = - self.w * self.a * math.cos(w_mod * time)
            self.act = (x, y)
