import sys, pygame, util
from pygame.locals import *
from carro import *
from roca import *
from random import *

SCREEN_WIDTH = 981
SCREEN_HEIGHT = 480
ICON_SIZE = 32


def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Vuela, Pega y Esquiva")
    background_image = util.cargar_imagen('imagenes/fondo.jpg');
    pierde_vida = util.cargar_sonido('sonidos/pierde_vida.wav')
    pygame.mouse.set_visible(False)
    heroe = Carro()
    villano = [Roca((500,40), 4),
               Roca((700, 150), 4),
               Roca((500, 220), 4),
               Roca((800, 300), 4),
               Roca((600, 350), 4),
               Roca((500, 400), 4)]

    while True:
        fuente = pygame.font.Font(None, 25)
        texto_puntos = fuente.render("Puntos: " + str(heroe.puntos), 1, (240, 240, 240))
        texto_vida = fuente.render("Daño: " + str(heroe.daño), 1, (240, 240, 240))
        heroe.update()
        for n in villano:
            n.update()

        for n in villano:
            if heroe.rect.colliderect(n.rect):
                heroe.image = heroe.imagenes[1]
                pierde_vida.play()
                if heroe.daño < 100:
                    heroe.daño = heroe.daño + 1
                    n.velocidad = 4
            elif heroe.rect.x == n.rect.x:
                heroe.puntos = heroe.puntos + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0, 0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_vida, (100, 410))
        screen.blit(texto_puntos, (100, 440))
        for n in villano:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(10)


if __name__ == '__main__':
    game()