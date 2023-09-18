def keymap():
    import pygame
    import mysql.connector as con
    
    # Initiallizing Mysql
    myserv = con.connect(host='localhost', user='root', passwd='admin', database='aashaed')
    mycursor = myserv.cursor()
    
    # Saving New Data
    def savemap(texts = dict()):
        for i in texts:
            mycursor.execute(f'update keymap set keyname = \'{texts[i][0]}\' where keyid = {i}')
            mycursor.execute(f'update keymap set keygame = \'{texts[i][1]}\' where keyid = {i}')
        myserv.commit()
    
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
    home_screen = pygame.image.load('Photos/background_img.jpg')

    # Fonts
    pygame.font.init()
    header_font = pygame.font.Font('Fonts/Ghiya Strokes Reg.ttf',90)
    text_font = pygame.font.Font('Fonts/P22 Underground Regular.ttf',35)
    
    # Header
    header = header_font.render('Key Mapping', True, (255,255,255))

    # Button Settings
    submit_mapper = text_font.render('Submit/Next', True, (255,255,255))
    repeat_mapper = text_font.render('Repeat', True, (255,255,255))
    hint_mapper = text_font.render('Hint', True, (255,255,255))
    result_mapper = text_font.render('Result', True, (255,255,255))
    save_button = text_font.render('Save', True, (255,255,255))

    # Input Boxes
    global submit_value
    global repeat_value
    global hint_value
    global result_value
    global submit_text
    global repeat_text
    global hint_text
    global result_text

    mycursor.execute('select keygame from keymap where keyid=0')
    submit_value = list(mycursor)[0][0]
    mycursor.execute('select keygame from keymap where keyid=1')
    repeat_value = list(mycursor)[0][0]
    mycursor.execute('select keygame from keymap where keyid=2')
    hint_value = list(mycursor)[0][0]
    mycursor.execute('select keygame from keymap where keyid=3')
    result_value = list(mycursor)[0][0]
    
    mycursor.execute('select keyname from keymap where keyid=0')
    submit_text = str(list(mycursor)[0]).split('\'')[1]
    mycursor.execute('select keyname from keymap where keyid=1')
    repeat_text = str(list(mycursor)[0]).split('\'')[1]
    mycursor.execute('select keyname from keymap where keyid=2')
    hint_text = str(list(mycursor)[0]).split('\'')[1]
    mycursor.execute('select keyname from keymap where keyid=3')
    result_text = str(list(mycursor)[0]).split('\'')[1]

    submit_input = text_font.render(submit_text,True,(255,255,255))
    repeat_input = text_font.render(repeat_text,True,(255,255,255))
    hint_input = text_font.render(hint_text,True,(255,255,255))
    result_input = text_font.render(result_text,True,(255,255,255))

    # Editing Input Boxes
    edit = [False,False,False,False,False]
    
    # Available keys
    keys = {pygame.K_1:'1', pygame.K_2:'2', pygame.K_3:'3', pygame.K_4:'4', pygame.K_5:'5', pygame.K_6:'6', pygame.K_7:'7', pygame.K_8:'8', pygame.K_9:'9', pygame.K_0:'0', pygame.K_TAB:'Tab', pygame.K_RETURN:'Enter', pygame.K_SPACE:'Space'}
    
    # Start Display
    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
                if True in edit:
                    text = ''
                    if event.key in keys:
                        text = keys[event.key]
                        value = event.key
                        if edit.index(True)==0:
                            submit_value = value
                            submit_text=text
                            submit_input = text_font.render(submit_text,True,(255,255,255))
                        elif edit.index(True)==1:
                            repeat_value = value
                            repeat_text=text
                            repeat_input = text_font.render(repeat_text,True,(255,255,255))
                        elif edit.index(True)==2:
                            hint_value = value
                            hint_text=text
                            hint_input = text_font.render(hint_text,True,(255,255,255))
                        elif edit.index(True)==3:
                            result_value=value
                            result_text=text
                            result_input = text_font.render(result_text,True,(255,255,255))
                    edit[edit.index(True)] = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] in range(450,650) and mouse[1] in range(195,245):
                    edit[0] = True
                if mouse[0] in range(450,650) and mouse[1] in range(265,315):
                    edit[1] = True
                if mouse[0] in range(450,650) and mouse[1] in range(335,385):
                    edit[2] = True
                if mouse[0] in range(450,650) and mouse[1] in range(405,455):
                    edit[3] = True
                if mouse[0] in range(300,500) and mouse[1] in range(500,550):
                    savemap({0:(submit_text,submit_value),1:(repeat_text,repeat_value),2:(hint_text,hint_value),3:(result_text,result_value)})
        # Screen
        screen.blit(home_screen,(0,0))
        screen.blit(header,(width/2-200,50))

        # Naming
        screen.blit(submit_mapper,(200,200))
        screen.blit(repeat_mapper,(200,270))
        screen.blit(hint_mapper,(200,340))
        screen.blit(result_mapper,(200,410))
        
        # Text Inputs
        if mouse[0] in range(450,650) and mouse[1] in range(195,245):
            pygame.draw.rect(screen,(170,170,170), [450,195,200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [450,195,200,50])

        if mouse[0] in range(450,650) and mouse[1] in range(265,315):
            pygame.draw.rect(screen,(170,170,170), [450,265,200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [450,265,200,50])

        if mouse[0] in range(450,650) and mouse[1] in range(335,385):
            pygame.draw.rect(screen,(170,170,170), [450,335,200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [450,335,200,50])

        if mouse[0] in range(450,650) and mouse[1] in range(405,455):
            pygame.draw.rect(screen,(170,170,170), [450,405,200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [450,405,200,50])
            
        screen.blit(submit_input,(500,200))
        screen.blit(repeat_input,(500,270))
        screen.blit(hint_input,(500,340))
        screen.blit(result_input,(500,410))
        
        # Save Button
        if mouse[0] in range(300,500) and mouse[1] in range(500,550):
            pygame.draw.rect(screen,(170,170,170), [300,500,200,50])
        else:
            pygame.draw.rect(screen,(100,100,100), [300,500,200,50])
        screen.blit(save_button,(365,502))
        pygame.display.update()