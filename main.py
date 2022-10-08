import pygame, math
import time as tm

pygame.display.init()                                                               

screenDimension = int(pygame.display.Info().current_w * 0.5)                        
win = pygame.display.set_mode((screenDimension, screenDimension))
pygame.display.set_caption("Studies With Shaq")
pygame.font.init()    

def windowdisplay():
    img = pygame.image.load('display.png')
    win.blit(img, (0, screenDimension * 0.2))

def refresh():
    win.fill([255, 255, 255])

main = True
while main:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            main = False

    refresh()
    pygame.display.update()
