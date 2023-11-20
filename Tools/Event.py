import pygame
pygame.init()

screen=pygame.display.set_mode((900,800))
GameNotOver=True



while GameNotOver:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            GameNotOver=False
    pygame.display.flip()
pygame.quit()




