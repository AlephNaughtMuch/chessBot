"""
This class is responsible for storing the current all the information about the current state of a chess game. It will
also be responsible for determining the valid moves at the current state. It will also keep a move log.
"""


import pygame
from ChessBot import ChessEngine

'''
Initialization of important properties and libraries
'''
pygame.init()

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 60
IMAGES = {}

'''
Initialize a global dictionary of images, called exactly once in the main
'''

def loadImages():
    pieces = ["wP", "wR", "wN", "wB", "wK", "wQ", "bP", "bR", "bN", "bB", "bK", "bQ"]

    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("resources/images/chess_pieces/" + piece + ".png"),
                                               (SQ_SIZE, SQ_SIZE))



'''
The main driver for the code, will handle user input and update the game accordingly
'''

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    game_state = ChessEngine.GameState()
    loadImages() #should only be done once
    running = True

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        drawGameState(screen, game_state)
        clock.tick(MAX_FPS)
        pygame.display.flip()

'''
Responsible for drawing the graphics for the current game state
'''

def drawGameState(screen, gs):
    drawSquares(screen)
    drawPieces(screen, gs.board)

'''
Draws the squares on the board
'''
def drawSquares(screen):
    colors = [pygame.Color(240, 240, 240), pygame.Color(50, 50, 50)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
Draws the pieces on the board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]

            if piece != "--":
                screen.blit(IMAGES[piece], pygame.Rect(column * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()