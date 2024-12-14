import pygame
from skills import Fireball, Shield, Arrows, Evasion, Slash

CELL_SIZE = 40

class Unit:
    def __init__(self, x, y, health, attack_power, team):
        self.x = x
        self.y = y
        self.health = health
        self.attack_power = attack_power
        self.team = team  # 'player' ou 'enemy'
        self.is_selected = False

    def move(self, dx, dy):
        """Déplace l'unité dans la grille."""
        if 0 <= self.x + dx < 800 // CELL_SIZE and 0 <= self.y + dy < 600 // CELL_SIZE:
            self.x += dx
            self.y += dy

    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power

    def draw(self, screen):
        """Dessine l'unité sur la grille."""
        color = (0, 0, 255) if self.team == 'player' else (255, 0, 0)
        if self.is_selected:
            pygame.draw.circle(
                screen, (0, 255, 0),
                (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2),
                CELL_SIZE // 2, 3
            )
        pygame.draw.circle(
            screen, color,
            (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2),
            CELL_SIZE // 3
        )

class Ninja(Unit):
    def __init__(self, x, y, team):
        super().__init__(x, y, health=20, attack_power=10, team=team)
        self.skills = [Fireball(), Evasion()]

class Samurai(Unit):
    def __init__(self, x, y, team):
        super().__init__(x, y, health=30, attack_power=8, team=team)
        self.skills = [Slash(), Shield()]

class Archer(Unit):
    def __init__(self, x, y, team):
        super().__init__(x, y, health=15, attack_power=7, team=team)
        self.skills = [Arrows(), Evasion()]
