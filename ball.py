import pygame
import time

BALL_ACTIVE_DURATION = .1

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity_x = 0
        self.velocity_y = 0
        self.start_time = None

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def check_collision_with_walls(self, screen_width, screen_height):
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.velocity_x = -self.velocity_x
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.velocity_y = -self.velocity_y

    def start_moving(self, direction):
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

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), self.radius)