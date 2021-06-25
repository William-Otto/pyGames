import pygame
from pygame.locals import *
import os
import sys
from random import randint
EXEC_DIR = os.path.dirname(__file__)

class Carinha(pygame.sprite.Sprite):
    def __init__(self, type):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        carinha_path = os.path.join(EXEC_DIR, 'hit_or_fail')
        if self.type == 'hit':
            self.image = pygame.image.load(os.path.join(carinha_path,'hit.png'))
        elif self.type == 'fail':
            self.image = pygame.image.load(os.path.join(carinha_path, 'fail.png'))
        self.rect = self.image.get_rect()
        self.rect.topleft = [200, 300]
        self.lifespan = 15 
        
    def update(self):
        self.lifespan -= 1
        if self.type == 'hit':
            x, y = (randint(1,500), randint(1,500))
        else:
            x, y = [200, 300]
        self.rect.topleft = [x, y]
    
    def reset(self):
        self.lifespan = 25 