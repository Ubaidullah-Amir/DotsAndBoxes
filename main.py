from Algorithm import *
from DotsNBoxes import *
from Board import *
from Nodes import *
import pygame


WHITE = (255, 255, 255)
RED = (252, 91, 122)
BLUE = (78, 193, 246)
GREEN = (0, 255, 0)
BLACK = (12, 12, 12)
GREY = (164, 162,162)

SCREEN = WIDTH, HEIGHT = 800, 600
pygame.init()
# window size
win = pygame.display.set_mode((WIDTH, HEIGHT))
running=True
Match = DotsNBoxes(3*2+1, 3*2+1, 3,win)
Match.start()
# while running:
#     win.fill(WHITE)
#     mouse_position=pygame.mouse.get_pos()

    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print("quit")
#             running=False
#     pygame.display.update()
# pygame.quit()
