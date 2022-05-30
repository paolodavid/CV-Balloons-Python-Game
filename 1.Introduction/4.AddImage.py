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

#Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    window.blit(imgBackground,(0, 0))
    window.blit(imgBalloonRed, (200, 300))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)