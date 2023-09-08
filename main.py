import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Cramptés')
clock = pygame.time.Clock()
testFont = pygame.font.Font('font/Pixeltype.ttf',50)

sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()

scoreSurface = testFont.render("Cramptes Geants", False, (64,64,64))
scoreRectangle = scoreSurface.get_rect(center = (400,50))

snailSurface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snailRectangle = snailSurface.get_rect(bottomright = (600,300))

playerSurface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
playerRectangle = playerSurface.get_rect(midbottom = (80,300))
playerGravity = 0

while True:#game loop infinie, dessiner tous les éléments, ensuite tout update
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            exit() #on call exit plutôt que break, break ne terminerait que le if 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(playerRectangle.collidepoint(event.pos)):
                playerGravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and playerRectangle.bottom>=300:
                playerGravity = -20

    screen.blit(sky,(0,0))
    screen.blit(ground,(0,300))
    pygame.draw.rect(screen,'#c0e8ec',scoreRectangle)
    pygame.draw.rect(screen,'#c0e8ec',scoreRectangle,5)

    screen.blit(scoreSurface,scoreRectangle)

    snailRectangle.left -= 5
    if(snailRectangle.right <0):
        snailRectangle.left = 800 # fait aller l'escargot de droite à gauche
    screen.blit(snailSurface,snailRectangle)

    #Player
    playerGravity += 1
    playerRectangle.top += playerGravity
    if(playerRectangle.bottom>=300):
        playerRectangle.bottom=300
    screen.blit(playerSurface,playerRectangle)

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
