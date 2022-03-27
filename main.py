import pygame
import pygments
import ai
import player

DISPLAY_W, DISPLAY_H = 700, 500
WIN = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
pygame.display.set_caption("Pong VS AI")

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event == event.QUIT:
                run = False
                