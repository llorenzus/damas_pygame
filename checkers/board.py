import pygame
from .constants import SQUARE_SIZE, WHITE, RED, ROWS, COLS, BLACK, BEIGE
from .pieces import Piece
class Board:

    # Inicia o objeto tabuleiro
    def __init__(self):
        self.board = []        
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
    
    # Desenha os quadrados no tabuleiro
    def draw_square(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                # onde desenhar, cor do desenho, (parametros do desenho)
                pygame.draw.rect(win, BEIGE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Cria o tabuleiro
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):      #Verifica se é um local onde a peça pode ser desenhada
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4 :
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_square(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)                    

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.queen_piece()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1        

    def get_piece(self, row, col):
        return self.board[row][col]     

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # Define se as peças movem para cima ou para baixo
        if piece.color == RED or piece.king:
            moves.update(self._verify_move_left(row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._verify_move_right(row - 1, max(row-3, -1), -1, piece.color, right))            
            
        if piece.color == WHITE or piece.king:
            moves.update(self._verify_move_left(row + 1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._verify_move_right(row + 1, min(row+3, ROWS), 1, piece.color, right))     

        return moves
    
    def _verify_move_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []

        for r in range(start, stop, step):
            
            if left < 0:
                break
            current = self.board[r][left]

            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped                    
                else:
                    moves[(r, left)] = last
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min (r+r, ROWS)
                    moves.update(self._verify_move_left(r+step, row, step, color, left - 1, skipped = last))
                    moves.update(self._verify_move_right(r+step, row, step, color, left + 1, skipped = last))  
                break;

            elif current.color == color:
                break

            else:
                last = [current]
            left -= 1
        return moves

    def _verify_move_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []

        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]

            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped                    
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._verify_move_left(r+step, row, step, color, right - 1, skipped = last))
                    moves.update(self._verify_move_right(r+step, row, step, color, right + 1, skipped = last))  
                break                                  
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        return moves    
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == RED:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <=0:
            return RED
        
        return None
