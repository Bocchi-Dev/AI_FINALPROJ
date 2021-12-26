import sys
import pygame
import random
import math

pygame.init()

screen_width = 900
screen_height = 780

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pusod ni lanz")
bgcolor = (200, 200, 200)

#BG Images
level1bgImage = pygame.image.load("images/level1bg.png")
level2bgImage = pygame.image.load("images/level2bg.png")
level3bgImage = pygame.image.load("images/level3bg.png")

# Level 2 Enemy
enemy = pygame.image.load("images/enemyfire.png")
enemy2 = pygame.image.load("images/enemyfire.png")

#enemy dimensions
enemy_size_X = 64
enemy_size_Y = 64

enemyPositions = [(500, 30), (200, 300), (600, 250), (529, 450), (200, 458),
                  (40, 560)]

#level 2 goal
level2Goal = pygame.image.load("images/lvl2Goal.png")
level2GoalPosX = 800
level2GoalPosY = 720

level3EnemyPositions = [(18, 127), (256, 253), (404, 371), (556, 460),
                  (16, 586)]

#level3 goal
level3Goal = pygame.image.load("images/lvl3Goal.png")
level3GoalPosX = 807
level3GoalPosY = 618
level3GoalPosition = [(807, 618)]


#set platform dimensions
plat_size_X = 100
plat_size_Y = 100

coin_size_X = 30
coin_size_Y = 30

#platform Images
prototypeImage = pygame.image.load('images/l2plat2.png')
level3Platform = pygame.image.load('images/l3plat6.png')
level1Platform = pygame.image.load('images/l1plat1.png')
level2Plaform = pygame.image.load('images/l2plat2.png')

#bools for levels
isLevelPrototype = False
isLevelOne = False
isLevelTwo = True
isLevelThree = False

prototypeLevelPlatformPos = [(10, 500), (100, 200), (300, 50), (500, 700)]

#insert list of platform positions for each level
Level1PlatformPos = [(200, 80), (320, 80), (440, 80), (-3, 250),
                             (150, 350), (270, 350), (750, 300), (630, 300),
                             (500, 500), (620, 500), (180, 620), (290, 620), (60, 620)]

level2PlatformPos = [(10, 130), (200, 250), (270, 250),
                             (500, 100),  (400, 180), (800, 250),
                             (730, 250), (70, 350), (180, 450),
                             (250, 450), (450, 450), (600, 350),
                             (700, 600), (630, 600),(560, 600),
                             (490, 600), (300, 700)]

level3PlatformPos = [(782,94), (711, 94), (642, 94), (520, 134), (361, 134),
                     (241, 87), (26, 266), (177, 355), (255, 408), (325, 450),
                     (69, 483), (474, 545), (126, 659), (309, 686), (610, 649),
                     (805, 679), (831, 166)]

#score
score = 0
font = pygame.font.SysFont('Arial', 32)
scoreX = 10
scoreY = 10

#coins
coinImage = pygame.image.load('images/coin.png')

level2CoinsPos = [(80, 590), (50, 230), (250, 50), (350, 50), (480, 50), (200, 590), (200, 320), (300, 320), (640, 270),
                          (640, 470), (550, 470), (500, 750), (550, 750), (600, 750), (650, 750)]

prototypeLevelCoinsPos = [(50, 500), (150, 200), (350, 50)]
level3CoinsPos = [(537, 86), (35, 214), (470, 310), (130, 609),
                  (732, 565), (389, 603)]

Coins = []

def set_Coins(coinLocations):
    global Coins
    for loc in coinLocations:
        Coins.append(pygame.Rect(loc[0], loc[1], coin_size_X, coin_size_Y))

def spawn_coins():
    global score
    #coins
    for c in Coins:
        screen.blit(coinImage, (c[0], c[1]))

    for c in Coins:
        if c.colliderect(player):
            Coins.remove(c)
            score += 1
            print(score)

def show_score(x, y):
    score_display = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_display, (x, y))

#Level 2 Goal
def level2GoalObject(x, y):
    screen.blit(level2Goal, (x, y))

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
        global score
        directionX = 0
        directionY = 0

        #get movement
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -20 #jump speed
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            directionX -= 7 #move speed
        if key[pygame.K_RIGHT]:
            directionX += 7

        #gravity
        self.vel_y += 2
        if self.vel_y > 10:
            self.vel_y = 10
        directionY += self.vel_y

        # collision with screen borders
        if self.rect.right >= screen_width:
            self.rect.x = 10
        if  self.rect.left <= 0:
            self.rect.x = screen_width - 50
        if self.rect.top <= 0:
            self.rect.y = screen_height
        if self.rect.bottom >= screen_height:
            self.rect.y = 0


        #check for collision with world
        collision_tolerance = 10
        for plat in currentLevel.platforms:
            if self.rect.colliderect(plat.rect):
                if abs(self.rect.left - plat.rect.right) < collision_tolerance and directionX < 0: #colliding on right of platform
                    directionX = 0
                if abs(self.rect.right - plat.rect.left) < collision_tolerance and directionX > 0: #colliding on left of platform
                    directionX = 0
                  # check collision on y-axis
                if self.vel_y <= 0 and abs(self.rect.top - plat.rect.bottom) < collision_tolerance: #check if hit ceiling
                    directionY = plat.rect.bottom - self.rect.top
                    self.vel_y = 0
                if self.vel_y >= 0 and self.rect.top < plat.rect.top: #check if fall on ground
                    print(self.vel_y)
                    self.rect.bottom = plat.rect.top

        #update player location
        self.rect.x += directionX
        self.rect.y += directionY

        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
        screen.blit(self.image, self.rect)

