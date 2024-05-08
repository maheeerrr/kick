import pygame

# set up pygame modules
pygame.init()
pygame.font.init()
intro_font = pygame.font.SysFont('Arial', 30)
big_font = pygame.font.SysFont('Comic Sans', 60)
pygame.display.set_caption("Kick!")

# set up variables for the display
size = (725, 363)
screen = pygame.display.set_mode(size)

title = pygame.image.load("title.png")
bg = pygame.image.load("map.png")
# render the text for later

display_intro = big_font.render("Welcome to Kick!", True, (255, 0, 0))
display_intro2 = intro_font.render("Score goals against your opponent to win.", True, (0, 0, 0))
display_intro3 = intro_font.render("Try to get a high score!", True, (0, 0, 0))
display_intro4 = intro_font.render("Click anywhere to start.", True, (0, 0, 0))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
game_start = False
# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_start = True
            
    screen.blit(title, (0, 0))
    screen.blit(display_intro, (200, 100))
    screen.blit(display_intro2, (50, 150))
    screen.blit(display_intro3, (200, 185))
    screen.blit(display_intro4, (200, 220))
    if game_start == True:
        screen.blit(bg, (0, 0))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()