import pygame

# INFORMAÇÕES DO TABULEIRO
WIDTH, HEIGHT = 600, 600    # Largura e Altura da Janela
ROWS, COLS = 8, 8           # Filas e Colunas
SQUARE_SIZE = WIDTH//COLS   # Tamanho de cada quadrado do tabuleiro

# CORES
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BEIGE = (255, 255, 102)
GREY = (96, 96, 96)
GREEN = (0, 255, 0)

# IMAGENS
CROWN = pygame.transform.scale(pygame.image.load('C:\\Users\\T-GAMER\\Desktop\\Projetos\\Damas\\assets\\crown.png'),(39, 18))