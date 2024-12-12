import pygame
import random

# cette interface a une MAP
# Initialisation des constantes
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40
BLACK = (0, 0, 0)
DARK_GRAY = (50, 50, 50)
TREE_COLOR = (34, 139, 34)  # Vert pour les arbres
WALL_COLOR = (139, 69, 19)  # Brun pour les murs

class Interface:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.grid_width = width // CELL_SIZE
        self.grid_height = height // CELL_SIZE
        self.obstacles = self.generate_obstacles()

    def generate_obstacles(self):
        """Génère des positions aléatoires pour les obstacles."""
        obstacles = []
        for _ in range(20):  # Nombre d'obstacles
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            obstacles.append((x, y, "tree" if random.random() < 0.5 else "wall"))
        return obstacles

    def draw_grid(self):
        """Affiche la grille."""
        self.screen.fill(BLACK)
        for x in range(0, self.width, CELL_SIZE):
            for y in range(0, self.height, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, DARK_GRAY, rect, 1)

    def draw_obstacles(self):
        """Dessine les obstacles sur la carte."""
        for x, y, obstacle_type in self.obstacles:
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = TREE_COLOR if obstacle_type == "tree" else WALL_COLOR
            pygame.draw.rect(self.screen, color, rect)

    def draw_units(self, player_units, enemy_units):
        """Dessine les unités."""
        for unit in player_units + enemy_units:
            unit.draw(self.screen)

    def run(self, player_units, enemy_units):
        """Boucle principale du jeu."""
        self.draw_grid()  # Dessine la grille
        self.draw_obstacles()  # Dessine les obstacles
        self.draw_units(player_units, enemy_units)  # Dessine les unités des joueurs et ennemis

# Correction des positions d'éléments : vérifiez les unités
class Unit:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen):
        """Dessine l'unité centrée dans la cellule."""
        pygame.draw.circle(
            screen,
            self.color,
            (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2),  # Correction des positions
            CELL_SIZE // 3,
        )
