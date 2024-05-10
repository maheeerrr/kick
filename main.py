import pygame
import time

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

plain = pygame.image.load("title.png")
bg = pygame.image.load("map.png")
b = pygame.image.load("ball.png")
# render the text for later

display_intro = big_font.render("Welcome to Kick!", True, (255, 0, 0))
display_intro2 = intro_font.render("Score goals against your opponent to win.", True, (0, 0, 0))
display_intro3 = intro_font.render("Try to get a high score!", True, (0, 0, 0))
display_intro4 = intro_font.render("Click anywhere to start.", True, (0, 0, 0))

display_end = big_font.render("Game Over!", True, (255, 0, 0))

start_time = time.time() + 10
seconds = time.time()
display_string = "Timer: " + str(seconds) + "s"
display_seconds = my_font.render(display_string, True, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
game_start = False
game_over = False
# -------- Main Program Loop -----------
while run:
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
            start_time = time.time() + 1
            
            
    if not game_start or not game_over:
        screen.blit(plain, (0, 0))
        screen.blit(display_intro, (200, 100))
        screen.blit(display_intro2, (50, 150))
        screen.blit(display_intro3, (200, 185))
        screen.blit(display_intro4, (200, 220))
    if game_start and not game_over:
        screen.blit(bg, (0, 0))
        screen.blit(b, (200, 200))
        screen.blit(display_seconds, (0, 0))
    if not game_start and game_over:
        screen.blit(plain, (0, 0))
        screen.blit(display_end, (240, 100))
        
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()