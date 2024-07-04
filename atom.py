from draw import Draw                                   # También se utilizará la interfaz
import mol                                              # Para la constante de avogadro
import math                                             # Funciones trigonométricas
import copy                                             # Copiar idéntico


class Atom:
    def __init__(self, pos, m, element):
        self.pos0 = copy.deepcopy(pos)
        self.pos = pos                                  # Posición inicial, estática (static) sta
        self.mol = m                                    # Masa molar
        self.element = element                          # Elemento

        self.bonded = False                             # Posee enlace
        self.v0 = 0                                     # Velocidad inicial
        self.anchor = None                              # Ancla con otro objeto átomo
        self.d = 0                                      # Distancia entre dos átomos
        self.angle = 0                                  # Ángulo

        self.a = 0                                      # Amplitud
        self.w = 0                                      # Velocidad angular (ANgular Velocity)

        self.va = 0                                     # Velocidad actual

    def draw(self, screen):                             # Simplemente muestra la coordenada actual
        if self.bonded:                                 # Crear enlace si el valor bonded es verdadero
            Draw.bond(screen, self.pos, self.anchor)
        Draw.atom(screen, self.pos, 40, self.element)   # Dibujar átomo de todas maneras

    def sprivean(self, spring, velocity, anchor):       # Resorte-Velocidad-Ancla (SPRIng-VElocity-ANchor)
        self.v0 = velocity                              # Velocidad
        self.anchor = anchor.pos                        # Ancla
        self.bonded = True                              # Notificar que tiene enlace y es el átomo en movimiento

        dx = anchor.pos[0] - self.pos[0]                # Distancia x
        dy = anchor.pos[1] - self.pos[1]                # Distancia y
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

        self.w = math.sqrt(spring/(self.mol/(mol.avg * 1000)))  # Obtención de velocidad angular
        self.a = (self.v0 / self.w)

    def compute(self, time):
        if self.bonded:                                 # Solo funcionará si tiene los parámetros de enlace
            a = self.a * (10 ** 10)                     # Amplitud en angstroms
            w_mod = self.w / (10**15)                   # 1 femtosegundos por fotograma
            x = math.cos(self.angle) * (self.d - (math.sin(w_mod * time) * a)) + self.anchor[0]
            y = math.sin(self.angle) * (self.d - (math.sin(w_mod * time) * a)) + self.anchor[1]
            self.pos = [x, y]                           # Posición de los átomos en movimiento
            v = - self.w * self.a * math.cos(w_mod * time)
            x = math.cos(self.angle) * v                # Velocidad descompuesta en X
            y = math.sin(self.angle) * v                # Velocidad descompuesta en Y
            self.va = [x, y]                            # Velocidad del átomo

    def move(self, pos):                                # Mover átomo. Solo se usará para mover el hidrógeno
        self.pos[0] += pos[0]
        self.pos[1] += pos[1]
