"""
Rect

    Can detect Collisions
    Can access x and y points

    Two ways of creating a rect
    1. pygame.Rect(x,y,width,height)
    2. surface.get_rect()   #creates rect around a surface/image
"""

# Import
import pygame

#Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")

#Initialize Clock for EPS
fps = 30
clock = pygame.time.Clock()

# Load Images
imgBackground = pygame.image.load('../Resources/BackgroundBlue.jpg').convert()    #it should have the same size of your window
imgBalloonRed = pygame.image.load('../Resources/BalloonRed.png').convert_alpha()    #differently from comvert, accepts png
#uso getrect se voglio creare un oggetto da un immagine esistente
# è la via piu usata
rectBalloon = imgBalloonRed.get_rect()

# Rect
#uso Rect se voglio creare un oggetto rettangolo a partire da 0
rectNew = pygame.Rect(500,0,200,200)


#Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    print(rectBalloon.colliderect(rectNew))

    # comandi per fare spostare l'oggetto lungo asse x e y
    rectBalloon.x += 5
    #rectBalloon.y += 5

    window.blit(imgBackground,(0, 0))
    #pygame.draw.rect(window, (0,255,0),rectBalloon)
    pygame.draw.rect(window, (0,255,0),rectNew)
    window.blit(imgBalloonRed, rectBalloon)


    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)