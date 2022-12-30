import pygame
class Rect:
    def __init__(self,x,y,width,height) -> None:
        self.rect=pygame.Rect(x,y,width,height)
    def draw(self,win,color):
        pygame.draw.rect(win,color,self.rect)
    def if_hit(self,win,positoin):
        if self.rect.collidepoint(positoin):
            pygame.draw.rect(win,(0,0,0),self.rect)
    
