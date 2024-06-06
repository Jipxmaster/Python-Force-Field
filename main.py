import pygame
import molecule
import math

# pygame setup, no es muy relevante
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
counter = 0

while running:
    # Events in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # All screen modifications happens here, vacía la pantalla
    screen.fill((0, 0, 0))
    molecule.Screen.grill(screen)

    # Cálculo de posición de los hidrógenos (utilizando valores arbitrarios)
    # Está basado en tiempo "counter"
    x = math.sin(52.26 * (math.pi / 180)) * (0.9572 - (math.sin(counter / 10) * 0.3) - 0.3)
    y = math.cos(52.26 * (math.pi / 180)) * (0.9572 - (math.sin(counter / 10) * 0.3) - 0.3)

    # Dibujo de los átomos
    molecule.Screen.draw(screen, (0, 0), (255, 0, 0))  # Oxygen
    molecule.Screen.draw(screen, (-x, -y), (255, 255, 255))  # Hydrogen
    molecule.Screen.draw(screen, (x, -y), (255, 255, 255))  # Hydrogen

    # Flip frame and frame limiter, aplica los cambios del dibujado
    pygame.display.flip()
    clock.tick(60)
    counter += 1  # Incrementar el tiempo "counter"

# End of program
pygame.quit()
