import sys
import copy
import random 
import pygame
import numpy as np
import math

from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE AI")
screen.fill(BG_COLOR)


class Board:

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqr = self.squares  # [squares]
        self.marked_sqrs = 0

    def final_state(self, show=False):
        # return 0 if there is no win yet and if board full = draw
        # retunr 1 if player 1 wins
        # retunr 2 if player 2 wins

        # vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]  # retunr the player who won

        # horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]

        # diagonals desc
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # diagonal asc
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # no win yet
        return 0

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def is_empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_empty_sqr(row, col):
                    empty_sqrs.append((row, col))

        return empty_sqrs

    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0

class AI:
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player
        self.other_player = 1 if self.player == 2 else 2

    def minimax(self, board, depth=0, maximizing_player=True):

        # Base case: Check for terminal states
        case = board.final_state(show=False)
        if case == self.player:
            return {'position': None, 'score': 10 - depth}
        elif case == self.other_player:
            return {'position': None, 'score': depth - 10}
        elif len(board.get_empty_sqrs()) == 0:
            return {'position': None, 'score': 0}

        if maximizing_player:
            best = {'position': None, 'score': -math.inf}
            for (row, col) in board.get_empty_sqrs():
                board.mark_sqr(row, col, self.player)
                sim_score = self.minimax(board, depth + 1, False)
                board.squares[row][col] = 0

                if sim_score['score'] > best['score']:
                    best['score'] = sim_score['score']
                    best['position'] = (row, col)

        else:
            best = {'position': None, 'score': math.inf}
            for (row, col) in board.get_empty_sqrs():
                board.mark_sqr(row, col, self.other_player)
                sim_score = self.minimax(board, depth + 1, True)
                board.squares[row][col] = 0

                if sim_score['score'] < best['score']:
                    best['score'] = sim_score['score']
                    best['position'] = (row, col)

        print('thinking...', best['score'])
        return best

class Game:
    
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1 #1-cross #2-cirles #1 we start, 2 ai starts
        self.gamemode = 'ai' #pvp or ai
        self.running = True
        self.show_lines()


    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()


    def show_lines(self):

        #paint screen when reset
        screen.fill(BG_COLOR)

        #vertical
        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH- SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)

        #horizonal
        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT-SQSIZE), LINE_WIDTH)

    def draw_fig(self, row, col):
        if self.player == 1:
            #desc line
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            
            #asc line
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
             

        elif self.player == 2:
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE //2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1

    def reset(self):
        self.__init__()
    
    def isover(self):
        return self.board.final_state(show= True) != 0 or self.board.isfull()

def main():
    game = Game()
    board = game.board
    ai = game.ai
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                # convert from pixels to rows and cols
                row = int(pos[1] // SQSIZE)
                col = int(pos[0] // SQSIZE)


                if board.is_empty_sqr(row, col) and game.running:
                    game.make_move(row, col)

                    if game.isover():
                        game.running = False

        if game.gamemode == "ai" and game.player == ai.player and game.running:
            pygame.display.update()

            # AI methods
            result = ai.minimax(board)

            if result['position'] is not None:
                row, col = result['position']
                print(f'The nest move for me is: {result}')
                game.make_move(row, col)

                if game.isover():
                    game.running = False
            else:
                print("Board is full!")
                game.running = False
                #game.reset()
                #board = game.board
                #ai = game.ai

        pygame.display.update()

main()
    