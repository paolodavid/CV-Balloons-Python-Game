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
    red, green, blue = (255,0,0), (0,255,0), (0,0,255)
    pygame.draw.polygon(window, red, ((491, 100), (788, 100), (937, 357),
                                      (788, 614), (491, 614), (342, 357)))
    pygame.draw.circle(window,green,(640,360),200)
    pygame.draw.line(window,blue,(468,392), (812,392), 10)
    pygame.draw.rect(window, blue,(468,307,345,70),border_radius=20)

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)