import sys
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((600, 780))
pygame.display.set_caption("Pusod ni lanz")
bgcolor = (200, 200, 200)
continuePlay = True

#character
character = pygame.image.load("images/plat2.png")
charPosX = 300
charPosY = 100
charXChange = 0
charYChange = 0
dx, dy = 0
distance = 0

#Enemy
enemy = pygame.image.load("images/plat2.png")
enemyPosX = 300
enemyPosY = 600

#platform
platform = pygame.image.load("images/plat2.png")
platPosX = 370
platPosY = 480

def character_position(x, y):
    screen.blit(character, (x, y))

def enemy_position(x, y):
    screen.blit(enemy, (x, y))

def plat_position(x, y):
    screen.blit(platform, (x, y))

def Follow_player(x, y):
    distance = (math.hypot(x - charPosX, y - charPosY))
    angle_radians = (math.atan2(y - charPosY, enemyPosX - charPosX))

    y += math.sin(angle_radians)*0.5
    x += math.cos(angle_radians)*0.5



while continuePlay:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuePlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                charYChange -= 1
            elif event.key == pygame.K_DOWN:
                charYChange += 1
            elif event.key == pygame.K_LEFT:
                charXChange -= 1
            elif event.key == pygame.K_RIGHT:
                charXChange += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or pygame.K_DOWN:
                charYChange = 0
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                charXChange = 0
    charPosY += charYChange
    charPosX += charXChange
    if charPosX <= 0:
        charPosX = 0
    elif charPosX >= 480:
        charPosX = 480
    if charPosY <= 0:
        charPosY = 0
    elif charPosY >= 660:
        charPosY = 660

    radians = math.atan2(charPosY-enemyPosY, charPosX-enemyPosX)
    distance = math.hypot(charPosX-enemyPosX, charPosY-enemyPosY)
    distance = int(distance)

    character_position(charPosX, charPosY)
    enemy_position(enemyPosX, enemyPosY)
    plat_position(platPosX, platPosY)
    Follow_player(enemyPosX, enemyPosY)
    pygame.display.update()

pygame.quit()
sys.exit()

