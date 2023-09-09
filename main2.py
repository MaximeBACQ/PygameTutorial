import pygame
from sys import exit
from random import randint

def displayScore(obstacleList,score):
        for obstacle in obstacleList:
            if obstacle.x == 40:
                score += 1

        scoreSurface = testFont.render(f'Cramptes: {score}', False, (64,64,64))
        scoreRectangle = scoreSurface.get_rect(center = (400,50))
        screen.blit(scoreSurface,scoreRectangle)
        return score
        

# def displayScore():
#     currentTime = int(pygame.time.get_ticks()/1000 - startTime)
#     scoreSurface = testFont.render(f'Cramptes: {currentTime}', False, (64,64,64))
#     scoreRectangle = scoreSurface.get_rect(center = (400,50))
#     screen.blit(scoreSurface,scoreRectangle)
#     return currentTime
    
def obstacleMovement(obstacleList):
    if(obstacleList):
        for obstacleRectangle in obstacleList:
            obstacleRectangle.x -= 5

            if obstacleRectangle.bottom == 300:
                screen.blit(snailSurface,obstacleRectangle)
            else:
                screen.blit(flySurface,obstacleRectangle)

        obstacleList = [obstacle for obstacle in obstacleList if obstacle.x>-100]
        return obstacleList
    else:
        return []
    
def collisions(player,obstacles): 
    if obstacles:
        for obstacleRectangle in obstacles  :
            if player.colliderect(obstacleRectangle):
                return False
    return True
 
pygame.init()

active = True

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Cramptés')
clock = pygame.time.Clock()
testFont = pygame.font.Font('font/Pixeltype.ttf',50)
startTime = 0
score = 0

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

# scoreSurface = testFont.render("Cramptes Geants", False, (64,64,64))
# scoreRectangle = scoreSurface.get_rect(center = (400,50))

# Obstacles
snailSurface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
flySurface = pygame.image.load('graphics/Fly/fly1.png').convert_alpha()

obstacleRectList = []

playerStandSurface = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
playerStandSurfaceScaled = pygame.transform.scale2x(playerStandSurface)
playerStandRectangleScaled = playerStandSurfaceScaled.get_rect(center = (400,200))

playerSurface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
playerRectangle = playerSurface.get_rect(midbottom = (80,300))
playerGravity = 0

gameName = testFont.render('Crampti Game', False, (111,196,169))
gameNameRectangle = gameName.get_rect(center=(400,80))

gameOverSurface = testFont.render("Game over", False, (0,255,255))
gameOverRectangle = gameOverSurface.get_rect(center = (400,50))

gameMessage = testFont.render('Press space to run', False, (0,255,255))
gameMessageRectangle = gameMessage.get_rect(center = (400,350))

#Timer
obstacleTimer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacleTimer,1400)

while True:#game loop infinie, dessiner tous les éléments, ensuite tout update
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            exit() #on call exit plutôt que break, break ne terminerait que le if 
        if active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playerRectangle.collidepoint(event.pos) and playerRectangle.bottom>=300:
                    playerGravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and playerRectangle.bottom>=300:
                    playerGravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                startTime = pygame.time.get_ticks()/1000
                active = True
        if event.type == obstacleTimer and active:
            if randint(0,2):
                obstacleRectList.append(snailSurface.get_rect(bottomright = (randint(900,1100),300)))
            else:
                obstacleRectList.append(flySurface.get_rect(bottomright = (randint(900,1100),200)))


    if active:
        screen.blit(sky,(0,0))
        screen.blit(ground,(0,300))
        # pygame.draw.rect(screen,'#c0e8ec',scoreRectangle)
        # pygame.draw.rect(screen,'#c0e8ec',scoreRectangle,5)

        # screen.blit(scoreSurface,scoreRectangle)
        #score = displayScore()

        #Player
        playerGravity += 1
        playerRectangle.top += playerGravity
        if(playerRectangle.bottom>=300):
            playerRectangle.bottom=300
        screen.blit(playerSurface,playerRectangle)

        #obstacle movement
        obstacleRectList = obstacleMovement(obstacleRectList)

        print(score)
        score = displayScore(obstacleRectList,score)
        print(score)

        # collision
        active = collisions(playerRectangle,obstacleRectList)
    else:
        obstacleRectList.clear()
        playerRectangle.y=300
        playerGravity = 0

        screen.fill((176,196,222))
        screen.blit(gameOverSurface,gameOverRectangle)

        if score == 0 :
            screen.blit(gameName,gameNameRectangle)
        else:
            scoreMessage = testFont.render(f'Your score: {score}', False, (111,196,169))
            scoreMessageRectangle = scoreMessage.get_rect(center = (400,80))
            screen.blit(scoreMessage,scoreMessageRectangle)
        

        screen.blit(playerStandSurfaceScaled,playerStandRectangleScaled)

        screen.blit(gameMessage,gameMessageRectangle)



        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')
        # if playerRectangle.colliderect(snailRectangle): # return 0 ou 1 (0 = pas collision, 1 = collision), après test ça return en fait false ou true
        #     print('collision')

        # mousePosition = pygame.mouse.get_pos()
        # if(playerRectangle.collidepoint(mousePosition)):
        #     print(pygame.mouse.get_pressed()) 

        #game loop infinie, dessiner tous les éléments
        #update all

    pygame.display.update() #fait l'update de l'écran à chaque début du loop
    clock.tick(60)#set le framerate maximum


