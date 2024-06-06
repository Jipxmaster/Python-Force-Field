import pygame


class Screen:
    @staticmethod
    # Para dibujar la rejilla de líneas blancas
    def grill(screen):
        res = [640, 480]
        size = 80
        cx = int(res[0] / size)
        cy = int(res[1] / size)
        # bucles para dibujar las rayas
        while cx != 0:
            pygame.draw.line(screen, (255, 255, 255), (cx * size, 0), (cx * size, res[1]))
            cx -= 1
        while cy != 0:
            pygame.draw.line(screen, (255, 255, 255), (0, cy * size), (res[0], cy * size))
            cy -= 1
    # Para dibujar la partícula o molécula

    @staticmethod
    def draw(screen, pos, color):
        # La resolución se divide en dos para obtener el centro de la pantalla
        # de ahí alterar con las coordenadas del plano cartesiano
        res = [640, 480]
        size = 80  # tamaño de los cuadros
        dot_size = 20  # tamaño del punto
        position = (res[0]/2 + (pos[0] * size * 2), res[1]/2 - (pos[1] * size * 2))
        pygame.draw.circle(screen, color, position, dot_size)
