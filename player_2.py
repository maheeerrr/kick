import pygame


class Player_2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Player 1.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.image_right = pygame.image.load('right_2.png')
        self.image_left = pygame.image.load('left_2.png')
        self.image_up = pygame.image.load('up_2.png')
        self.image_down = pygame.image.load('down_2.png')
        self.image = self.image_left  # Set a default image
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3
        self.width = self.image_size[0]
        self.height = self.image_size[1]

    def move_direction(self, direction):
        # Images for each direction
        self.images = {
            "right": self.image_right,
            "left": self.image_left,
            "up": self.image_up,
            "down": self.image_down
        }

        if direction == "right" and self.x < 725 - 32:
            self.x += self.delta
            self.image = self.images["right"]
        elif direction == "left" and self.x > 0 - 32:
            self.x -= self.delta
            self.image = self.images["left"]
        elif direction == "up" and self.y > 0 - 32:
            self.y -= self.delta
            self.image = self.images["up"]
        elif direction == "down" and self.y < 363 - 32:
            self.y += self.delta
            self.image = self.images["down"]

        # Update the rectangle after moving
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def detect_collision(self, ball):
        if (self.x < ball.x < self.x + self.width and
            self.y < ball.y < self.y + self.height):
            # Determine direction based on where the sprite makes contact with the ball
            dx = (ball.x - (self.x + self.width / 2))
            dy = (ball.y - (self.y + self.height / 2))
            ball.start_moving((dx, dy))