class Platform():
    def __init__(self, platformLocation,  platformImage):
        self.platform = pygame.transform.scale(platformImage, (plat_size_X, plat_size_Y))
        self.rect = self.platform.get_rect()
        self.position = platformLocation
        self.rect.topleft = platformLocation

class Enemy():
    def __init__(self, enemyPosition, enemyImage):
        self.enemy = pygame.transform.scale(enemyImage, (enemy_size_X, enemy_size_Y))
        self.rect = self.enemy.get_rect()
        self.position = enemyPosition
        self.rect.topleft = enemyPosition
        self.rect.x = enemyPosition[0]
        self.rect.y = enemyPosition[1]
        self.width = self.enemy.get_width()
        self.height = self.enemy.get_height()
        self.goingLeft = False
        self.goingRight = True
        self.enemySpeed = 2

    def update(self):
        global enemyPosX
        # Detects if the enemy is going left
        if self.goingLeft:
            self.rect.x -= self.enemySpeed
            screen.blit(self.enemy, (self.rect.x, self.rect.y))
            # Enemy stops at this position
            if (self.rect.x < self.position[0]):
                self.goingLeft = False
                self.goingRight = True

        # Detects if the enemy is going right
        if self.goingRight:
            self.rect.x += self.enemySpeed
            screen.blit(self.enemy, self.rect)
            # Enemy stops at this position
            if (self.rect.x > (self.position[0] + 130)):
                self.goingLeft = True
                self.goingRight = False

        screen.blit(self.enemy, self.rect)


class Level():
    def __init__(self, platformLocations, platformImage, enemyLocations, enemyImage, backgroundImage,
                 playerSpawn, coinLocations, goalObject, goalObjectSpawn):
        self.background = backgroundImage
        self.goalObject = pygame.transform.scale(goalObject, (64, 64))
        self.goalSpawn = goalObjectSpawn
        self.enemyLocation_list = enemyLocations
        self.enemyImage = enemyImage
        self.platformLocation_list = platformLocations
        self.platformImage = platformImage
        self.platforms = []
        self.enemies = []
        self.coinsPos = coinLocations
        player.rect.x = playerSpawn[0]
        player.rect.y = playerSpawn[1]
        set_Coins(coinLocations)

    def draw(self):
        screen.blit(self.background, (0, 0))
        screen.blit(self.goalObject, self.goalSpawn)
        for i in range(len(self.platformLocation_list)):
            platformToSpawn = Platform(self.platformLocation_list[i], self.platformImage)
            self.platforms.append(platformToSpawn)
            pygame.draw.rect(self.platforms[i].platform, (0, 255, 0), self.platforms[i].rect, 2)
            screen.blit(self.platforms[i].platform, self.platforms[i].position)
            screen.blit(self.platforms[i].platform, self.platforms[i].position)

        for i in range(len(self.enemyLocation_list)):
            enemyToSpawn = Enemy(self.enemyLocation_list[i], self.enemyImage)
            self.enemies.append(enemyToSpawn)
            self.enemies[i].update()


# instantiating player and levels
player = Player(100, screen_height - 130)

level_Proto = Level(prototypeLevelPlatformPos, prototypeImage, enemyPositions, enemy, level3bgImage,
                    (0, 0), prototypeLevelCoinsPos, level3Goal, (807, 618))
level_One = Level(Level1PlatformPos, level1Platform, enemyPositions, enemy, level1bgImage,
                    (100, 10), prototypeLevelCoinsPos, level3Goal, (807, 618))
level_Two = Level(level2PlatformPos, level2Plaform, enemyPositions, enemy, level2bgImage,
                  (90, 10), prototypeLevelCoinsPos, level2Goal, (800, 720))
level_Three = Level(level3PlatformPos, level3Platform, enemyPositions, enemy, level3bgImage,
                    (825, 31), prototypeLevelCoinsPos, level3Goal, (807, 618))

# insert other levels

currentLevel = level_Two


pygame.display.update()

continuePlay = True
while continuePlay:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuePlay = False

    if isLevelPrototype:
        currentLevel = level_Proto
    if isLevelThree:
        currentLevel = level_Three
    if isLevelOne:
        currentLevel = level_One
    if isLevelTwo:
        currentLevel = level_Two

    currentLevel.draw()
    player.update()
    spawn_coins()
    #display score
    show_score(scoreX, scoreY)

    pygame.display.update()


pygame.quit()
sys.exit()

