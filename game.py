import os
import pygame
from pygame.locals import *
from pygame.color import THECOLORS
from imagens import Imagem 
import random
import sys
from carinhas import Carinha

EXEC_DIR = os.path.dirname(__file__)  

images = os.walk(os.path.join(EXEC_DIR, "images"))

pygame.init()
pygame.display.set_caption("IMED Soletrando")

# Configs
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.SysFont('Helvetica', 50)
relogio = pygame.time.Clock()
lista_imagens = []
certo = False
errado = False
texto_inserido = []
screen_x, screen_y = screen.get_size()

for root, dir, files in images:
    for file in files:
        if '.DS_Store' not in file:
            lista_imagens.append(file)

teclas_ignoradas = ('escape', 'return', 'backspace', 'enter', 'space', 'right shift'\
                ,'left shift', 'left meta', 'right meta', 'f1', 'f2', 'f3', 'f4', 'f5'\
                ,'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'caps lock')

feliz = Carinha('hit')
triste = Carinha('fail')

feliz_group = pygame.sprite.GroupSingle()
triste_group = pygame.sprite.GroupSingle()

hifen = False

palavra = Imagem(random.choice(lista_imagens))

# Main
def main():
   
    global palavra
    global texto_inserido
    global teclas_ignoradas
    global errado
    global certo
    global hifen
    
    running = True
    pygame.key.set_repeat(0,0)
    while running:
        cursor = 0
        posição_letra = dict()
        chave = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        screen.fill(THECOLORS['white'])
        palavra.draw(screen, (screen_x/2 - palavra.width/2), 50)

        numero_linhas = len(palavra.letters)  
        underline_width = 40                     
        text_total_width = (numero_linhas * underline_width) + ((numero_linhas - 1) * 20) 
        line_x1 = screen_x/2 - text_total_width/2
        
        letter_beginning_list = []
        
        letter_beginning = screen_x/2 - text_total_width/2
        
        vermelho = (255, 10, 10)
        branco = (255, 255, 255)
        
        palavras_chave = range(0, palavra.length)
        

        for letter in palavra.letters:
            letter_size = font.size(letter)

            letter_beginning_list.append([letter_beginning + (underline_width/2 - letter_size[0]/2), letter])
            correct_letter = font.render(letter, 1, (255, 10, 10))
            letter_size = font.size(letter)                        
            if letter == "-":
                screen.blit(correct_letter, [letter_beginning + (underline_width/2 - letter_size[0]/2), 400])             
            letter_beginning += underline_width + 20 
            
           
            line_x2 = line_x1 + underline_width 
            pygame.draw.line(screen, THECOLORS['black'], (line_x1, 460), (line_x2, 460), 2)
            line_x1 += underline_width + 20 
            line_x2 += underline_width + 20 
        

        letter_dict = dict(zip(palavras_chave, letter_beginning_list))
        
        
        if triste.lifespan == 0:
            triste_group.empty()
            errado = False
        triste_group.update()
        
        if feliz.lifespan == 0:
            feliz_group.empty()
            certo = False
            palavra = Imagem(random.choice(lista_imagens))
            feliz.reset()
        feliz_group.update()
        
        if certo:
            relogio.tick(10)
            feliz_group.draw(screen)
            texto_inserido = []
        if errado:
            relogio.tick(10)
            triste_group.draw(screen)
            texto_inserido = []

        if chave[pygame.K_ESCAPE]:
            sys.exit()
        elif (mods & KMOD_META):
            if chave[pygame.K_q]:
                sys.exit()
        if hifen:
            texto_inserido.append('-')
            hifen = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    sys.exit()
                
            if event.type == pygame.KEYDOWN:
                key_value = pygame.key.name(event.key)
                if key_value == 'backspace':
                    if texto_inserido:
                        texto_inserido.pop()

                if key_value not in teclas_ignoradas:
                    texto_inserido.append(key_value)
                    print(texto_inserido)
                
                if key_value == 'return':
                    hyphen_pos = [i for i,x in enumerate(palavra.letters) if x == '-']
                    print(hyphen_pos)
                    if hyphen_pos:
                        del(palavra.letters[int(hyphen_pos[0])])

                    if texto_inserido == palavra.letters:
                        feliz_group.add(feliz)
                        certo = True
                    else:
                        triste.reset()
                        triste_group.add(triste)
                        errado = True
       
        
        # Renderizar palavras digitadas na tela
        for letter in texto_inserido:                                          
            if not letter == 'backspace':
                if letter_dict.get(cursor)[1] == '-':
                    cursor += 1

                correct_letter = font.render(letter, 1, (255, 10, 10))
                letter_size = font.size(letter)                        
                screen.blit(correct_letter, [letter_dict.get(cursor)[0], 400])             
                cursor += 1
        
        pygame.display.update()                                              
        relogio.tick(15)
        
if __name__ == "__main__":
    main()

