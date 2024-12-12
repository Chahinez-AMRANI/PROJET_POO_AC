import pygame
from skills import Fireball, Shield, Arrows, Evasion, Slash 

CELL_SIZE = 60


class Unit:
    """Classe de base pour représenter une unité."""
    def __init__(self, x, y, health, attack_power, team):
        self.x = x
        self.y = y
        self.health = health
        self.attack_power = attack_power
        self.team = team  # 'player' ou 'enemy'
        self.is_selected = False
        self.shield = 0  # Valeur du bouclier (par défaut 0)
        self.dodge_chance = 0  # Chance d'esquiver une attaque (par défaut 0)
        self.skills = []  # Liste des compétences de l'unité

    def move(self, dx, dy):
        """Déplace l'unité."""
        if 0 <= self.x + dx < 8 and 0 <= self.y + dy < 8:  # Limite de la grille
            self.x += dx
            self.y += dy

    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power
            print(f"{self.__class__.__name__} attaque {target.__class__.__name__}. Santé restante : {target.health}.")

    def draw(self, screen):
        """Dessine l'unité sur l'écran."""
        color = (0, 0, 255) if self.team == 'player' else (255, 0, 0)
        if self.is_selected:
            pygame.draw.rect(screen, (0, 255, 0), (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    def take_damage(self, damage):
        """Réduit les points de vie en tenant compte du bouclier."""
        if self.shield > 0:
            damage = max(0, damage - self.shield)
            self.shield = max(0, self.shield - damage)
        self.health -= damage
        print(f"{self.__class__.__name__} subit {damage} dégâts. Santé restante : {self.health}.")


class Ninja(Unit):
    """Classe pour représenter un Ninja."""
    def __init__(self, x, y, team):
        super().__init__(x, y, health=20, attack_power=10, team=team)
        self.skills = [Fireball(), Evasion()]  # Compétences pour Ninja


class Samurai(Unit):
    """Classe pour représenter un Samurai."""
    def __init__(self, x, y, team):
        super().__init__(x, y, health=30, attack_power=8, team=team)
        self.skills = [Slash(), Shield()]  # Compétences pour Samurai


class Archer(Unit):
    """Classe pour représenter un Archer."""
    def __init__(self, x, y, team):
        super().__init__(x, y, health=15, attack_power=7, team=team)
        self.skills = [Arrows(), Evasion()]  # Compétences pour Archer
