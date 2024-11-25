import pygame
import sys
import heapq

pygame.init()

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800

#values
CELL_SIZE = 20
ROWS = WINDOW_HEIGHT // CELL_SIZE
COLS = WINDOW_WIDTH // CELL_SIZE

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("a_star")

drawn_cells = set()
player_position = None
end_position = None


mode = "player"
path = []


def main():
    
    global mode, player_position, end_position, path
    
    
    clock = pygame.time.Clock()
    drawing = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    mouse_x, mouse_y = event.pos
                    col = mouse_x // CELL_SIZE
                    row = mouse_y // CELL_SIZE
                    
                    if mode == "player":
                        player_position = (row, col) #only once
                    elif mode == "draw":
                        drawn_cells.add((row, col)) #tas adding
                    elif mode == "end":
                        end_position = (row, col) #only once
                        
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    
            elif event.type == pygame.MOUSEMOTION and drawing:
                if mode == "draw":
                    mouse_x, mouse_y = event.pos 
                    col = mouse_x // CELL_SIZE
                    row = mouse_y // CELL_SIZE
                    drawn_cells.add((row, col))
                    
            
