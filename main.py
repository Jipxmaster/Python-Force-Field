import pygame                           # Querido pygame
from interface import Draw              # Todo lo relacionado a la interfaz
from atom import Atom                   # Clase átomo

res = (640, 480)                        # Resolución de pantalla

pygame.init()                           # Inicialización de pygame
screen = pygame.display.set_mode(res)   # Colocar resolución
clock = pygame.time.Clock()             # Objeto reloj
running = True

# ---- V A R I A B L E S   I N I C I A L E S ----
h_1 = Atom((-2, -1), 1.0008, "H")
h_2 = Atom((0, 0), 1.0008, "O")
h_1.sprivean(200, 50, h_2)
time = 0

while running:
    for event in pygame.event.get():    # Revisar eventos
        if event.type == pygame.QUIT:   # Salir del bucle principal al quitar la ventana
            running = False

    screen.fill((0, 0, 0))              # Vaciar la pantalla con color negro

    # ---- E M P I E Z A   L A   M A G I A ----
    # -----------------------------------------
    Draw.grill(screen, res, 40)

    h_1.compute(time)

    h_1.draw(screen)
    h_2.draw(screen)

    # -----------------------------------------
    # ---- T E R M I N A   L A   M A G I A ----

    pygame.display.flip()               # Cambio de buffer
    clock.tick(50)                      # 50 Hz hace más fácil el cálculo de tiempos
    time += 1

pygame.quit()                           # Cerrar pygame y terminar el programa
