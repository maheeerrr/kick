import pygame

pygame.mixer.init()
movement_stopped = False
kick_sound = pygame.mixer.Sound("kick_ball.wav")
class Player_1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.original_image = pygame.image.load("Player 1.png").convert_alpha()
        self.image_size = self.original_image.get_size()
        scale_size = (int(self.image_size[0] * 1.7), int(self.image_size[1] * 1.7))
        self.original_image = pygame.transform.scale(self.original_image, scale_size)
        self.image_size = self.original_image.get_size()
        self.flipped_image = pygame.transform.flip(self.original_image, True, False)
        self.image = self.original_image
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 6.5
        self.width = self.image_size[0]
        self.height = self.image_size[1]
        self.current_direction = "right"

    def move_direction(self, direction):
        global movement_stopped
        if not movement_stopped:
            if direction == "right" and self.x < 1661 - self.width:
                self.x += self.delta
                self.image = self.original_image
                self.current_direction = "right"
            elif direction == "left" and self.x > 0:
                self.x -= self.delta
                self.image = self.flipped_image
                self.current_direction = "left"
            elif direction == "up" and self.y > 0:
                self.y -= self.delta
            elif direction == "down" and self.y < 1000 - self.height:
                self.y += self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def detect_collision(self, ball):
        if (self.x < ball.x < self.x + self.width and
            self.y < ball.y < self.y + self.height):
            # Determine direction based on where the sprite makes contact with the ball
            dx = (ball.x - (self.x + self.width / 2))
            dy = (ball.y - (self.y + self.height / 2))
            ball.start_moving((dx, dy))
            kick_sound.play()

    def stop(self):
        self.velocity_x = 0
        self.velocity_y = 0
