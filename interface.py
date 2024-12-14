import pygame
import random

# cette interface a une MAP
# Initialisation des constantes
CELL_SIZE = 40
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TREE_COLOR = (34, 139, 34)
WALL_COLOR = (139, 69, 19)

class Interface:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.grid_width = width // CELL_SIZE
        self.grid_height = height // CELL_SIZE
        self.obstacles = self.generate_obstacles()
        # Chargement du nouvel arrière-plan
        self.background = pygame.image.load("ninja_village_background.jpg").convert()

    def generate_obstacles(self):
        #génère des obstacles à des positions aléatoires
        obstacles = []
        for _ in range(20):  # Nombre d'obstacles
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
             obstacles.append((x, y, random.choice(["tree", "wall"])))
        return obstacles

    def draw_grid(self):
        """Affiche la grille."""
        self.screen.fill(BLACK)
        for x in range(0, self.width, CELL_SIZE):
            for y in range(0, self.height, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, DARK_GRAY, rect, 1)

    def draw_obstacles(self):
        for x, y, obstacle_type in self.obstacles:
            color = TREE_COLOR if obstacle_type == "tree" else WALL_COLOR
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, color, rect)

     def flip_display(self, player_units, enemy_units):
        self.draw_grid()
        self.draw_obstacles()
        for unit in player_units + enemy_units:
            unit.draw(self.screen)
        pygame.display.flip()
