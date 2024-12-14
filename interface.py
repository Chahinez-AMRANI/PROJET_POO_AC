import pygame
import random

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
        obstacles = []
        for _ in range(20):
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            obstacles.append((x, y, random.choice(["tree", "wall"])))
        return obstacles

    def draw_grid(self):
        # Dessine l'arrière-plan avant la grille
        self.screen.blit(self.background, (0, 0))
        # Dessine les lignes de la grille par-dessus
        for x in range(0, self.width, CELL_SIZE):
            for y in range(0, self.height, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

    def draw_obstacles(self):
        for x, y, obstacle_type in self.obstacles:
            color = TREE_COLOR if obstacle_type == "tree" else WALL_COLOR
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(self.screen, color, rect)

    def draw_units(self, player_units, enemy_units):
        for unit in player_units + enemy_units:
            unit.draw(self.screen)

    def draw_skills(self, unit):
        # Affiche les compétences disponibles pour le joueur
        if not unit.skills:
            return

        font = pygame.font.Font(None, 24)
        skill_text = "Skills: "
        for idx, skill in enumerate(unit.skills):
            skill_text += f"{idx + 1} - {skill.name}  "

        skill_surface = font.render(skill_text, True, (255, 255, 255))
        self.screen.blit(skill_surface, (10, self.height - 30))  # En bas de l'écran

    def display_skill_effect(self, skill, target):
        # Affiche un effet visuel lors de l'utilisation d'une compétence
        font = pygame.font.Font(None, 36)
        text_surface = font.render(f"{skill.name} activated!", True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))
        pygame.display.flip()
        pygame.time.delay(1000)

        if skill.name == "Fireball":
            pygame.draw.circle(
                self.screen,
                (255, 0, 0),  # Rouge pour Fireball
                (target.x * CELL_SIZE + CELL_SIZE // 2, target.y * CELL_SIZE + CELL_SIZE // 2),
                CELL_SIZE // 2,
                3
            )
        elif skill.name == "Shield":
            pygame.draw.circle(
                self.screen,
                (0, 255, 255),  # Cyan pour Shield
                (target.x * CELL_SIZE + CELL_SIZE // 2, target.y * CELL_SIZE + CELL_SIZE // 2),
                CELL_SIZE // 2,
                3
            )
        elif skill.name == "Arrows":
            pygame.draw.line(
                self.screen,
                (0, 255, 0),  # Vert pour Arrows
                (target.x * CELL_SIZE, target.y * CELL_SIZE),
                (target.x * CELL_SIZE + CELL_SIZE, target.y * CELL_SIZE + CELL_SIZE),
                3
            )
        elif skill.name == "Slash":
            pygame.draw.line(
                self.screen,
                (255, 255, 0),  # Jaune pour Slash
                (target.x * CELL_SIZE, target.y * CELL_SIZE),
                (target.x * CELL_SIZE + CELL_SIZE, target.y * CELL_SIZE + CELL_SIZE),
                5
            )

        pygame.display.flip()
        pygame.time.delay(1000)  # Pause pour afficher l'effet

    def flip_display(self, player_units, enemy_units):
        self.draw_grid()
        self.draw_obstacles()
        self.draw_units(player_units, enemy_units)
        selected_unit = next((unit for unit in player_units if unit.is_selected), None)
        if selected_unit:
            self.draw_skills(selected_unit)
        pygame.display.flip()
