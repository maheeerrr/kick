import pygame

movement_stopped = False

class Player_2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Player 2.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 1.7, self.image_size[1] * 1.7)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.flipped_image = pygame.transform.flip(self.image, True, False)
        self.delta = 6.5
        self.width = self.image_size[0]
        self.height = self.image_size[1]
        self.current_direction = "right"

    def move_direction(self, direction):
        global movement_stopped
        if not movement_stopped:
          if direction == "right" and self.x < 1661 - 32:
            self.x = self.x + self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
          if direction == "left" and self.x > 0 - 32:
            self.x = self.x - self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
          if direction == "up" and self.y > 0 - 32:
            self.y = self.y - self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
          if direction == "down" and self.y < 1000 - 32:
            self.y = self.y + self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def detect_collision(self, ball):
        if (self.x < ball.x < self.x + self.width and
            self.y < ball.y < self.y + self.height):
            # Determine direction based on where the sprite makes contact with the ball
            dx = (ball.x - (self.x + self.width / 2))
            dy = (ball.y - (self.y + self.height / 2))
            ball.start_moving((dx, dy))

    def stop(self):
        self.velocity_x = 0
        self.velocity_y = 0