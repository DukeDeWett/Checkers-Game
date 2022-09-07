import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb colors
RED = (184, 22, 30)
WHITE = (255, 255, 255)
BLACK = (36, 31, 31)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('checkers/assets/crown.png'), (44, 25))
