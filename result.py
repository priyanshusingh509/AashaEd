def drawgraph(correct, incorrect):
    import pygame
    from pandas import DataFrame
    import matplotlib
    import matplotlib.backends.backend_agg as agg
    import pylab
    matplotlib.use('Agg')
    pygame.init()
    res = 800,600
    height = res[1]
    width = res[0]
    screen = pygame.display.set_mode(res)
    pygame.display.set_caption('AashaEd')
    homeasset_url = 'Photos/background_img.jpg'
    home_screen = pygame.image.load(homeasset_url)
    bg = pygame.image.load('Photos/white-paper-texture.png')
    pygame_icon = pygame.image.load('Photos/online-course.png')
    pygame.display.set_icon(pygame_icon)
    # Fonts
    pygame.font.init()
    header_font = pygame.font.Font('Fonts/Ghiya Strokes Reg.ttf',90)
    button_font = pygame.font.Font('Fonts/P22 Underground Regular.ttf',35)

    # Header
    header = header_font.render('Result', True, (255,255,255))

    data1 = {'Correct': [correct],'Wrong': [incorrect]}
    df1 = DataFrame(data1,columns=['Correct', 'Wrong'])
    figure1 = pylab.figure(figsize=(7,6), dpi=70)
    ax1 = figure1.add_subplot(111)
    bar1 = agg.FigureCanvasAgg(figure1)
    df1 = df1[['Correct', 'Wrong']].sum()
    df1.plot(kind='bar', ax=ax1, color=['blue','orange'])
    ax1.set_title('Correct Vs. Wrong')
    bar1.draw()
    renderer = bar1.get_renderer()
    raw_data = renderer.tostring_rgb()
    pylab.savefig('result.png',transparent=True)
    graph = pygame.image.load('result.png')

    
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
        screen.blit(header,((width/2-105),(height/2-250)))
        screen.blit(bg,(180,150))
        screen.blit(graph, (160,140))
        pygame.display.update()