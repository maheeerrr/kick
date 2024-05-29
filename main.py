import pygame
import time
from ball import Ball
from player_1 import Player_1
from player_2 import Player_2

# set up pygame modules
pygame.init()
pygame.font.init()
intro_font = pygame.font.SysFont('Arial', 30)
big_font = pygame.font.SysFont('Comic Sans', 60)
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Kick!")

# set up variables for the display
size = (725, 363)
screen = pygame.display.set_mode(size)

x = 328
y = 160

plain = pygame.image.load("title.png")
bg = pygame.image.load("map.png")
b = Ball(x, y)
p1 = Player_1(50, 150)
p2 = Player_2(600, 150)
# render the text for later



display_intro = big_font.render("Welcome to Kick!", True, (120,81, 169))
display_intro2 = intro_font.render("Score goals against your opponent to win.", True, (255, 255, 255))
display_intro3 = intro_font.render("Try to get a high score!", True, (255, 255, 255))
display_intro4 = intro_font.render("Click anywhere to start.", True, (255, 255, 255))

display_end = big_font.render("Game Over!", True, (255, 0, 0))

start_time = time.time() + 120
seconds = time.time()
display_string = "Timer: " + str(seconds) + "s"
display_seconds = my_font.render(display_string, True, (0, 0, 0))

message = "Collision not detected"
display_message = my_font.render(message, True, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
game_start = False
game_over = False
collision = False
# -------- Main Program Loop -----------
while run:
    if not game_over and game_start:
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_d]:
          p1.move_direction("right")
        if keys[pygame.K_a]:
          p1.move_direction("left")
          pygame.transform.flip(p1.image, True, False)
        if keys[pygame.K_w]:
          p1.move_direction("up")
        if keys[pygame.K_s]:
          p1.move_direction("down")


        if keys[pygame.K_RIGHT]:
          p2.move_direction("right")
        if keys[pygame.K_LEFT]:
          p2.move_direction("left")
        if keys[pygame.K_UP]:
          p2.move_direction("up")
        if keys[pygame.K_DOWN]:
          p2.move_direction("down")

        if p1.rect.colliderect(b.rect):
          collision = True
        else:
          collision = False
        if p2.rect.colliderect(b.rect):
          collision = True
        else:
          collision = False

        if collision:
          b.set_location(x - 10, y - 10)
          collision = False
            
    if not game_over and game_start:
        current_time = time.time()
        seconds = round(start_time - current_time, 2)
        display_string = "Timer: " + str(seconds) + "s"
        display_seconds = my_font.render(display_string, True, (255, 255, 255))
    if seconds == 0:
        game_over = True
        game_start = False

    for event in pygame.event.get():  
          if event.type == pygame.QUIT:  # If user clicked close
            run = False
          if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            game_start = True
            start_time = time.time() + 120
            
            
    if not game_start or not game_over:
        screen.blit(plain, (0, 0))
        screen.blit(display_intro, (200, 100))
        screen.blit(display_intro2, (50, 150))
        screen.blit(display_intro3, (200, 185))
        screen.blit(display_intro4, (200, 220))
    if game_start and not game_over:
        screen.blit(bg, (0, 0))
        screen.blit(b.image, b.rect)
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        screen.blit(display_seconds, (0, 0))
        screen.blit(display_message, (0, 15))
    if not game_start and game_over:
        screen.blit(plain, (0, 0))
        screen.blit(display_end, (240, 100))
        
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
