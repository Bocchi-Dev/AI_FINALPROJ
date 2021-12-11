import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((601, 999.5))
pygame.display.set_caption("Pusod ni lanz")
bgcolor = (200, 200, 200)
screen.fill(bgcolor)
continuePlay = True


while continuePlay:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuePlay = False

pygame.display.update()

pygame.quit()
sys.exit()

