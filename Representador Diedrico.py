import pygame

pygame.init()

ANCHO, ALTO = 1200, 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Representador Diédrico 2 Vistas")

BLANCO, NEGRO, ROJO, AZUL, VERDE, MORADO, GRIS = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 0, 255), (0, 255, 0), (150, 0, 150), (200, 200, 200)
FUENTE = pygame.font.SysFont(None, 20)

CUADROS = 10
ESPACIO_X, ESPACIO_Y = ANCHO // (CUADROS * 2), ALTO // CUADROS
centro_x1, centro_x2, centro_y = ANCHO * 0.25, ANCHO * 0.75, ALTO * 0.5

coords = [("A", 0, 2, 4), ("B", 1, 3, 1), ("C", -2, -1, 2), ("D", 2, 1, -1)]

def dibujar_cuadricula():
    for i in range(0, ANCHO, ESPACIO_X):
        pygame.draw.line(VENTANA, GRIS, (i, 0), (i, ALTO))
    for j in range(0, ALTO, ESPACIO_Y):
        pygame.draw.line(VENTANA, GRIS, (0, j), (ANCHO, j))
    pygame.draw.line(VENTANA, NEGRO, (0, centro_y), (ANCHO, centro_y), 2)
    pygame.draw.line(VENTANA, NEGRO, (centro_x2, 0), (centro_x2, ALTO), 2)
    pygame.draw.circle(VENTANA, ROJO, (centro_x1, centro_y), 6)
    pygame.draw.circle(VENTANA, ROJO, (centro_x2, centro_y), 6)
    pygame.draw.line(VENTANA, NEGRO, (ANCHO * 0.5, 0), (ANCHO * 0.5, ALTO), 4)

def vista_diedrica(coordenadas):
    for n, x, y, z in coordenadas:
        px, py1, py2 = centro_x1 + x * ESPACIO_X, centro_y + y * ESPACIO_Y, centro_y + (-z) * ESPACIO_Y
        if (px, py1) == (px, py2):
            pygame.draw.circle(VENTANA, MORADO, (px, py1), 6)
            VENTANA.blit(FUENTE.render(f"{n}12", True, MORADO), (px + 8, py1 - 8))
        else:
            pygame.draw.line(VENTANA, NEGRO, (px, py1), (px, py2), 1)
            pygame.draw.circle(VENTANA, AZUL, (px, py1), 5)
            pygame.draw.circle(VENTANA, VERDE, (px, py2), 5)
            VENTANA.blit(FUENTE.render(f"{n}1", True, AZUL), (px + 8, py1 - 8))
            VENTANA.blit(FUENTE.render(f"{n}2", True, VERDE), (px + 8, py2 - 8))

def vista_yz(coordenadas):
    for n, _, y, z in coordenadas:
        px, py = centro_x2 + y * ESPACIO_X, centro_y - z * ESPACIO_Y
        pygame.draw.circle(VENTANA, AZUL, (px, py), 6)
        VENTANA.blit(FUENTE.render(n, True, AZUL), (px + 8, py - 8))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit()
    VENTANA.fill(BLANCO)
    dibujar_cuadricula()
    vista_diedrica(coords)
    vista_yz(coords)
    pygame.display.flip()
