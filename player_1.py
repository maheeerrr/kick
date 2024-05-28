import pygame


class Player_1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Player 1.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 2, self.image_size[1] * 2)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3

    def move_direction(self, direction):
        if direction == "right" and self.x < 725 - 32:
            self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "left" and self.x > 0 - 32:
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up" and self.y > 0 - 32:
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down" and self.y < 363 - 32:
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])