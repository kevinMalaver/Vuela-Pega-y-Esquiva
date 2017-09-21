import pygame
from pygame.sprite import Sprite
from pygame import *
import util
from random import *


class Roca(Sprite):
    def __init__(self, coord, vel):
        Sprite.__init__(self)
        self.image = util.cargar_imagen('imagenes/Piedra.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(coord[0], coord[1])
        self.dir = "l"
        self.velocidad = vel

    def update(self):
        teclas2 = pygame.key.get_pressed()
        if self.dir == "l":
            self.rect.x -= self.velocidad
            if self.rect.x <= 40:
                self.rect.x = randint(940,980)
                self.rect.y = randint(40,440)
        if teclas2[K_LEFT] and self.velocidad>1:
            self.velocidad = self.velocidad-1
        elif teclas2[K_RIGHT] and self.velocidad<=10:
            self.velocidad = self.velocidad+1