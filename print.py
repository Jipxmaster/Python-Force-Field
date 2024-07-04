import pygame


class Print:
    @staticmethod
    def __init__(text, line, screen):                           # Imprimir texto según línea y contenido
        font = pygame.font.Font('freesansbold.ttf', 20)         # Obtener la fuente
        text = font.render(text, True, "WHITE")                 # Fuente y color de la pantalla
        rect = text.get_rect()                                  # Obtener tamaño del texto en píxeles
        rect.center = (800 + (rect[2] / 2), 64 + (line * 32))   # Alinear a la izquierda, usando el tamaño del texto
        screen.blit(text, rect)                                 # Mostrar el texto
