import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 780))
pygame.display.set_caption("Pusod ni lanz")
bgcolor = (200, 200, 200)
screen.fill(bgcolor)
continuePlay = True

platform = pygame.image.load("images/plat2.png")
platPosX = 370
platPosY = 480

def plat_position(x, y):
    screen.blit(platform, (x, y))

while continuePlay:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuePlay = False


    plat_position(platPosX, platPosY)
    pygame.display.update()

pygame.quit()
sys.exit()

