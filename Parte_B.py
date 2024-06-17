k = 1.380649 * (10 ** -23)                              # Constante de Boltzmann
pi = 3.1415926535897932384626                           # Número pi
avg = 6.02214129 * (10 ** 23)                           # Número de avogadro
h = 1.00794                                             # Masa molar del hidrógeno
o = 15.9994                                             # Masa molar del oxígeno
temp = 273                                              # Temperatura del sistema


def dmb(t, m, option):                                  # Distribución de Maxwell-Boltzmann (DMB)
    if option == 1:                                     # Opción 1: Velocidad más probable (VMS)
        v = (2 * k * t) / m
    elif option == 2:                                   # Opción 2: Velocidad media (VM)
        v = (8 * k * t) / (pi * m)
    else:                                               # Sin selección: Media cuadrátiva de velocidad (VMD)
        v = (3 * k * t) / m
    return v ** 0.5                                     # Terminar la ecuación con una raíz


def gnp(a):                                             # Generador de números pseudoaleatorios (GNP)
    a = a ^ (a << 13)                                   # Método XORSHIFT
    a = a ^ (a >> 17)                                   # Desplaza n bits a cualquiera de los dos lados, luego
    a = a ^ (a << 5)                                    # opera XOR con el resultado anterior
    return a                                            # Retorna la siguiente iteración


def gvi(vc, q, sem):                                    # Generador de velocidades individuales (GVI)
    velocities = []
    for i in range(q):                                  # Generar q (quantity) veces
        sem = gnp(sem)                                  # Iterar GNP
        rnd = (sem & 512) >> 1                          # Obtener número a partir de bit 1 a bit 8
        vel = vc + ((vc * 0.1) / 128) * (128 - rnd)     # Sumar vc (velocidad centro) con un el número generado
        velocities.append(vel)                          # Añadir el resultado
    return velocities                                   # Retornar un arreglo de resultados


v_w = dmb(temp, (2 * h + o)/avg, 1)                     # VMS del agua

velocidades = gvi(v_w, 4, 15)
print(velocidades)

