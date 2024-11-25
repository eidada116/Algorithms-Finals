import pygame
import sys
import heapq

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

CELL_SIZE = 20
ROWS = WINDOW_HEIGHT // CELL_SIZE
COLS = WINDOW_WIDTH // CELL_SIZE #

DRAW = (0, 0, 255)  
PLAYER_COLOR = (255, 0, 0) 
END_COLOR = (255, 255, 0)  
VISITED_COLOR = (0, 255, 0)  
PATH_COLOR = (255, 165, 0)  
GRID_COLOR = (200, 200, 200)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("dijkstra's")

#background_image = pygame.image.load("background.jpg")
#background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

BACGKROUND_COLOR = (255,255,255)


drawn_cells = set() 
player_position = None 
end_position = None  


mode = "player"
path = []


def dijkstra(start, end, obstacles):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    visited = set()
    pq = [(0, start)]  
    came_from = {}
    distances = {start: 0}

    while pq:
        current_distance, current = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)

        if current == end:
            
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, visited

        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)

            if (
                0 <= neighbor[0] < ROWS
                and 0 <= neighbor[1] < COLS
                and neighbor not in obstacles
                and neighbor not in visited
            ):
                new_distance = current_distance + 1
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(pq, (new_distance, neighbor))
                    came_from[neighbor] = current

    return [], visited  




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
                        player_position = (row, col)
                    elif mode == "draw":
                        drawn_cells.add((row, col))
                    elif mode == "end":
                        end_position = (row, col)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False

            elif event.type == pygame.MOUSEMOTION and drawing:
                if mode == "draw":
                    mouse_x, mouse_y = event.pos
                    col = mouse_x // CELL_SIZE
                    row = mouse_y // CELL_SIZE
                    drawn_cells.add((row, col))

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n: #n for changing mode
                    if mode == "player":
                        mode = "draw"
                    elif mode == "draw":
                        mode = "end"
                    elif mode == "end":
                        mode = "player"
                elif event.key == pygame.K_m:  #run with m
                    if player_position and end_position:
                        path, visited = dijkstra(player_position, end_position, drawn_cells)

        #screen.blit(background_image, (0, 0))
        screen.fill(BACGKROUND_COLOR)


        #THIS DRAWS THE COLUMNS AND ROWS
        for row in range(ROWS + 1):
            pygame.draw.line(screen, GRID_COLOR, (0, row * CELL_SIZE), (WINDOW_WIDTH, row * CELL_SIZE))
        for col in range(COLS + 1):
            pygame.draw.line(screen, GRID_COLOR, (col * CELL_SIZE, 0), (col * CELL_SIZE, WINDOW_HEIGHT))

        for row, col in drawn_cells:
            pygame.draw.rect(screen, DRAW, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if 'visited' in locals():
            for row, col in visited:
                pygame.draw.rect(screen, VISITED_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if end_position:
            end_row, end_col = end_position
            pygame.draw.rect(screen, END_COLOR, (end_col * CELL_SIZE, end_row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if player_position:
            player_row, player_col = player_position
            pygame.draw.rect(screen, PLAYER_COLOR, (player_col * CELL_SIZE, player_row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        for row, col in path:
            pygame.draw.rect(screen, PATH_COLOR, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
