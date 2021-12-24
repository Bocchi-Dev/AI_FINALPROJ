import sys
import pygame

pygame.init()

screen_width = 900
screen_height = 780

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pusod ni lanz")
bgcolor = (200, 200, 200)
screen.fill(bgcolor)

#set platform dimensions
plat_size_X = 100
plat_size_Y = 100

coin_size_X = 30
coin_size_Y = 30

#platform Images
prototypeImage = pygame.image.load('images/plat2.png')
#insert image of platforms for each level


#bools for levels
isLevelPrototype = True
isLevelOne = False
isLevelTwo = False
isLevelThree = False

#level platform positions
prototypeLevelPlatformPos = [(10, 500), (100, 200), (300, 50), (500, 700)]
#insert list of platform positions for each level

#score
score = 0
font = pygame.font.SysFont('Arial', 32)
scoreX = 10
scoreY = 10

#coins
coinImage = pygame.image.load('images/coin.png')
prototypeLevelCoinsPos = [(50, 500), (150, 200), (350, 50)]
Coins = [

]

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

class Player():
    def __init__(self, x, y):
        sprite = pygame.image.load('images/carrot.png')
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
            self.vel_y = -10 #jump speed
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            directionX -= 2 #move speed
        if key[pygame.K_RIGHT]:
            directionX += 2

        #gravity
        self.vel_y += 0.15
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

class Level():
    def __init__(self, platformLocations, platformImage, playerSpawn, coinLocations):
        self.platformLocation_list = platformLocations
        self.platformImage = platformImage
        self.platforms = []
        self.coinsPos = coinLocations
        player.rect.x = playerSpawn[0]
        player.rect.y = playerSpawn[1]
        set_Coins(coinLocations)

    def draw(self):
        for i in range(len(self.platformLocation_list)):
            platformToSpawn = Platform(self.platformLocation_list[i], self.platformImage)
            self.platforms.append(platformToSpawn)
            pygame.draw.rect(self.platforms[i].platform, (0, 255, 0), self.platforms[i].rect, 2)
            screen.blit(self.platforms[i].platform, self.platforms[i].position)
            screen.blit(self.platforms[i].platform, self.platforms[i].position)

#instantiating player and levels
player = Player(100, screen_height - 130)
level_Proto = Level(prototypeLevelPlatformPos, prototypeImage, (100, 10), prototypeLevelCoinsPos)
#insert other levels

currentLevel = level_Proto #change to level one later

pygame.display.update()

continuePlay = True
while continuePlay:
    screen.fill(bgcolor)
    player.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuePlay = False


    #display score
    show_score(scoreX, scoreY)

    if isLevelPrototype:
        currentLevel = level_Proto
    #insert if levelOne, etc...
        #insert level_one.draw...
    spawn_coins()
    currentLevel.draw()
    pygame.display.update()

pygame.quit()
sys.exit()

