from pygame import draw                                     # Solo se utilizará la función dibujar

elements = {"H": "WHITE", "O": "RED"}                       # Colores según átomo
resolution = []                                             # Resolución por definir
sq = 0                                                      # Tamaño de cuadrado "square size" (sq)


class Draw:
    @classmethod
    def grill(cls, screen, res, size):                      # Dibujar la matriz
        global resolution
        global sq
        sq = size                                           # Actualizar tamaño de cuadrado
        resolution = res                                    # Actualizar resolución
        c = "WHITE"                                         # Color de la matriz
        w = res[0]                                          # Ancho de pantalla
        h = res[1]                                          # Altura de pantalla
        x = int(res[0]/2)                                   # Mitad de ancho
        y = int(res[1]/2)                                   # Mitad de altura

        a = int(x/size)                                     # Máximo de iteraciones para las líneas horizontales
        for i in range(0, a + 1):                           # Dibujar desde el centro y luego desviarse
            b = size * i                                    # Desviación
            draw.line(screen, c, (x + b, 0), (x + b, h))
            draw.line(screen, c, (x - b, 0), (x - b, h))

        a = int(y/size)                                     # Máximo de iteraciones para las líneas verticales
        for i in range(0, a + 1):                           # Dibujar desde el centro y desviarse nuevamente
            b = size * i                                    # Desviación
            draw.line(screen, c, (0, y + b), (w, y + b))
            draw.line(screen, c, (0, y - b), (w, y - b))

    @staticmethod
    def atom(screen, pos, dot_size, element):               # Dibujar átomo
        color = elements[element.upper()]                   # Obtención de color
        x = int(resolution[0] / 2) + (pos[0] * sq)          # Coordenadas cartesianas a pantallas
        y = int(resolution[1] / 2) - (pos[1] * sq)          # Muy importante la resta
        draw.circle(screen, color, (x, y), dot_size)        # Finalmente el dibujo
