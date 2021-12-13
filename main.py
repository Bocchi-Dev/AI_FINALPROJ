import sys
import pygame

pygame.init()

screen_width = 600
screen_height = 780

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pusod ni lanz")
bgcolor = (200, 200, 200)
screen.fill(bgcolor)

#level platform positions
prototypeLevelPlatformPos = [(10, 500), (100, 200), (300, 50)]

class Player():
    def __init__(self, x, y):
        sprite = pygame.image.load('images/carrot.png')
        self.image = pygame.transform.scale(sprite, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):
        directionX = 0
        directionY = 0

        #get movement
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            directionX -= 5
        if key[pygame.K_RIGHT]:
            directionX += 5

        #gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        directionY += self.vel_y

        #check for collision

        #update player location
        self.rect.x += directionX
        self.rect.y += directionY

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            directionY = 0

        screen.blit(self.image, self.rect)

class Platform():
    def __init__(self, positionX, positionY, platformImage):
        self.positionX = positionX
        self.positionY = positionY
        self.platformImage = platformImage

class Level():
    def __init__(self, platformLocations, platformImage):
        self.platformLocation_list = []

        platform_img = platformImage

    def draw(self):
        for platform in self.platform_list:
            screen.blit((platform))

#def prototypeLevel():
 #   platform = pygame.image.load("images/plat2.png")
  #  platformList = [Platform(10, 500, platform), Platform(100, 200, platform), Platform(300, 50, platform)]
   # for i in range(len(platformList)):
    #    screen.blit(platformList[i].platformImage, (platformList[i].positionX, platformList[i].positionY))

player = Player(100, screen_height - 130)

continuePlay = True
while continuePlay:
    screen.fill(bgcolor)
    player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuePlay = False


    #prototypeLevel()
    pygame.display.update()

pygame.quit()
sys.exit()

