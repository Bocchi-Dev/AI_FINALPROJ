import sys
import pygame

pygame.init()

screen_width = 600
screen_height = 780

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pusod ni lanz")
bgcolor = (200, 200, 200)
screen.fill(bgcolor)

#set platform dimensions
plat_size_X = 128
plat_size_Y = 128

#platform Images
#level 1 platforms
prototypeImage = pygame.image.load('images/l1plat1.png')

#bools for levels
isLevelPrototype = True
isLevelOne = False
isLevelTwo = False
isLevelThree = False

#insert list of platform positions for each level
prototypeLevelPlatformPos = [(200, 80), (320, 80), (440, 80),
                             (-3, 250), (150, 350), (270, 350),
                             (475, 480), (180, 620), (290, 620), (60, 620)]



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

        #check for collision with world
        for plat in currentLevel.platforms:
            if pygame.Rect.colliderect(plat.rect, self.rect): #check collision on x-axis
                print("hit")
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

class Level():
    def __init__(self, platformLocations, platformImage):
        self.platformLocation_list = platformLocations
        self.platformImage = platformImage
        self.platforms = []

    def draw(self):
        for i in range(len(self.platformLocation_list)):
            platformToSpawn = Platform(self.platformLocation_list[i], self.platformImage)
            self.platforms.append(platformToSpawn)
            pygame.draw.rect(self.platforms[i].platform, (0, 255, 0), self.platforms[i].rect, 2)
            screen.blit(self.platforms[i].platform, self.platforms[i].position)

#instantiating player and levels
player = Player(100, screen_height - 130)
level_Proto = Level(prototypeLevelPlatformPos, prototypeImage)

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

    if isLevelPrototype:
        currentLevel = level_Proto

    #insert if levelOne, etc...
        #insert level_one.draw...

    currentLevel.draw()
    pygame.display.update()

pygame.quit()
sys.exit()

