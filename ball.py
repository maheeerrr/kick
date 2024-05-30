import pygame
import time

BALL_ACTIVE_DURATION = 1

class Ball:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("ball.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .05, self.image_size[1] * .05)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.velocity_x = 0
        self.velocity_y = 0
        self.start_time = None
        self.radius = self.image_size[0] / 2

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def start_moving(self, direction):
        if self.velocity_x == 0 and self.velocity_y == 0:
            self.velocity_x, self.velocity_y = direction
            self.start_time = time.time()

    def update_velocity(self):
        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            if elapsed_time >= BALL_ACTIVE_DURATION:
                self.velocity_x = 0
                self.velocity_y = 0
            else:
                slow_down_factor = (BALL_ACTIVE_DURATION - elapsed_time) / BALL_ACTIVE_DURATION
                self.velocity_x *= slow_down_factor
                self.velocity_y *= slow_down_factor
