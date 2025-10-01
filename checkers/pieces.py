from .constants import BEIGE, SQUARE_SIZE, CROWN, RED, WHITE, GREY
import pygame

class Piece:
    PADDING = 10
    BORDER = 2     

    # Inicia o objeto Peça
    def __init__(self, row, col, color): 
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == BEIGE:
            self.direction = -1      
        else:
             self.direction = 1
        self.x = 0
        self.y = 0
        self.calc_pos()
        
    # Define a posição da Peça
    def calc_pos(self):
        centralize = SQUARE_SIZE // 2 #Centro do quadrado
        self.x = SQUARE_SIZE * self.col + centralize
        self.y = SQUARE_SIZE * self.row + centralize
    
    # Desenha a peça
    def draw(self, win):
        centralize = SQUARE_SIZE // 2 #Centro do quadrado
        radius = centralize -  self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)   