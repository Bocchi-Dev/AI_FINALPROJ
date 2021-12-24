import sys
import pygame

pygame.init()

screen_width = 900
screen_height = 780

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pusod ni lanz")
bgcolor = (200, 200, 200)
level3bgImage = pygame.image.load("images/level3bg.png")
# screen.fill(bgcolor)
screen.blit(level3bgImage, (0, 0))

# Level 3 Enemy
enemy = pygame.image.load("images/enemyfire.png")
enemy2 = pygame.image.load("images/enemyfire.png")

enemyPosX = 350
enemyPosY = 350
level3EnemySpeed = 0.1
level3EnemySpeed2 = 0.2
goingLeft = True
goingRight = False
#enemy dimensions
enemy_size_X = 64
enemy_size_Y = 64
enemyPositions = [(166, 87), (256, 253), (529, 365), (804, 458),
                  (16, 586)]
enemyPosXList = [166, 256, 529, 804, 16]

#level3 goal
level3Goal = pygame.image.load("images/lvl3Goal.png")
level3GoalPosX = 807
level3GoalPosY = 618


#set platform dimensions
plat_size_X = 65
plat_size_Y = 65

#platform Images
prototypeImage = pygame.image.load('images/plat2.png')
level3Platform = pygame.image.load('images/l3plat6.png')
#insert image of platforms for each level

#bools for levels
isLevelPrototype = False
isLevelOne = False
isLevelTwo = False
isLevelThree = True

#level platform positions
prototypeLevelPlatformPos = [(10, 500), (100, 200), (300, 50), (500, 700)]
level3PlatformPos = [(782,94), (711, 94), (642, 94), (520, 134), (361, 134),
                     (241, 87), (26, 266), (177, 355), (255, 408), (325, 450),
                     (69, 483), (474, 545), (126, 659), (309, 686), (610, 649),
                     (805, 679), (831, 166)]
#insert list of platform positions for each level

class Player():
    def __init__(self, x, y):
        sprite = pygame.image.load('images/ice.png')
        self.image = pygame.transform.scale(sprite, (40, 40)) #maybe adjust player size later
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False

    def update(self):
        directionX = 0
        directionY = 0

        #get movement
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -10 #jump speed
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            directionX -= 2 #move speed
        if key[pygame.K_RIGHT]:
            directionX += 2

        #gravity
        self.vel_y += 0.40
        if self.vel_y > 10:
            self.vel_y = 10
        directionY += self.vel_y

        #check for collision with world
        for plat in currentLevel.platforms:
            if pygame.Rect.colliderect(plat.rect, self.rect): #check collision on x-axis
                # print("hit")
                directionX = 0
            if pygame.Rect.colliderect(plat.rect, self.rect): #check collision on y-axis
                if self.vel_y < 0: #check if fell on ground
                    directionY = plat.rect.bottom - self.rect.top
                    self.vel_y = 0
                elif self.vel_y >= 0: #check if hit ceiling
                    directionY = plat.rect.top - self.rect.bottom
                    self.vel_y = 0

        #update player location
        self.rect.x += directionX
        self.rect.y += directionY

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            directionY = 0

        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        screen.blit(self.image, self.rect)

class Platform():
    def __init__(self, platformLocation,  platformImage):
        self.platform = pygame.transform.scale(platformImage, (plat_size_X, plat_size_Y))
        self.rect = self.platform.get_rect()
        self.position = platformLocation
        self.rect.topleft = platformLocation

        #pygame.draw.rect(self.platform, (0, 0, 255), self.rect, 2)
        #screen.blit(self.platform, platformLocation)

