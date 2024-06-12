import pygame
import time

BALL_ACTIVE_DURATION = .1
pygame.mixer.init()
bounce_sound = pygame.mixer.Sound("wall_ball.wav")

class Ball:
    def __init__(self, x, y, radius, image_path):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity_x = 0
        self.velocity_y = 0
        self.start_time = None
        self.image = pygame.image.load("ball.png")
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))
    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

    def check_collision_with_walls(self, screen_width, screen_height):
        if self.x - self.radius <= 50 or self.x + self.radius >= 1565:
            self.velocity_x = -self.velocity_x
            bounce_sound.play()
        if self.y - self.radius <= 25 or self.y + self.radius >= 950:
            self.velocity_y = -self.velocity_y
            bounce_sound.play()

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
        ball_rect = self.image.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(self.image, ball_rect.topleft)

    def stop(self):
        self.velocity_x = 0
        self.velocity_y = 0