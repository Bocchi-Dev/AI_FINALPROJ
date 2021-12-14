import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 780))
pygame.display.set_caption("Pusod ni lanz")
bgcolor = (200, 200, 200)
screen.fill(bgcolor)
continuePlay = True


# Plaforms
platform = pygame.image.load("images/plat2.png")

platPosX = 370
platPosY = 480

platformPos = [(460, 132), (430, 147), (293, 156), (163, 229), (61, 326), (255, 311),
               (166, 427), (262, 531), (413, 524), (493, 681), (356, 686), (209, 687)]

# Player


# Level 3 Enemy
enemy = pygame.image.load("images/enemyfire.png")
enemyPosX = 100
enemyPosY = 350
level3EnemySpeed = 0.1
goingLeft = True
goingRight = False

#Spawns the level 3 enemy
def spawnEnemylvl3(x, y):
    screen.blit(enemy, (x, y))

#Movement for the level 3 enemy
def enemyMovementlvl3(enemy, x, y):
    global enemyPosX
    global goingRight
    global goingLeft

    # Detects if the enemy is going left
    if goingLeft:
        enemyPosX += level3EnemySpeed
        screen.blit(enemy, (x, y))
        # Enemy stops at this position
        if (enemyPosX == 194.39999999999463):
            goingLeft = False
            goingRight = True

    # Detects if the enemy is going right
    if goingRight:
        enemyPosX -= level3EnemySpeed
        screen.blit(enemy, (x, y))
        # Enemy stops at this position
        if (enemyPosX == 83.40000000000094):
            goingLeft = True
            goingRight = False

    screen.blit(enemy, (x, y))

def plat_position(x, y):
    screen.blit(platform, (x, y))

pygame.display.update()

enemyMovement = False

while continuePlay:
    screen.fill(bgcolor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuePlay = False

    # Calls spawn enemy
    spawnEnemylvl3(enemyPosX, enemyPosY)

    # Makes enemy movement true
    enemyMovement = True

    # Calls the enemy movement
    if enemyMovement:
        enemyMovementlvl3(enemy, enemyPosX, enemyPosY)

    plat_position(platPosX, platPosY)
    pygame.display.update()

pygame.quit()
sys.exit()

