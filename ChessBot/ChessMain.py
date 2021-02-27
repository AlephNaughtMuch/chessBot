"""
This class is responsible for storing the current all the information about the current state of a chess game. It will
also be responsible for determining the valid moves at the current state. It will also keep a move log.
"""


import pygame
from ChessBot import ChessEngine

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
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
        