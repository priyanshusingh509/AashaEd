import pygame, game_options
def startgame():
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
    homeasset_url = 'Photos/background_img.jpg'
    home_screen = pygame.image.load(homeasset_url) 

    # Fonts
    pygame.font.init()
    header_font = pygame.font.Font('Fonts/Ghiya Strokes Reg.ttf',90)
    button_font = pygame.font.Font('Fonts/P22 Underground Regular.ttf',35)

    # Header
    header = header_font.render('Select A Level', True, (255,255,255))

    # Button Settings

    easy_button = button_font.render('Easy', True, (255,255,255))
    med_button = button_font.render('Medium', True, (255,255,255))
    hard_button = button_font.render('Hard', True, (255,255,255))

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
                # For Easy Button
                if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2-100) <= mouse[1] <= (height/2-100)+50:
                    game_options.start_game('easy')
                # For Medium Button
                if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2) <= mouse[1] <= (height/2)+50:
                    game_options.start_game('mid')
                # For Hard Button 
                if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2+100) <= mouse[1] <= (height/2+100)+50:
                    game_options.start_game('diff')
                
        screen.blit(home_screen,(0,0))
        screen.blit(header,((width/2-270),(height/2-250)))
        
        

        # Easy Button
        if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2-100) <= mouse[1] <= (height/2-100)+50:
            pygame.draw.rect(screen,(170,170,170), [(width/2-100),(height/2-100),200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [(width/2-100),(height/2-100),200,50])
        screen.blit(easy_button,((width/2-30),(height/2-94)))

        # Medium Button
        if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2) <= mouse[1] <= (height/2)+50:
            pygame.draw.rect(screen,(170,170,170), [(width/2-100),(height/2),200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [(width/2-100),(height/2),200,50])
        screen.blit(med_button,((width/2-60),(height/2+4)))
        
        # Hard Button
        if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2+100) <= mouse[1] <= (height/2+100)+50:
            pygame.draw.rect(screen,(170,170,170), [(width/2-100),(height/2+100),200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [(width/2-100),(height/2+100),200,50])
        screen.blit(hard_button,((width/2-30),(height/2+104)))
        pygame.display.update()