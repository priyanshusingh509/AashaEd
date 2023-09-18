import pygame

def how_to():
    # Initiallizing Pygame
    pygame.init()

    res = 800,600
    height = res[1]
    width = res[0]
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption('AashaEd')

    # Display Settings
    homeasset_url = 'Photos/background_img.jpg'
    home_screen = pygame.image.load(homeasset_url)

    # Fonts
    pygame.font.init()
    header_font = pygame.font.Font('Fonts/Ghiya Strokes Reg.ttf',70)
    text_font = pygame.font.Font('Fonts/P22 Underground Regular.ttf',20)

    # Header
    header = header_font.render('How to Play', True, (255,255,255))

    # Button Settings
    line1 = text_font.render('\u2022You will hear an English word belonging to the chosen difficulty class.', True, (255,255,255))
    line2 = text_font.render('\u2022You must try and type the heard word in the given box and hit enter to check its', True, (255,255,255))
    line2_contd = text_font.render('spelling.', True, (255,255,255))
    line3 = text_font.render('\u2022To hear the word again, click on the ‘Repeat’ button.', True, (255,255,255))
    line4 = text_font.render('\u2022In case of facing difficulties with the given word’s spelling, you may click on', True, (255,255,255))
    line4_contd = text_font.render('the ‘Hint button to reveal the word’s spelling, letter by letter.', True, (255,255,255))
    line5 = text_font.render('\u2022To move on to the next word, click on the ‘Next Word’ button, and you will hear', True, (255,255,255))
    line5_contd = text_font.render('the next word.', True, (255,255,255))
    line6 = text_font.render('\u2022To know the result, click on the ‘Result’ button to view a bar graph of your', True, (255,255,255))
    line6_contd = text_font.render('journey.', True, (255,255,255))
    line7 = text_font.render('\u2022After each successful attempt of the word, you will be provided its meaning', True, (255,255,255))
    line7_contd = text_font.render('and usage.', True, (255,255,255))
    line8 = text_font.render('\u2022Getting the word correct provides you with 10 points and each wrong answer', True, (255,255,255))
    line8_contd = text_font.render('costs you 3 points.', True, (255,255,255))
    line9 = text_font.render('\u2022For the best experience, wear a headset.', True, (255,255,255))

    # Render Game
    running = True
    while running:
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
                
        screen.blit(home_screen,(0,0))
        screen.blit(header,((width/2-174),(height/2-240)))
        screen.blit(line1,((30),(150)))
        screen.blit(line2,((30),(175)))
        screen.blit(line2_contd,((45),(200)))
        screen.blit(line3,((30),(225)))
        screen.blit(line4,((30),(250)))
        screen.blit(line4_contd,((45),(275)))
        screen.blit(line5,((30),(300)))
        screen.blit(line5_contd,((45),(325)))
        screen.blit(line6,((30),(350)))
        screen.blit(line6_contd,((45),(375)))
        screen.blit(line7,((30),(400)))
        screen.blit(line7_contd,((45),(425)))
        screen.blit(line8,((30),(450)))
        screen.blit(line8_contd,((45),(475)))
        screen.blit(line9,((30),(500)))
        
        pygame.display.update()