import pygame, pyttsx3, random, webscrape, result
import mysql.connector as con
def start_game(type_dict):
    # Initiallizing mysql
    connection = con.connect(host = 'localhost', user = 'root', passwd = 'admin', database = 'aashaed')
    cursor_sql = connection.cursor()
    cursor_sql.execute(f'select * from {type_dict}_word')
    dictionary=[]
    for i in cursor_sql:
        dictionary.append(i[0])
    # Initiallizing Pygame
    pygame.init()
    res = 800,600
    height = res[1]
    width = res[0]
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption('AashaEd')
    pygame_icon = pygame.image.load('Photos/online-course.png')
    pygame.display.set_icon(pygame_icon)

    # Initiallizing Pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 110)

    # Key Mappings
    cursor_sql.execute('select keygame from keymap where keyid=0')
    submit_value = list(cursor_sql)[0][0]
    cursor_sql.execute('select keygame from keymap where keyid=1')
    repeat_value = list(cursor_sql)[0][0]
    cursor_sql.execute('select keygame from keymap where keyid=2')
    hint_value = list(cursor_sql)[0][0]
    cursor_sql.execute('select keygame from keymap where keyid=3')
    result_value = list(cursor_sql)[0][0]

    # Word Selection
    global word
    global spoken
    word = random.choice(dictionary)
    dictionary.remove(word)
    spoken = False
    
    
    # Game System
    global ncorrect
    global nincorrect
    global correct
    global point
    global text
    ncorrect = 0
    nincorrect = 0
    correct = False
    point = 0
    text = ''
    def new_word():
        global spoken
        global word
        global correct
        global meaning
        global usage
        global text
        global answer
        global submit_button
        word = random.choice(dictionary)
        dictionary.remove(word)
        correct = False
        meaning = small_font.render('', True, (255,255,255))
        usage = small_font.render('', True, (255,255,255))
        text = ''
        answer = header_font.render('', True, (255,255,255))
        submit_button = button_font.render('Submit', True, (255,255,255))
        spoken = False


    def submit():
        global ncorrect
        global nincorrect
        global word
        global text
        global point
        global answer
        global header
        global correct
        global submit_button
        if text == word:
            global meaning
            global usage
            correct = True
            ncorrect+=1
            answer = header_font.render('Correct Answer', True, (255,255,255))
            point+=10
            meaning = small_font.render('Meaning:'+ webscrape.scrape_meaning(word), True, (255,255,255))
            usage = small_font.render(f'Example: {webscrape.scrape_usage(word)}', True, (255,255,255))
            submit_button = button_font.render('  Next', True, (255,255,255))
        else:
            correct = False
            nincorrect+=1
            answer = header_font.render('    Try Again', True, (255,255,255))
            point-=2
        header = header_font.render(f'Points: {point}', True, (255,255,255))
    
    def repeat():
        global word
        engine.say(word)
        engine.runAndWait()
    
    def hint():
        global text
        global word
        if text != word:
            for x in range(len(text)):
                if text[x]!=word[x]:
                    text = text[:x]+word[x]
                    break
            else:
                text = text+word[len(text)]

    # Display Settings
    home_screen = pygame.image.load('Photos/background_img.jpg')

    # Button Settings
    global header
    global answer
    global meaning
    global usage
    global submit_button
    header_font = pygame.font.SysFont('Corbel',60)
    header = header_font.render(f'Points: {point}', True, (255,255,255))
    answer = header_font.render('', True, (255,255,255))

    button_font = pygame.font.SysFont('Corbel',35)
    submit_button = button_font.render('Submit', True, (255,255,255))
    repeat_button = button_font.render('Repeat', True, (255,255,255))
    hint_button = button_font.render('Hint', True, (255,255,255))
    result_button = button_font.render('Result', True, (255,255,255))
    
    small_font = pygame.font.SysFont('Corbel',18)
    meaning = small_font.render('', True, (255,255,255))
    usage = small_font.render('', True, (255,255,255))
    
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
                if event.key == submit_value:
                    if correct == False:
                        submit()
                    else:
                        new_word()
                elif event.key == repeat_value:
                    repeat()
                elif event.key == hint_value:
                    hint()
                elif event.key == result_value:
                    result.drawgraph(ncorrect,nincorrect)
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_TAB or event.key == pygame.K_ESCAPE:
                    pass
                else:
                    text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Submit    
                if (width/2+170) <= mouse[0] <= (width/2+170)+200 and (height/2) <= mouse[1] <= (height/2)+50:
                    if correct == False:
                        submit()
                    else:
                        new_word()
                # Repeat
                if (width/2-230) <= mouse[0] <= (width/2-230)+200 and (height/2+80) <= mouse[1] <= (height/2+80)+50:
                    repeat()
                # Hint
                if (width/2+50) <= mouse[0] <= (width/2+50)+200 and (height/2+80) <= mouse[1] <= (height/2+80)+50:
                    hint()
                # Result
                if (width/2-60) <= mouse[0] <= (width/2-60)+200 and (height/2+160) <= mouse[1] <= (height/2+160)+50:
                    result.drawgraph(ncorrect,nincorrect)
        if len(text)>16:
            text = text[:-1]
        input = button_font.render(text, True, (0,0,0))
        screen.blit(home_screen,(0,0))
        screen.blit(header,((width/2-100),(height/2-280)))
        screen.blit(answer,((width/2-170),(height/2-220)))
        screen.blit(meaning,((width/2-365),(height/2-150)))
        screen.blit(usage,((width/2-365),(height/2-100)))

        # Input
        pygame.draw.rect(screen,(200,200,200), [(width/2-370),(height/2),500,50])
        screen.blit(input,((width/2-365),(height/2+7)))

        # Submit Button
        if (width/2+170) <= mouse[0] <= (width/2+170)+200 and (height/2) <= mouse[1] <= (height/2)+50:
            pygame.draw.rect(screen,(170,170,170), [(width/2+170),(height/2),200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [(width/2+170),(height/2),200,50])
        screen.blit(submit_button,((width/2+220),(height/2+8)))
        
        # Repeat Button
        if (width/2-230) <= mouse[0] <= (width/2-230)+200 and (height/2+80) <= mouse[1] <= (height/2+80)+50:
            pygame.draw.rect(screen,(170,170,170), [(width/2-230),(height/2+80),200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [(width/2-230),(height/2+80),200,50])
        screen.blit(repeat_button,((width/2-180),(height/2+88)))
        
        # Hint Button
        if (width/2+50) <= mouse[0] <= (width/2+50)+200 and (height/2+80) <= mouse[1] <= (height/2+80)+50:
            pygame.draw.rect(screen,(170,170,170), [(width/2+50),(height/2+80),200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [(width/2+50),(height/2+80),200,50])
        screen.blit(hint_button,((width/2+117),(height/2+88)))

        # Result Button
        if (width/2-100) <= mouse[0] <= (width/2-100)+200 and (height/2+160) <= mouse[1] <= (height/2+160)+50:
            pygame.draw.rect(screen,(170,170,170), [(width/2-100),(height/2+160),200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [(width/2-100),(height/2+160),200,50])
        screen.blit(result_button,((width/2-50),(height/2+168)))
        
        pygame.display.update()
        
        # Speak Word
        if spoken == False:
            engine.say(word)
            engine.runAndWait()
            spoken=True
