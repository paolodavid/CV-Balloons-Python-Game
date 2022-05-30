# Import
import pygame
import cv2

#Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Awesome Game")

#Initialize Clock for EPS
fps = 30
clock = pygame.time.Clock()

#Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    window.fill((255,255,255))

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)






