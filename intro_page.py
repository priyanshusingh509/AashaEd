import pygame, select_level,How_to_play, keymapping, sys, os

# EXE Support
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Initiallizing Pygame
pygame.init()
res = 800,600
height = res[1]
width = res[0]
screen = pygame.display.set_mode(res)
pygame.display.set_caption('AashaEd')
pygame_icon = pygame.image.load('Photos/online-course.png')
pygame.display.set_icon(pygame_icon)

# Display Settings
homeasset_url = resource_path('Photos/background_img.jpg')
home_screen = pygame.image.load(homeasset_url)

# Fonts
pygame.font.init()
header_font = pygame.font.Font('Fonts/Ghiya Strokes Reg.ttf',90)
button_font = pygame.font.Font('Fonts/P22 Underground Regular.ttf',35)

# Header
header = header_font.render('AashaEd', True, (255,255,255))

# Button Settings

start_button = button_font.render('Start', True, (255,255,255))
how_to_button = button_font.render('How to Play', True, (255,255,255))
keymap_button = button_font.render('Keymapping', True, (255,255,255))
quit_button = button_font.render('Quit', True, (255,255,255))

# Render Game
running = True
while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # For Start Button
            if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2-100) <= mouse[1] <= (height/2-100)+50:
                select_level.startgame()
            # For How-To-Play Button
            if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2) <= mouse[1] <= (height/2)+50:
                How_to_play.how_to()
            # For Quit Button 
            if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2+100) <= mouse[1] <= (height/2+100)+50:
                keymapping.keymap()
            if mouse[0] in range(300,500) and mouse[1] in range(500,550):
                running = False
            
    screen.blit(home_screen,(0,0))
    screen.blit(header,((width/2-165),(height/2-250)))


    # Start Button
    if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2-100) <= mouse[1] <= (height/2-100)+50:
        pygame.draw.rect(screen,(170,170,170), [(width/2-100),(height/2-100),200,50])
    else:
        pygame.draw.rect(screen,(100,100,100), [(width/2-100),(height/2-100),200,50])
    screen.blit(start_button,((width/2-35),(height/2-97)))

    # How to Button
    if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2) <= mouse[1] <= (height/2)+50:
        pygame.draw.rect(screen,(170,170,170), [(width/2-100),(height/2),200,50])
    else:
        pygame.draw.rect(screen,(100,100,100), [(width/2-100),(height/2),200,50])
    screen.blit(how_to_button,((width/2-92),(height/2+3)))
    
    # Keymap Button
    if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2+100) <= mouse[1] <= (height/2+100)+50:
        pygame.draw.rect(screen,(170,170,170), [(width/2-100),(height/2+100),200,50])
    else:
        pygame.draw.rect(screen,(100,100,100), [(width/2-100),(height/2+100),200,50])
    screen.blit(keymap_button,((width/2-92),(height/2+102)))
    
    # Quit Button
    if mouse[0] in range(300,500) and mouse[1] in range(500,550):
        pygame.draw.rect(screen,(170,170,170), [(width/2-100),(height/2+200),200,50])
    else:
        pygame.draw.rect(screen,(100,100,100), [(width/2-100),(height/2+200),200,50])
    screen.blit(quit_button,((width/2-35),(height/2+202)))
    pygame.display.update()