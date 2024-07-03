import pygame                           # Querido pygame
from draw import Draw              # Todo lo relacionado a la interfaz
from water import Water

res = (1024, 768)                       # Tamaño de ventana
render_res = (768, 768)                 # Tamaño de simulación

pygame.init()                           # Inicialización de pygame
screen = pygame.display.set_mode(res)   # Colocar resolución
clock = pygame.time.Clock()             # Objeto reloj
time = 0                                # Tiempo de simulación (fotogramas transcurridos)
running = True

# ---- V A R I A B L E S   I N I C I A L E S ----

water = Water()                         # Crear la variable agua

water.set_temperature(298)              # Calentar el agua

while running:
    for event in pygame.event.get():    # Revisar eventos
        if event.type == pygame.QUIT:   # Salir del bucle principal al quitar la ventana
            running = False

    # ---- E M P I E Z A   L A   M A G I A ----
    # -----------------------------------------
    if time == 999999:                      # Cambiar la posición de los átomos
        water.o_1.pos = (-1, -3)
        water.h_1.pos = (-2, -2)
        water.h_2.pos = (0, -2)
        water.set_temperature(273)      # Reasignar algunas variables internas

    screen.fill((0, 0, 0))              # Vaciar la pantalla con color negro

    Draw.grill(screen, render_res, 150)

    water.compute(time)                 # Calcular la siguiente posición del agua
    water.draw(screen)                  # Dibujar la molécula de agua
    water.info(screen)                  # Imprimir información de la molécula

    # -----------------------------------------
    # ---- T E R M I N A   L A   M A G I A ----

    pygame.display.flip()               # Cambio de buffer
    clock.tick(60)                       # 50 Hz, sesgo europeo. Más fácil de calcular el tiempo de simulación
    time += 1

pygame.quit()                           # Cerrar pygame y terminar el programa
