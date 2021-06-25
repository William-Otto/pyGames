import os
import pygame
import sys
EXEC_DIR = os.path.dirname(__file__)

class Imagem(object):
    def __init__(self, imagem):

        self.word_image = os.path.join(EXEC_DIR, "images", imagem)
        self.imagem = imagem
        self.image = pygame.image.load(self.word_image)
        self.rect = self.image.get_rect()
        self.soletrando_palavra = self.imagem.split('.')[0]
        self.letters = list(self.soletrando_palavra)
        self.width = self.image.get_width()
        self.length = len(self.letters)
        
    def draw(self, screen, x, y):
        screen.blit(self.image, [x, y])
