import pygame
import random

def window(screen):
    # draw horizontal lines
    for i in range(1, 16):
        pygame.draw.line(
            screen,
            "dark green",
            (0, i*32),
            (640, i*32)
        )
        # draw vertical lines
    for i in range(1, 20):
        pygame.draw.line(
            screen,
            "dark green",
            (i * 32, 0),
            (i * 32, 512)
        )
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        rand1 = 0
        rand2 = 0
        screen.fill("light green")
        window(screen)
        screen.blit(mole_image, mole_image.get_rect(topleft=(rand1, rand2)))
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #used to randomize the location of the mole image
                    x, y = pygame.mouse.get_pos()
                    if rand1 <= x <= rand1 +32 and rand2 <= y <= rand2 +32:
                        rand1 = random.randrange(0,20)*32
                        rand2 = random.randrange(0,16)*32
                        screen.fill("light green")
                        window(screen)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(rand1, rand2)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
