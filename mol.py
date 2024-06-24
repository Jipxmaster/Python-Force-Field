k = 1.380649 * (10 ** -23)                              # Constante de Boltzmann
pi = 3.1415926535897932384626                           # Número pi
avg = 6.02214129 * (10 ** 23)                           # Número de avogadro
seed = 15                                               # Semilla para números aleatorios


def dmb(t, m, option):                                  # Distribución de Maxwell-Boltzmann (DMB)
    if option == 1:                                     # Opción 1: Velocidad más probable (VMS)
        v = (2 * k * t) / m
    elif option == 2:                                   # Opción 2: Velocidad media (VM)
        v = (8 * k * t) / (pi * m)
    else:                                               # Sin selección: Media cuadrátiva de velocidad (VMD)
        v = (3 * k * t) / m
    return v ** 0.5                                     # Terminar la ecuación con una raíz


def gnp(a):                                             # Generador de números pseudoaleatorios (GNP) [0-255]
    global seed
    a = a ^ (a << 13)                                   # Método XORSHIFT
    a = a ^ (a >> 17)                                   # Desplaza n bits a cualquiera de los dos lados, luego
    a = a ^ (a << 5)                                    # opera XOR con el resultado anterior
    seed = a                                            # Actualizar variable seed
    a = (a & 511) >> 1                                  # Seleccionar los bits (1 - 8)
    return a                                            # Retorna la siguiente iteración


def gvi(v, q):                                          # Generador de velocidades individuales (GVI)
    velocities = []
    for i in range(q):                                  # Generar q (quantity) veces
        rnd = gnp(seed)                                 # Iterar GNP
        vel = v + ((v * 0.1) / 128) * (128 - rnd)       # Alterar v (velocidad) con valor aleatorio
        velocities.append(vel)                          # Añadir el resultado
    return velocities                                   # Retornar un arreglo de resultados


class Simkit:                                           # Clase SimKit: Utiliza las funciones definidas anteriormente
    @classmethod
    def random(cls):                                    # Generar números aleatorios
        return gnp(seed)

    @classmethod
    def distribute(cls, velocity, quantity):            # Generar variaciones de una velocidad determinada
        return gvi(velocity, quantity)

    @staticmethod
    def velocity(temp, part, sele=1):                   # Generar velocidad con distribuciób de Maxwell-Boltzmann
        return dmb(temp, part, sele)