class Enemy():
    def __init__(self, enemyPosition, enemyImage):
        self.enemy = pygame.transform.scale(enemyImage, (enemy_size_X, enemy_size_Y))
        self.rect = self.enemy.get_rect()
        self.position = enemyPosition
        self.rect.topleft = enemyPosition
        self.rect.x = enemyPosition(0)
        self.rect.y = enemyPosition(1)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.goingLeft = True
        self.goingRight = False

    def update(self):
        global enemyPosX
        # Detects if the enemy is going left
        if self.goingLeft:
            enemyPosX += level3EnemySpeed2
            screen.blit(enemy, (self.rect.x, self.rect.y))
            # Enemy stops at this position
            if (self.rect.x == self.position(0)):
                self.goingLeft = False
                self.goingRight = True

        # Detects if the enemy is going right
        if self.goingRight:
            enemyPosX -= level3EnemySpeed2
            screen.blit(enemy, (self.rect.x, self.rect.y))
            # Enemy stops at this position
            if (self.rect.x == (self.position(0) + 130)):
                self.goingLeft = True
                self.goingRight = False

        screen.blit(enemy, (self.rect.x, self.rect.y))


class Level():
    def __init__(self, platformLocations, platformImage, enemyLocations, enemyImage):
        self.enemyLocation_list = enemyLocations
        self.enemyImage = enemyImage
        self.platformLocation_list = platformLocations
        self.platformImage = platformImage
        self.platforms = []
        self.enemies = []

    def draw(self):
        for i in range(len(self.platformLocation_list)):
            platformToSpawn = Platform(self.platformLocation_list[i], self.platformImage)
            enemyToSpawn = Enemy(self.enemyLocation_list[i], self.enemyImage)
            self.platforms.append(platformToSpawn)
            self.enemies.append(enemyToSpawn)
            pygame.draw.rect(self.platforms[i].platform, (0, 255, 0), self.platforms[i].rect, 2)
            screen.blit(self.platforms[i].platform, self.platforms[i].position)



#Spawns the level 3 enemy
def spawnEnemylvl3():
    screen.blit(enemy, enemyPositions[0])
    screen.blit(enemy, enemyPositions[1])
    screen.blit(enemy, enemyPositions[2])
    screen.blit(enemy, enemyPositions[3])
    screen.blit(enemy, enemyPositions[4])


# Movement for the level 3 enemy
def enemyMovementlvl3(enemy, x, y):
    global enemyPosX
    global goingRight
    global goingLeft

    # Detects if the enemy is going left
    if goingLeft:
        enemyPosX += level3EnemySpeed2
        screen.blit(enemy, (x, y))
        # Enemy stops at this position
        if (enemyPosX == 480.99999999999255):
            goingLeft = False
            goingRight = True

    # Detects if the enemy is going right
    if goingRight:
        enemyPosX -= level3EnemySpeed2
        screen.blit(enemy, (x, y))
        # Enemy stops at this position
        if (enemyPosX == 350.59999999999997):
            goingLeft = True
            goingRight = False

    screen.blit(enemy, (x, y))



#Level 3 Goal
def level3GoalObject(x, y):
    screen.blit(level3Goal, (x, y))

# instantiating player and levels
player = Player(100, screen_height - 130)
level_Proto = Level(prototypeLevelPlatformPos, prototypeImage, enemyPositions, enemy)
level_Three = Level(level3PlatformPos, level3Platform, enemyPositions, enemy)
# insert other levels

currentLevel = level_Three# change to level one later

pygame.display.update()

enemyMovement = False

pygame.display.update()

continuePlay = True
while continuePlay:
    # screen.fill(bgcolor)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuePlay = False


    if isLevelPrototype:
        currentLevel = level_Proto

    if isLevelThree:
        screen.blit(level3bgImage, (0, 0))
        currentLevel = level_Three
        # Calls level 3 Goal
        #level3GoalObject(level3GoalPosX, level3GoalPosY)
        # Calls function to spawn enemy
        #spawnEnemylvl3()

        # Makes enemy movement true
        enemyMovement = True

        if enemyMovement:
            # Calls the enemy movement
            #enemyMovementlvl3(enemy, enemyPosX, enemyPosY)
            for enemy in currentLevel.enemies:
                enemy.update()


    player.update()



    #insert if levelOne, etc...
        #insert level_one.draw...

    currentLevel.draw()
    pygame.display.update()

pygame.quit()
sys.exit()

