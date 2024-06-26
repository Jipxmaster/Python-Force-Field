import pygame                           # Querido pygame
from interface import Draw              # Todo lo relacionado a la interfaz
from interface import Print
from atom import Atom                   # Clase átomo
import math                             # Funciones

res = (1024, 768)                       # Pantalla
render_res = (768, 768)                 # Renderizado

pygame.init()                           # Inicialización de pygame
screen = pygame.display.set_mode(res)   # Colocar resolución
clock = pygame.time.Clock()             # Objeto reloj
time = 0                                # Tiempo de simulación (fotogramas transcurridos)
running = True

# ---- V A R I A B L E S   I N I C I A L E S ----
h_1 = Atom((0.7568, -0.3936), 1.008, "H")
h_2 = Atom((-0.7568, -0.3936), 1.008, "H")
o_1 = Atom((0, 0), 15.9994, "O")
h_1.sprivean(312.6463, 200, o_1)
h_2.sprivean(312.6463, 200, o_1)
linea1 = Print("RESULTADOS", (896, 32))

while running:
    for event in pygame.event.get():    # Revisar eventos
        if event.type == pygame.QUIT:   # Salir del bucle principal al quitar la ventana
            running = False

    screen.fill((0, 0, 0))              # Vaciar la pantalla con color negro

    # ---- E M P I E Z A   L A   M A G I A ----
    # -----------------------------------------
    Draw.grill(screen, render_res, 250)

    h_1.compute(time)                   # Calcular posiciones de los átomos de hidrógeno
    h_2.compute(time)

    linea2 = Print("H. IZQ.", (896, 64))
    linea3 = Print("V0 = " + str(h_1.v0), (896, 96))
    linea4 = Print("V = " + str(int(h_1.va)), (896, 128))

    linea5 = Print("H. DER.", (896, 192))
    linea6 = Print("V0 = " + str(h_2.v0), (896, 224))
    linea7 = Print("V = " + str(int(h_2.va)), (896, 256))

    h_1.draw(screen)                    # Mostrar todos los átomos
    h_2.draw(screen)
    o_1.draw(screen)

    linea1.print(screen)
    linea2.print(screen)
    linea3.print(screen)
    linea4.print(screen)
    linea5.print(screen)
    linea6.print(screen)
    linea7.print(screen)

    #print(h_1.v0, h_1.va * math.cos(h_1.angle), h_1.va * math.sin(h_1.angle))

    # -----------------------------------------
    # ---- T E R M I N A   L A   M A G I A ----

    pygame.display.flip()               # Cambio de buffer
    clock.tick(50)                      # 50 Hz, sesgo europeo. Más fácil de calcular el tiempo de simulación
    time += 1

pygame.quit()                           # Cerrar pygame y terminar el programa
