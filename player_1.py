import pygame


class Player_1:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Player 1.png")
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .5, self.image_size[1] * .5)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.image_size = self.image.get_size()
        self.image_right = pygame.image.load('right.png')
        self.image_left = pygame.image.load('left.png')
        self.image_up = pygame.image.load('up.png')
        self.image_down = pygame.image.load('down.png')
        self.image = self.image_right  # Set a default image
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
        # Create a rectangle for the ball using its coordinates and size
        ball_rect = pygame.Rect(ball.x, ball.y, ball.width, ball.height)

        # Check if the player's rectangle intersects with the ball's rectangle
        if self.rect.colliderect(ball_rect):
            # Determine direction based on where the sprite makes contact with the ball
            dx = (ball.x + ball.width / 2) - (self.x + self.width / 2)
            dy = (ball.y + ball.height / 2) - (self.y + self.height / 2)

            # Normalize the direction vector
            magnitude = (dx**2 + dy**2) ** 0.5
            if magnitude != 0:
                dx /= magnitude
                dy /= magnitude

            # Start the ball moving in the determined direction
            ball.start_moving((dx, dy))


