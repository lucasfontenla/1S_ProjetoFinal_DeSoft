import pygame, math, eztext, eztextNum, os
from Servidor.gameClient3 import Client 
from Servidor.gameServer2 import Server
from threading import Thread  

client = Client()
server = Server()

pygame.init()


display_width = 800
display_height = 600

#window size
gameDisplay = pygame.display.set_mode((display_width, display_height))#, pygame.FULLSCREEN)
    
#Title
pygame.display.set_caption("Tug War - O melhor jogo do Brasil")
    
#variável para FPS
clock = pygame.time.Clock()

intro = 0

alp = 255


def func(x):
    fun = 255*(1/(1 + math.e**-(0.05*x)))
    return fun
    
jaja = False

while True:
    gameDisplay.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            client.Close()
            server.Close()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pygame.quit()
            
    if pygame.mouse.get_pressed()[0]:
        jaja = True
    
    if jaja:
        break
    
    introSize = int(intro*0.3)
        
    introText = pygame.image.load("CDG_Images/intro.png")
    introText = pygame.transform.scale(introText, (500 + introSize, 250 + int(introSize/2)))
    gameDisplay.blit((introText), (190 - int(introSize/2), 250 - int(introSize/6)))
    
    
    si = pygame.Surface((800,600))  # the size of your rect
    si.set_alpha(alp - func(intro - 100))               # alpha level
    si.fill((0,0,0))
    su = pygame.Surface((800,600))  # the size of your rect
    su.set_alpha(func(intro - 250))               # alpha level
    su.fill((0,0,0))
            
    gameDisplay.blit(si, (0,0))
    gameDisplay.blit(su, (0,0))

            
    intro += 1
            
    if intro > 60*6:
        break
    click1 = False
    clock.tick(60)
    pygame.display.update()



#os.system('UDPgameServer.py')
while True:

    #posição inicial de cada nuvem
    cl_x1 = -60
    cl_x2 = 600
    cl_x3 = -60 + 60
    cl_x4 = -60 + 600
    cl_x5 = -60 -50
    cl_x6 = -60 +500
    cl_x7 = -60 +200
    cl_x8 = -60 +650
    cl_x9 = -60 - 100
    cl_x10 = -60 + 300
    cl_x11 = -60 - 200
    cl_x12 = -60 + 400
    
    
    TitleSize = 0
    
    n = 0
    
    original = 0
    right = 0
    left = 1
    
    j = 0.15
    
    contadorBlue = 0
    contadorRed = 0
    
    intensityLevel = 0
    
    click1 = False
    
    blurInt = 1
    
    nome = None
    ip = None
    
    cont = False
    
    
        
    
    
    #class Thing:
    
    #    def Object(self, img, position, size, orientation):
    #        self.img = pygame.image.load(img)
    #        if orientation == left:
    #            self.img = pygame.transform.flip(self.img, True, False)
    #        if size != original:
    #            self.img = pygame.transform.scale(self.img, size)
    #        gameDisplay.blit(self.img, position)
    #        
    #função de personagem
    def character(img, orientation):
    #    Thing.Object(img, position, 0, orientation)
        im = pygame.image.load(img)
        if orientation == left:
            im = pygame.transform.flip(im, True, False)
    #    if size != original:
    #        self.img = pygame.transform.scale(self.img, size)
#        gameDisplay.blit(im, position)    
        
            
    #load das imagens da corda
    c1 = pygame.image.load("CDG_Images/rope_igual.png")
    c1 = pygame.transform.scale(c1, (400, 20))
    c_e = pygame.image.load("CDG_Images/rope_esquerda1.png")
    c_e = pygame.transform.scale(c_e, (400, 20))
    c_d = pygame.image.load("CDG_Images/rope_direita1.png")
    c_d = pygame.transform.scale(c_d, (400, 20))
    
    #load das imagens da montanha
    mountain = pygame.image.load("CDG_Images/Pixel_mountain.png")
    mountain = pygame.transform.scale(mountain, (1000, 200))
    
    #load das imagens da montanha flutuante
    fmountain = pygame.image.load("CDG_Images/Pixel_fmountain.png")
    fmountain = pygame.transform.scale(fmountain, (200, 200))
    fmountain1 = pygame.transform.flip(fmountain, True, False)
    
    #load image of sun
    psun = pygame.image.load("CDG_Images/Pixel_sun.png")
    psun = pygame.transform.scale(psun, (800, 400))
    psunO = pygame.image.load("CDG_Images/Pixel_sun_orange.png")
    psunO = pygame.transform.scale(psunO, (800, 400))
    psunR = pygame.image.load("CDG_Images/Pixel_sun_strong.png")
    psunR = pygame.transform.scale(psunR, (800, 400))
    
    #load das imagens do QZ e PM do lado de cada time
    PM = pygame.image.load("CDG_Images/Pixel_PM.png")
    QZ = pygame.image.load("CDG_Images/Pixel_QZ.png")
    
    #load das imagens do botão START
    start0 = pygame.image.load("CDG_Images/START_0.png")
    start0 = pygame.transform.scale(start0, (200, 200))
    start1 = pygame.image.load("CDG_Images/START_1.png")
    start1 = pygame.transform.scale(start1, (200, 200))
    
    #load das imagens dos botões LOCAL e ONLINE
    localW = pygame.image.load("CDG_Images/Pixel_local_W.png")
    localW = pygame.transform.scale(localW, (600, 50))
    localY = pygame.image.load("CDG_Images/Pixel_local_Y.png")
    localY = pygame.transform.scale(localY, (600, 50))
    onlineW = pygame.image.load("CDG_Images/Pixel_online_W.png")
    onlineW = pygame.transform.scale(onlineW, (600, 50))
    onlineY = pygame.image.load("CDG_Images/Pixel_online_Y.png")
    onlineY = pygame.transform.scale(onlineY, (600, 50))
    
    #load das imagens do COUNTDOWN
    n3 = pygame.image.load("CDG_Images/No_3.png")
    n3 = pygame.transform.scale(n3, (300, 300))
    n2 = pygame.image.load("CDG_Images/No_2.png")
    n2 = pygame.transform.scale(n2, (300, 300))
    n1 = pygame.image.load("CDG_Images/No_1.png")
    n1 = pygame.transform.scale(n1, (300, 300))
    
    #load das imagens do YOU WIN!
    win_font = pygame.font.SysFont("pixelmix Regular", 100)
    wintext = win_font.render("YOU WIN!", True, (0,0,0))
    
    #load das imagens do BACKGROUND atrás das montanhas
    bgLow = pygame.image.load("CDG_Images/new_background.png")
    bgHigh = pygame.image.load("CDG_Images/background_hard.png")
    bgInsane = pygame.image.load("CDG_Images/background_insane.png")
    
    flagSize = (160, 240)
    
    redFlag0 = pygame.image.load("CDG_Images/redflag/flagred0.png")
    redFlag1 = pygame.image.load("CDG_Images/redflag/flagred1.png")
    redFlag2 = pygame.image.load("CDG_Images/redflag/flagred2.png")
    redFlag3 = pygame.image.load("CDG_Images/redflag/flagred3.png")
    redFlag4 = pygame.image.load("CDG_Images/redflag/flagred4.png")
    redFlag5 = pygame.image.load("CDG_Images/redflag/flagred5.png")
    redFlag6 = pygame.image.load("CDG_Images/redflag/flagred6.png")
    redFlag7 = pygame.image.load("CDG_Images/redflag/flagred7.png")
    redFlag0 = pygame.transform.flip(redFlag0, True, False)
    redFlag1 = pygame.transform.flip(redFlag1, True, False)
    redFlag2 = pygame.transform.flip(redFlag2, True, False)
    redFlag3 = pygame.transform.flip(redFlag3, True, False)
    redFlag4 = pygame.transform.flip(redFlag4, True, False)
    redFlag5 = pygame.transform.flip(redFlag5, True, False)
    redFlag6 = pygame.transform.flip(redFlag6, True, False)
    redFlag7 = pygame.transform.flip(redFlag7, True, False)
    redFlag0 = pygame.transform.scale(redFlag0, flagSize)
    redFlag1 = pygame.transform.scale(redFlag1, flagSize)
    redFlag2 = pygame.transform.scale(redFlag2, flagSize)
    redFlag3 = pygame.transform.scale(redFlag3, flagSize)
    redFlag4 = pygame.transform.scale(redFlag4, flagSize)
    redFlag5 = pygame.transform.scale(redFlag5, flagSize)
    redFlag6 = pygame.transform.scale(redFlag6, flagSize)
    redFlag7 = pygame.transform.scale(redFlag7, flagSize) 
    
    blueFlag0 = pygame.image.load("CDG_Images/blueflag/flagblue0.png")
    blueFlag1 = pygame.image.load("CDG_Images/blueflag/flagblue1.png")
    blueFlag2 = pygame.image.load("CDG_Images/blueflag/flagblue2.png")
    blueFlag3 = pygame.image.load("CDG_Images/blueflag/flagblue3.png")
    blueFlag4 = pygame.image.load("CDG_Images/blueflag/flagblue4.png")
    blueFlag5 = pygame.image.load("CDG_Images/blueflag/flagblue5.png")
    blueFlag6 = pygame.image.load("CDG_Images/blueflag/flagblue6.png")
    blueFlag7 = pygame.image.load("CDG_Images/blueflag/flagblue7.png")
    blueFlag0 = pygame.transform.scale(blueFlag0, flagSize)
    blueFlag1 = pygame.transform.scale(blueFlag1, flagSize)
    blueFlag2 = pygame.transform.scale(blueFlag2, flagSize)
    blueFlag3 = pygame.transform.scale(blueFlag3, flagSize)
    blueFlag4 = pygame.transform.scale(blueFlag4, flagSize)
    blueFlag5 = pygame.transform.scale(blueFlag5, flagSize)
    blueFlag6 = pygame.transform.scale(blueFlag6, flagSize)
    blueFlag7 = pygame.transform.scale(blueFlag7, flagSize) 
    
    def blurSurf(surface, amt):

        if amt < 1.0:
            raise ValueError("Arg 'amt' must be greater than 1.0, passed in value is %s"%amt)
        scale = 1.0/float(amt)
        surf_size = surface.get_size()
        scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
        surf = pygame.transform.smoothscale(surface, scale_size)
        surf = pygame.transform.smoothscale(surf, surf_size)
        return surf
        
    
    
    #funções para inserir cada jogador virado para a direita na tela

    marrom1 = pygame.image.load("CDG_Images/char1.1.png")
    marrom2 = pygame.image.load("CDG_Images/char1.2.png")
    marrom3 = pygame.image.load("CDG_Images/char1.3.png")
    marrom4 = pygame.image.load("CDG_Images/char1.4.png")
    amarelo1 = pygame.image.load("CDG_Images/char2.1.png")
    amarelo2 = pygame.image.load("CDG_Images/char2.2.png")
    amarelo3 = pygame.image.load("CDG_Images/char2.3.png")
    amarelo4 = pygame.image.load("CDG_Images/char2.4.png")
    rosa1 = pygame.image.load("CDG_Images/char3.1.png")
    rosa2 = pygame.image.load("CDG_Images/char3.2.png")
    rosa3 = pygame.image.load("CDG_Images/char3.3.png")
    rosa4 = pygame.image.load("CDG_Images/char3.4.png")
    jerry1 = pygame.image.load("CDG_Images/char4.1.png")
    jerry2 = pygame.image.load("CDG_Images/char4.2.png")
    jerry3 = pygame.image.load("CDG_Images/char4.3.png")
    jerry4 = pygame.image.load("CDG_Images/char4.4.png")
    ayres1 = pygame.image.load("CDG_Images/char5.1.png")
    ayres2 = pygame.image.load("CDG_Images/char5.2.png")
    ayres3 = pygame.image.load("CDG_Images/char5.3.png")
    ayres4 = pygame.image.load("CDG_Images/char5.4.png")
    hage1 = pygame.image.load("CDG_Images/char6.1.png")
    hage2 = pygame.image.load("CDG_Images/char6.2.png")
    hage3 = pygame.image.load("CDG_Images/char6.3.png")
    hage4 = pygame.image.load("CDG_Images/char6.4.png")
    batman1 = pygame.image.load("CDG_Images/char7.1.png")
    batman2 = pygame.image.load("CDG_Images/char7.2.png")
    batman3 = pygame.image.load("CDG_Images/char7.3.png")
    batman4 = pygame.image.load("CDG_Images/char7.4.png")
    leprichon1 = pygame.image.load("CDG_Images/char8.1.png")
    leprichon2 = pygame.image.load("CDG_Images/char8.2.png")
    leprichon3 = pygame.image.load("CDG_Images/char8.3.png")
    leprichon4 = pygame.image.load("CDG_Images/char8.4.png")
    dilma1 = pygame.image.load("CDG_Images/char9.1.png")
    dilma2 = pygame.image.load("CDG_Images/char9.2.png")
    dilma3 = pygame.image.load("CDG_Images/char9.3.png")
    dilma4 = pygame.image.load("CDG_Images/char9.4.png")
    fred1 = pygame.image.load("CDG_Images/char10.1.png")
    fred2 = pygame.image.load("CDG_Images/char10.2.png")
    fred3 = pygame.image.load("CDG_Images/char10.3.png")
    fred4 = pygame.image.load("CDG_Images/char10.4.png")
    super1 = pygame.image.load("CDG_Images/char11.1.png")
    super2 = pygame.image.load("CDG_Images/char11.2.png")
    super3 = pygame.image.load("CDG_Images/char11.3.png")
    super4 = pygame.image.load("CDG_Images/char11.4.png")  
    gui1 = pygame.image.load("CDG_Images/char12.1.png")
    gui2 = pygame.image.load("CDG_Images/char12.2.png")
    gui3 = pygame.image.load("CDG_Images/char12.3.png")
    gui4 = pygame.image.load("CDG_Images/char12.4.png")
    goku1 = pygame.image.load("CDG_Images/char13.1.png")
    goku2 = pygame.image.load("CDG_Images/char13.2.png")
    goku3 = pygame.image.load("CDG_Images/char13.3.png")
    goku4 = pygame.image.load("CDG_Images/char13.4.png")
    obama1 = pygame.image.load("CDG_Images/char14.1.png")
    obama2 = pygame.image.load("CDG_Images/char14.2.png")
    obama3 = pygame.image.load("CDG_Images/char14.3.png")
    obama4 = pygame.image.load("CDG_Images/char14.4.png")
    luscas1 = pygame.image.load("CDG_Images/char15.1.png")
    luscas2 = pygame.image.load("CDG_Images/char15.2.png")
    luscas3 = pygame.image.load("CDG_Images/char15.3.png")
    luscas4 = pygame.image.load("CDG_Images/char15.4.png")
    terminator1 = pygame.image.load("CDG_Images/char16.1.png")
    terminator2 = pygame.image.load("CDG_Images/char16.2.png")
    terminator3 = pygame.image.load("CDG_Images/char16.3.png")
    terminator4 = pygame.image.load("CDG_Images/char16.4.png")
    ash1 = pygame.image.load("CDG_Images/char17.1.png")
    ash2 = pygame.image.load("CDG_Images/char17.2.png")
    ash3 = pygame.image.load("CDG_Images/char17.3.png")
    ash4 = pygame.image.load("CDG_Images/char17.4.png")
    sakura1 = pygame.image.load("CDG_Images/char18.1.png")
    sakura2 = pygame.image.load("CDG_Images/char18.2.png")
    sakura3 = pygame.image.load("CDG_Images/char18.3.png")
    sakura4 = pygame.image.load("CDG_Images/char18.4.png")
    link1 = pygame.image.load("CDG_Images/char19.1.png")
    link2 = pygame.image.load("CDG_Images/char19.2.png")
    link3 = pygame.image.load("CDG_Images/char19.3.png")
    link4 = pygame.image.load("CDG_Images/char19.4.png")    
    
    
    marrom10 = pygame.transform.flip(marrom1, True, False)
    marrom20 = pygame.transform.flip(marrom2, True, False)
    marrom30 = pygame.transform.flip(marrom3, True, False)
    marrom40 = pygame.transform.flip(marrom4, True, False)
    amarelo10 = pygame.transform.flip(amarelo1, True, False)
    amarelo20 = pygame.transform.flip(amarelo2, True, False)
    amarelo30 = pygame.transform.flip(amarelo3, True, False)
    amarelo40 = pygame.transform.flip(amarelo4, True, False)
    rosa10 = pygame.transform.flip(rosa1, True, False)
    rosa20 = pygame.transform.flip(rosa2, True, False)
    rosa30 = pygame.transform.flip(rosa3, True, False)
    rosa40 = pygame.transform.flip(rosa4, True, False)
    jerry10 = pygame.transform.flip(jerry1, True, False)
    jerry20 = pygame.transform.flip(jerry2, True, False)
    jerry30 = pygame.transform.flip(jerry3, True, False)
    jerry40 = pygame.transform.flip(jerry4, True, False)
    ayres10 = pygame.transform.flip(ayres1, True, False)
    ayres20 = pygame.transform.flip(ayres2, True, False)
    ayres30 = pygame.transform.flip(ayres3, True, False)
    ayres40 = pygame.transform.flip(ayres4, True, False)
    hage10 = pygame.transform.flip(hage1, True, False)
    hage20 = pygame.transform.flip(hage2, True, False)
    hage30 = pygame.transform.flip(hage3, True, False)
    hage40 = pygame.transform.flip(hage4, True, False)
    batman10 = pygame.transform.flip(batman1, True, False)
    batman20 = pygame.transform.flip(batman2, True, False)
    batman30 = pygame.transform.flip(batman3, True, False)
    batman40 = pygame.transform.flip(batman4, True, False)
    leprichon10 = pygame.transform.flip(leprichon1, True, False)
    leprichon20 = pygame.transform.flip(leprichon2, True, False)
    leprichon30 = pygame.transform.flip(leprichon3, True, False)
    leprichon40 = pygame.transform.flip(leprichon4, True, False)
    dilma10 = pygame.transform.flip(dilma1, True, False)
    dilma20 = pygame.transform.flip(dilma2, True, False)
    dilma30 = pygame.transform.flip(dilma3, True, False)
    dilma40 = pygame.transform.flip(dilma4, True, False)
    fred10 = pygame.transform.flip(fred1, True, False)
    fred20 = pygame.transform.flip(fred2, True, False)
    fred30 = pygame.transform.flip(fred3, True, False)
    fred40 = pygame.transform.flip(fred4, True, False)
    super10 = pygame.transform.flip(super1, True, False)
    super20 = pygame.transform.flip(super2, True, False)
    super30 = pygame.transform.flip(super3, True, False)
    super40 = pygame.transform.flip(super4, True, False)
    gui10 = pygame.transform.flip(gui1, True, False)
    gui20 = pygame.transform.flip(gui2, True, False)
    gui30 = pygame.transform.flip(gui3, True, False)
    gui40 = pygame.transform.flip(gui4, True, False)
    goku10 = pygame.transform.flip(goku1, True, False)
    goku20 = pygame.transform.flip(goku2, True, False)
    goku30 = pygame.transform.flip(goku3, True, False)
    goku40 = pygame.transform.flip(goku4, True, False)
    obama10 = pygame.transform.flip(obama1, True, False)
    obama20 = pygame.transform.flip(obama2, True, False)
    obama30 = pygame.transform.flip(obama3, True, False)
    obama40 = pygame.transform.flip(obama4, True, False)
    luscas10 = pygame.transform.flip(luscas1, True, False)
    luscas20 = pygame.transform.flip(luscas2, True, False)
    luscas30 = pygame.transform.flip(luscas3, True, False)
    luscas40 = pygame.transform.flip(luscas4, True, False)
    terminator10 = pygame.transform.flip(terminator1, True, False)
    terminator20 = pygame.transform.flip(terminator2, True, False)
    terminator30 = pygame.transform.flip(terminator3, True, False)
    terminator40 = pygame.transform.flip(terminator4, True, False)
    ash10 = pygame.transform.flip(ash1, True, False)
    ash20 = pygame.transform.flip(ash2, True, False)
    ash30 = pygame.transform.flip(ash3, True, False)
    ash40 = pygame.transform.flip(ash4, True, False)
    sakura10 = pygame.transform.flip(sakura1, True, False)
    sakura20 = pygame.transform.flip(sakura2, True, False)
    sakura30 = pygame.transform.flip(sakura3, True, False)
    sakura40 = pygame.transform.flip(sakura4, True, False)
    link10 = pygame.transform.flip(link1, True, False)
    link20 = pygame.transform.flip(link2, True, False)
    link30 = pygame.transform.flip(link3, True, False)
    link40 = pygame.transform.flip(link4, True, False)
    
    marrom = [marrom1, marrom2, marrom3, marrom4, marrom10, marrom20, marrom30, marrom40]
    rosa = [rosa1, rosa2, rosa3, rosa4, rosa10, rosa20, rosa30, rosa40]
    amarelo = [amarelo1, amarelo2, amarelo3, amarelo4, amarelo10, amarelo20, amarelo30, amarelo40]
    fred = [fred1, fred2, fred3, fred4, fred10, fred20, fred30, fred40]        
    gui = [gui1, gui2, gui3, gui4, gui10, gui20, gui30, gui40]
    ayres = [ayres1, ayres2, ayres3, ayres4, ayres10, ayres20, ayres30, ayres40]
    hage = [hage1, hage2, hage3, hage4, hage10, hage20, hage30, hage40]
    superman = [super1, super2, super3, super4, super10, super20, super30, super40]
    jerry = [jerry1, jerry2, jerry3, jerry4, jerry10, jerry20, jerry30, jerry40]
    goku = [goku1, goku2, goku3, goku4, goku10, goku20, goku30, goku40]
    batman = [batman1, batman2, batman3, batman4, batman10, batman20, batman30, batman40]
    leprichon = [leprichon1, leprichon2, leprichon3, leprichon4, leprichon10, leprichon20, leprichon30, leprichon40]
    obama = [obama1, obama2, obama3, obama4, obama10, obama20, obama30, obama40]
    luscas = [luscas1, luscas2, luscas3, luscas4, luscas10, luscas20, luscas30, luscas40]
    terminator = [terminator1, terminator2, terminator3, terminator4, terminator10, terminator20, terminator30, terminator40]
    ash = [ash1, ash2, ash3, ash4, ash10, ash20, ash30, ash40]
    sakura = [sakura1, sakura2, sakura3, sakura4, sakura10, sakura20, sakura30, sakura40]
    link = [link1, link2, link3, link4, link10, link20, link30, link40]
    dilma = [dilma1, dilma2, dilma3, dilma4, dilma10, dilma20, dilma30, dilma40]
    
    
        
    #funções para inserir cada imagem da corda na tela
    def corda_i(x, y):
        gameDisplay.blit((c1), (x, y))
    def corda_e(x, y):
        gameDisplay.blit((c_e), (x, y))
    def corda_d(x, y):
        gameDisplay.blit((c_d), (x, y))
        
    #função para inserir a montanha na tela    
    def mountain_bg(x, y):
        gameDisplay.blit((mountain), (x, y))
        
    def floatMountain(x, y):
        gameDisplay.blit((fmountain), (x, y))
    def floatMountain1(x, y):
        gameDisplay.blit((fmountain1), (x, y))
        
    def sun(x, y):
        gameDisplay.blit((psun), (x, y))
    def sunO(x, y):
        gameDisplay.blit((psunO), (x, y))
    def sunR(x, y):
        gameDisplay.blit((psunR), (x, y))
        
    def flagR0(x):
        gameDisplay.blit((redFlag0), (x))
    def flagR1(x):
        gameDisplay.blit((redFlag1), (x))
    def flagR2(x):
        gameDisplay.blit((redFlag2), (x))
    def flagR3(x):
        gameDisplay.blit((redFlag3), (x))
    def flagR4(x):
        gameDisplay.blit((redFlag4), (x))
    def flagR5(x):
        gameDisplay.blit((redFlag5), (x))
    def flagR6(x):
        gameDisplay.blit((redFlag6), (x))
    def flagR7(x):
        gameDisplay.blit((redFlag7), (x))
        
    def flagB0(x):
        gameDisplay.blit((blueFlag0), (x))
    def flagB1(x):
        gameDisplay.blit((blueFlag1), (x))
    def flagB2(x):
        gameDisplay.blit((blueFlag2), (x))
    def flagB3(x):
        gameDisplay.blit((blueFlag3), (x))
    def flagB4(x):
        gameDisplay.blit((blueFlag4), (x))
    def flagB5(x):
        gameDisplay.blit((blueFlag5), (x))
    def flagB6(x):
        gameDisplay.blit((blueFlag6), (x))
    def flagB7(x):
        gameDisplay.blit((blueFlag7), (x))
        
    #função para inserir as nuvens na tela    
    #def cloud1(x, y):
    #    gameDisplay.blit(pygame.transform.scale((pygame.image.load("CDG_Images/Pixel_cloud1.png")), (400, 400)), (x, y))
    
    #função para inserir as nuvens novas na tela        
    def cloud1(x, y):
        cld1 = pygame.image.load("CDG_Images/fred_cloud1.png")
        cld1 = pygame.transform.flip(cld1, True, False)
        cld1 = pygame.transform.scale((cld1), (500, 350))
        gameDisplay.blit(cld1, (x, y))
    def cloud2(x, y):
        cld1 = pygame.image.load("CDG_Images/fred_cloud2.png")
        cld1 = pygame.transform.flip(cld1, True, False)
        cld1 = pygame.transform.scale((cld1), (300, 150))
        gameDisplay.blit(cld1, (x, y))
    def cloud11(x, y):
        cld1 = pygame.image.load("CDG_Images/fred_cloud3.png")
        cld1 = pygame.transform.flip(cld1, True, False)
        cld1 = pygame.transform.scale((cld1), (500, 350))
        gameDisplay.blit(cld1, (x - 10, y + 20))
    def cloud21(x, y):
        cld1 = pygame.image.load("CDG_Images/fred_cloud4.png")
        cld1 = pygame.transform.flip(cld1, True, False)
        cld1 = pygame.transform.scale((cld1), (300, 150))
        gameDisplay.blit(cld1, (x - 10, y + 20))
    def cloud12(x, y):
        cld1 = pygame.image.load("CDG_Images/fred_cloud6.png")
        cld1 = pygame.transform.flip(cld1, True, False)
        cld1 = pygame.transform.scale((cld1), (500, 350))
        gameDisplay.blit(cld1, (x - 10, y + 20))
    def cloud22(x, y):
        cld1 = pygame.image.load("CDG_Images/fred_cloud5.png")
        cld1 = pygame.transform.flip(cld1, True, False)
        cld1 = pygame.transform.scale((cld1), (300, 150))
        gameDisplay.blit(cld1, (x - 10, y + 20))
        
    #função para inserir o QZ e o PM na tela        
    def PM_bg(x, y):
        gameDisplay.blit((PM), (x, y))
    def QZ_bg(x, y):
        gameDisplay.blit((QZ), (x, y))
        
    #função para inserir o título na tela        
    def TugWar(x, y):
        gameDisplay.blit(blurSurf(Tug, blurInt), (x, y))
    
    #funções para inserir o COUNTDOWN na tela        
    def N3(x, y):
        gameDisplay.blit((n3), (x, y))
    def N2(x, y):
        gameDisplay.blit((n2), (x, y))
    def N1(x, y):
        gameDisplay.blit((n1), (x, y))
        
    #função para inserir qualquer texto de tamanho 20 na tela    
    def anyText(x, y, txt, colour):
        fonte = pygame.font.SysFont("pixelmix Regular", 20)
        ay = fonte.render(txt, True, colour)
        gameDisplay.blit((ay), (x, y))
    
    #função para inserir qualquer texto de tamanho 40 na tela        
    def anyText40(x, y, txt, colour):
        fonte = pygame.font.SysFont("pixelmix Regular", 40)
        ay = fonte.render(txt, True, colour)
        gameDisplay.blit(blurSurf(ay, blurInt), (x, y))
        
    #função para inserir a mensagem WIN na tela        
    def win(x, y, txt, colour):
    #    gameDisplay.blit((win_bg), (x, y))
        win_font = pygame.font.SysFont("pixelmix Regular", 100)
        wintext = win_font.render(txt, True, colour)
        gameDisplay.blit((wintext), (x + 150, y + 200))
        
    #função para inserir o nível de intensidade na tela        
    def intensity(x, y, txt, lvl):
        if lvl == 0:
            fo = pygame.font.SysFont("pixelmix Regular", 25)
            inten = fo.render(txt, True, (255,255,255))
            gameDisplay.blit((inten), (x + 130, y))
        if lvl == 1:
            fo = pygame.font.SysFont("pixelmix Regular", 35)
            inten = fo.render(txt, True, (200,150,150))
            gameDisplay.blit((inten), (x + 50 , y - 5))
        if lvl == 2:
            fo = pygame.font.SysFont("pixelmix Regular", 50)
            inten = fo.render(txt, True, (100,0,0))
            gameDisplay.blit((inten), (x - 90, y - 10))
            
    #funções para inserir os BACKGROUNDS na tela            
    def bgLOW(x, y):
        gameDisplay.blit((bgLow), (x, y))
    def bgHIGH(x, y):
        gameDisplay.blit((bgHigh), (x, y))
    def bgINSANE(x, y):
        gameDisplay.blit((bgInsane), (x, y))

    
    #Valor inicial da barra de progresso
    px = 200
    
    
    Tela = 2000
    
    #função para mover a camera do título até os jogadores
    def camera(x):
        cam = Tela*(1/(1 + math.e**-(0.7*x)))
        return -cam
    
    #função para mover a tela WIN
    def camera_win(x):
        cam = 600*(1/(1 + math.e**-(2*x)))
        return -cam
    
    #valor inicial para as funções
    x = -12
    
    select0 = False
    select1 = False
    select10 = False
    select11 = False
    enter = False
    start = False
    startonline = False
    team = ''
    selectTeam = False
    frameCounter = 0
    
    
    
    personagem_pos1x = 185,206 + 25 + camera(x) *1.5 + 1000 + Tela  +  TitleSize/2
    personagem_pos1y = 185,206 + 25 + camera(x) *1.5 + 1000 + Tela  +  TitleSize/2
    personagem_pos2x = 567, 206 + 25 + camera(x) *1.5 + 1000 + Tela  +  TitleSize/2
    personagem_pos2y = 567, 206 + 25 + camera(x) *1.5 + 1000 + Tela  +  TitleSize/2
    
    pixelFont = pygame.font.SysFont("pixelmix Regular", 40)
    white = (255,255,255)
    question = eztextNum.Input(maxlength=20, color=white, prompt='IP: ')
    name = eztext.Input(maxlength=20, color=white, prompt='USERNAME: ')    
    
    ##################################################################################################
    
    #loop MENU
    while not select0 or not select1:
        gameDisplay.fill((121, 202, 249))
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                client.Close()
                server.Close()
            
            if event.type == pygame.MOUSEBUTTONUP:
                click1 = True
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                pygame.quit()              
                
        cloud2(cl_x3, -100 + camera(x) + Tela - 2000)
        cloud1(cl_x4, 0 + camera(x) + Tela - 2000)
        cloud2(cl_x5, -150 + camera(x) + Tela - 1600)
        cloud1(cl_x6, 50 + camera(x) + Tela - 1600)
        
        cl_x1 += 0.3    
        cl_x2 += 0.3
        cl_x3 += 0.3    
        cl_x4 += 0.3
        cl_x5 += 0.3
        cl_x6 += 0.3
        cl_x7 += 0.3
        cl_x8 += 0.3
        cl_x9 += 0.3
        cl_x10 += 0.3
        cl_x11 += 0.3
        cl_x12 += 0.3
        
        if cl_x1 > 805:
            cl_x1 = -400
        if cl_x2 > 805:
            cl_x2 = -400
        if cl_x3 > 805:
            cl_x3 = -400
        if cl_x4 > 805:
            cl_x4 = -400
        if cl_x5 > 805:
            cl_x5 = -400
        if cl_x6 > 805:
            cl_x6 = -400
        if cl_x7 > 805:
            cl_x7 = -400
        if cl_x8 > 805:
            cl_x8 = -400
        if cl_x9 > 805:
            cl_x9 = -400
        if cl_x10 > 805:
            cl_x10 = -400
        if cl_x11 > 805:
            cl_x11 = -400
        if cl_x12 > 805:
            cl_x12 = -400
            
        
        Tug = pygame.image.load("CDG_Images/Tug_War.png")
        Tug = pygame.transform.scale(Tug, (800 + TitleSize, 800 + TitleSize))
                
        TitleSize = int((15*(1+math.sin(2*3.14*n*0.01)))*0.5)
        n -= 1
              
        TugWar(40 - TitleSize/3, -200 - TitleSize/3)
        
        if select1 == False and 300 > mouse_pos[0] > 120 and 570 > mouse_pos[1] > 520:
            gameDisplay.blit(localY,(120, 520))	
            if click1:
                start = True
                click1 = False
                break
        elif select1 == False:
            gameDisplay.blit(localW,(120, 520))
            
        if select1 == False and 700 > mouse_pos[0] > 500 and 570 > mouse_pos[1] > 520:
            gameDisplay.blit(onlineY,(500, 520))	
            if click1:
                select1 = True
                click1 = False
                
                
        elif select1 == False:
            gameDisplay.blit(onlineW,(500, 520))
            
        if frameCounter < 300:
            blackout = pygame.image.load("CDG_Images/blackout.png")
            gameDisplay.blit(blackout, (-200 + frameCounter*30 ,0))
        
        if select1 == True:
            name.set_pos(100, 520)
            name.set_font(pixelFont)
            name.draw(gameDisplay)
            name.update(pygame.event.get())
            
            #Valor do NOME
            
            if name.enter:
                nome = name.value
                client.setName(nome)
                name.enter = False
                break
            
        frameCounter += 1
        click1 = False
        pygame.display.update()
        
        
    #######################################################    
        
    blockThread = blockThread2 = timeout = done = False

    #loop ONLINE
    while select1:
        gameDisplay.fill((121, 202, 249))
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                client.Close()
                server.Close()
            if event.type == pygame.MOUSEBUTTONUP:
                click1 = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pygame.quit()
    
                
        cloud2(cl_x3, -100 + camera(x) + Tela - 2000)
        cloud1(cl_x4, 0 + camera(x) + Tela - 2000)
        cloud2(cl_x5, -150 + camera(x) + Tela - 1600)
        cloud1(cl_x6, 50 + camera(x) + Tela - 1600)
        
        cl_x1 += 0.3    
        cl_x2 += 0.3
        cl_x3 += 0.3
        cl_x4 += 0.3
        cl_x5 += 0.3
        cl_x6 += 0.3
        cl_x7 += 0.3
        cl_x8 += 0.3
        cl_x9 += 0.3
        cl_x10 += 0.3
        cl_x11 += 0.3
        cl_x12 += 0.3
        
        if cl_x1 > 805:
            cl_x1 = -400
        if cl_x2 > 805:
            cl_x2 = -400
        if cl_x3 > 805:
            cl_x3 = -400
        if cl_x4 > 805:
            cl_x4 = -400
        if cl_x5 > 805:
            cl_x5 = -400
        if cl_x6 > 805:
            cl_x6 = -400
        if cl_x7 > 805:
            cl_x7 = -400
        if cl_x8 > 805:
            cl_x8 = -400
        if cl_x9 > 805:
            cl_x9 = -400
        if cl_x10 > 805:
            cl_x10 = -400
        if cl_x11 > 805:
            cl_x11 = -400
        if cl_x12 > 805:
            cl_x12 = -400
            
        
        Tug = pygame.image.load("CDG_Images/Tug_War.png")
        Tug = pygame.transform.scale(Tug, (800 + TitleSize, 800 + TitleSize))
                
        TitleSize = int((15*(1+math.sin(2*3.14*n*0.01)))*0.5)
        n -= 1        
              
        TugWar(40 - TitleSize/3, -200 - TitleSize/3)        
        
        #condições para o botão CREATE        
        if select11 == False and 300 > mouse_pos[0] > 120 and 570 > mouse_pos[1] > 520:
            anyText40(120, 520, "CREATE", (255,255,0))	
            if click1:
                select10 = True
                click1 = False
                break
                
        elif select11 == False:
            anyText40(120, 520, "CREATE", (255,255,255))	
        
        #condições para o botão JOIN     
        if select11 == False and 620 > mouse_pos[0] > 500 and 570 > mouse_pos[1] > 520:
            anyText40(500, 520, "JOIN", (255,255,0))	
            if click1:
                select11 = True
                click1 = False
                
        elif select11 == False:
            anyText40(500, 520, "JOIN", (255,255,255))        
        
        #Tela para inserir IP
        if select11 == True:
            question.set_pos(200, 520)
            question.set_font(pixelFont)
            question.draw(gameDisplay)
            question.update(pygame.event.get())
            
            #Valor do IP
            if question.enter:
                pesquisarIP = True

                if not blockThread:
                    ip = question.value
                    client.setHost(ip)  

                    def startLoop():
                        global timeout
                        global blockThread
                        global done

                        while True:
                            if not blockThread:
                                def start():
                                    client.clientStart()
                                clientStartThread = Thread(target=start)
                                clientStartThread.start()
                            
                            anyText40(200, 300, "Searching Server...", (255,255,255))
                            
                            if client.Status() == 'Connected' or client.Status() == 'Connected as principal':
                                timeout = False
                                break
                            elif client.Status() == 'Timeout':
                                timeout = True
                                break
                            blockThread = 1
                        done = True

                if not blockThread2:
                    LoopStartThread = Thread(target=startLoop)
                    LoopStartThread.start()
                    blockThread2 = 1
                
                if not timeout and done:
                    select10 = False
                    select11 = True
                    break

                elif timeout and done:
                    break                   
    
        pygame.display.update() 
        
###############################################################################
    selectChar1 = startedOnce = threadOnce3 =  threadDone3 = False
    team = 'none'
    client.setTeam(team)
    LetsPlay = False
    ThreadStartOnce = False
    ThreadStartOnce10 = False
    #loop CREATE
    while select10:
        gameDisplay.fill((121, 202, 249))
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if not startedOnce:
            myIp = client.showMyHost()
            def StartTheServer():
                server.serverStart()

            startedOnce = True

            def startLoop():
                global timeout
                global done
                global myIp

                startedOnce = False

                while True:
                    myIp = client.showMyHost()
                    if not startedOnce:
                        client.setHost(myIp)
                        def start():
                            client.clientStart()
                        clientStartThread = Thread(target=start)
                        clientStartThread.start()
                    
                    anyText40(200, 300, "Searching Server...", (255,255,255))
                    
                    if client.Status() == 'Connected' or client.Status() == 'Connected as principal':
                        timeout = False
                        break
                    elif client.Status() == 'Timeout':
                        timeout = True
                        break
                    startedOnce = True
                done = True                    
                pygame.display.update()

            serverThread = Thread(target=StartTheServer)
            LoopStartThread = Thread(target=startLoop)            
            serverThread.start()
            LoopStartThread.start()
            startedOnce = True 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                client.Close()
                server.Close()
            if event.type == pygame.MOUSEBUTTONUP:
                click1 = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pygame.quit()
        
        row1 = (270 > mouse_pos[1] > 200)
        row2 = (370 > mouse_pos[1] > 300)
        row3 = (470 > mouse_pos[1] > 400)
        row4 = (570 > mouse_pos[1] > 500)
        r1 = 200
        r2 = 300
        r3 = 400
        r4 = 500
        
        column1 = (180 > mouse_pos[0] > 135)
        column2 = (300 > mouse_pos[0] > 255)
        column3 = (300 + 120 > mouse_pos[0] > 255 + 120)
        column4 = (300 + 120 + 120 > mouse_pos[0] > 255 + 120 + 120)
        column5 = (300 + 120 + 120 + 120 > mouse_pos[0] > 255 + 120 + 120 + 120)
        col1 = 135
        col2 = 255
        col3 = 255 + 120
        col4 = 255 + 120 + 120
        col5 = 255 + 120 + 120 + 120
    
                
        cloud2(cl_x3, -100 + camera(x) + Tela - 2000)
        cloud1(cl_x4, 0 + camera(x) + Tela - 2000)
        cloud2(cl_x5, -150 + camera(x) + Tela - 1600)
        cloud1(cl_x6, 50 + camera(x) + Tela - 1600)
        
        cl_x1 += 0.3    
        cl_x2 += 0.3
        cl_x3 += 0.3
        cl_x4 += 0.3
        cl_x5 += 0.3
        cl_x6 += 0.3
        cl_x7 += 0.3
        cl_x8 += 0.3
        cl_x9 += 0.3
        cl_x10 += 0.3
        cl_x11 += 0.3
        cl_x12 += 0.3
        
        if cl_x1 > 805:
            cl_x1 = -400
        if cl_x2 > 805:
            cl_x2 = -400
        if cl_x3 > 805:
            cl_x3 = -400
        if cl_x4 > 805:
            cl_x4 = -400
        if cl_x5 > 805:
            cl_x5 = -400
        if cl_x6 > 805:
            cl_x6 = -400
        if cl_x7 > 805:
            cl_x7 = -400
        if cl_x8 > 805:
            cl_x8 = -400
        if cl_x9 > 805:
            cl_x9 = -400
        if cl_x10 > 805:
            cl_x10 = -400
        if cl_x11 > 805:
            cl_x11 = -400
        if cl_x12 > 805:
            cl_x12 = -400
        
        if cont == False:
            anyText40(250, 100, 'IP: {0}'.format(myIp), (255, 255, 255))
        
        if cont == False and 650 > mouse_pos[0] > 510 and 500 > mouse_pos[1] > 450:
            anyText40(510, 450, "TEAM SELECT", (255,255,0))	
            if click1:
                cont = True
                click1 = False
                client.closeConnection()

        elif cont == False:
            anyText40(510, 450, "TEAM SELECT", (255,255,255))	

        if cont:
            if selectTeam == False and 290 > mouse_pos[0] > 200 and 315 > mouse_pos[1] > 275:
                anyText40(200, 275, "RED", (255,0,0))	
                if click1:
                    selectTeam = True
                    team = 'red'
                    click1 = False
                    
            elif selectTeam == False:
                anyText40(200, 275, "RED", (255,255,255))	
            
            if selectTeam == False and 700 > mouse_pos[0] > 580 and 315 > mouse_pos[1] > 275:
                anyText40(580, 275, "BLUE", (0,0,255))	
                if click1:
                    selectTeam = True
                    team = 'blue'
                    click1 = False
    
            elif selectTeam == False:
                anyText40(580, 275, "BLUE", (255,255,255))
            
            if selectTeam == False and 530 > mouse_pos[0] > 350 and 415 > mouse_pos[1] > 375:
                anyText40(350, 375, "RANDOM", (255,255,0))
                if click1:
                    selectTeam = True
                    team = 'random'
                    
                    click1 = False
                    
            elif selectTeam == False:
                anyText40(350, 375, "RANDOM", (255,255,255))

            if not selectChar1:
            
                if row1 and column1:
                    gameDisplay.blit(marrom[2], (col1,r1))	
                    if click1:
                        escolha1 = marrom
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(marrom[0], (col1,r1)) 
                    
                if row1 and column2:
                    gameDisplay.blit(rosa[2], (col2,r1))	
                    if click1:
                        escolha1 = rosa
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(rosa[0], (col2,r1)) 
                    
                if row1 and column3:
                    gameDisplay.blit(amarelo[2], (col3,r1))	
                    if click1:
                        escolha1 = amarelo
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(amarelo[0], (col3,r1)) 
                    
                if row1 and column4:
                    gameDisplay.blit(jerry[2], (col4,r1))	
                    if click1:
                        escolha1 = jerry
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(jerry[0], (col4,r1)) 
                    
                if row1 and column5:
                    gameDisplay.blit(obama[2], (col5,r1))	
                    if click1:
                        escolha1 = obama
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(obama[0], (col5,r1)) 
                    
                if row2 and column1:
                    gameDisplay.blit(fred[2], (col1,r2))	
                    if click1:
                        escolha1 = fred
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(fred[0], (col1,r2)) 
                    
                if row2 and column2:
                    gameDisplay.blit(luscas[2], (col2,r2))	
                    if click1:
                        escolha1 = luscas
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(luscas[0], (col2,r2))
                    
                if row2 and column3:
                    gameDisplay.blit(gui[2], (col3,r2))	
                    if click1:
                        escolha1 = gui
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(gui[0], (col3,r2)) 
                    
                if row2 and column4:
                    gameDisplay.blit(ayres[2], (col4,r2))	
                    if click1:
                        escolha1 = ayres
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(ayres[0], (col4,r2)) 
                    
                if row2 and column5:
                    gameDisplay.blit(hage[2], (col5,r2))	
                    if click1:
                        escolha1 = hage
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(hage[0], (col5,r2)) 
                    
                if row3 and column1:
                    gameDisplay.blit(superman[2], (col1,r3))	
                    if click1:
                        escolha1 = superman
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(superman[0], (col1,r3)) 
                    
                if row3 and column2:
                    gameDisplay.blit(batman[2], (col2,r3))	
                    if click1:
                        escolha1 = batman
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(batman[0], (col2,r3))
                    
                if row3 and column3:
                    gameDisplay.blit(link[2], (col3,r3))	
                    if click1:
                        escolha1 = link
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(link[0], (col3,r3))
                    
                if row3 and column4:
                    gameDisplay.blit(goku[2], (col4,r3))	
                    if click1:
                        escolha1 = goku
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(goku[0], (col4,r3))
                    
                if row3 and column5:
                    gameDisplay.blit(ash[2], (col5,r3))	
                    if click1:
                        escolha1 = ash
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(ash[0], (col5,r3))
                    
                if row4 and column1:
                    gameDisplay.blit(dilma[2], (col1,r4))	
                    if click1:
                        escolha1 = dilma
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(dilma[0], (col1,r4)) 
                    
                if row4 and column2:
                    gameDisplay.blit(terminator[2], (col2,r4))	
                    if click1:
                        escolha1 = terminator
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(terminator[0], (col2,r4))
                    
                if row4 and column3:
                    gameDisplay.blit(sakura[2], (col3,r4))	
                    if click1:
                        escolha1 = sakura
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(sakura[0], (col3,r4))
                    
                if row4 and column4:
                    gameDisplay.blit(leprichon[2], (col4,r4))	
                    if click1:
                        escolha1 = leprichon
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(leprichon[0], (col4,r4))
                    
                if row4 and column5:
                    gameDisplay.blit(ash[2], (col5,r4))	
                    if click1:
                        escolha1 = ash
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(ash[0], (col5,r4))
            
            if selectTeam and selectChar1:
                if team != 'none':
                    client.setTeam(team)

                # if not threadOnce3:
                #     def sendAsPrincipal():
                #         global threadDone3
                #         client.NameSend()
                #         threadDone3 = True

                #     AsPrincipal = Thread(target=sendAsPrincipal)
                #     AsPrincipal.start()
                #     threadOnce3 = True

                anyText40(230, 10, "CREATE GAME", (255, 255, 255))
                anyText40(420, 100, 'IP: {0}'.format(myIp), (255, 255, 255))
                
                rectHeight = 25
                rectWidth = 300
                
                pygame.draw.rect(gameDisplay, (0,0,255),     (50,70+ 0*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (100,100,255), (50,70+ 1*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (0,0,255),     (50,70+ 2*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (100,100,255), (50,70+ 3*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (0,0,255),     (50,70+ 4*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (100,100,255), (50,70+ 5*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (0,0,255),     (50,70+ 6*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (100,100,255), (50,70+ 7*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (0,0,255),     (50,70+ 8*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (100,100,255), (50,70+ 9*rectHeight,rectWidth, rectHeight), 0)
                
                pygame.draw.rect(gameDisplay, (255,0,0),     (50,70+ 10*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (255,100,100), (50,70+ 11*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (255,0,0),     (50,70+ 12*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (255,100,100), (50,70+ 13*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (255,0,0),     (50,70+ 14*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (255,100,100), (50,70+ 15*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (255,0,0),     (50,70+ 16*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (255,100,100), (50,70+ 17*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (255,0,0),     (50,70+ 18*rectHeight,rectWidth, rectHeight), 0)
                pygame.draw.rect(gameDisplay, (255,100,100), (50,70+ 19*rectHeight,rectWidth, rectHeight), 0)
                
                anyText(55, 72, nome, (255, 255, 255))
                anyText(55, 72+ 10*rectHeight, "Luscas", (255, 255, 255))
                anyText(55, 72+ 4*rectHeight, "Freddy", (255, 255, 255))
                
                #condições para o botão START        
                if select11 == False and 650 > mouse_pos[0] > 510 and 500 > mouse_pos[1] > 450:
                    anyText40(510, 450, "START", (255,255,0))	
                    if click1:
                        startonline = True
                        click1 = False
                        client.StartGame()

                elif select11 == False:
                    anyText40(510, 450, "START", (255,255,255))	
                
                #condições para o botão QUIT     
                if select11 == False and 730 > mouse_pos[0] > 400 and 570 > mouse_pos[1] > 520:
                    anyText40(400, 520, "QUIT TO MENU", (255,255,0))	
                    if click1:
                        click1 = False
                        break
                        
                elif select11 == False:
                    anyText40(400, 520, "QUIT TO MENU", (255,255,255))            
            
                if LetsPlay:
                    break
        
        click1 = False
        pygame.display.update()
        
##################################################################################
    ThreadWaitSendOnce = False
    ThreadWaitSendDone = False
    ThreadOnce2 = False
    ThreadOnce = False
    team = 'none'
    client.setTeam(team)
    ThreadDone = False
    ThreadDone2 = False
    WaitStartTheGame = False
    StartGame = False
    ThreadStartedOnce = False
    #loop JOIN
    while select11:    
                    
        gameDisplay.fill((121, 202, 249))
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                client.Close()
                server.Close()
            if event.type == pygame.MOUSEBUTTONUP:
                click1 = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: pygame.quit()

        # if not ThreadWaitSendOnce:
        #     def WaitSend():
        #         global ThreadWaitSendDone
        #         client.waitToSend()
        #         ThreadWaitSendDone = True

        #     ThreadWait = Thread(target=WaitSend)
        #     ThreadWait.start()
        #     ThreadWaitSendOnce = True

        row1 = (270 > mouse_pos[1] > 200)
        row2 = (370 > mouse_pos[1] > 300)
        row3 = (470 > mouse_pos[1] > 400)
        row4 = (570 > mouse_pos[1] > 500)
        r1 = 200
        r2 = 300
        r3 = 400
        r4 = 500
        
        column1 = (180 > mouse_pos[0] > 135)
        column2 = (300 > mouse_pos[0] > 255)
        column3 = (300 + 120 > mouse_pos[0] > 255 + 120)
        column4 = (300 + 120 + 120 > mouse_pos[0] > 255 + 120 + 120)
        column5 = (300 + 120 + 120 + 120 > mouse_pos[0] > 255 + 120 + 120 + 120)
        col1 = 135
        col2 = 255
        col3 = 255 + 120
        col4 = 255 + 120 + 120
        col5 = 255 + 120 + 120 + 120
                
        cloud2(cl_x3, -100 + camera(x) + Tela - 2000)
        cloud1(cl_x4, 0 + camera(x) + Tela - 2000)
        cloud2(cl_x5, -150 + camera(x) + Tela - 1600)
        cloud1(cl_x6, 50 + camera(x) + Tela - 1600)
        
        cl_x1 += 0.3    
        cl_x2 += 0.3
        cl_x3 += 0.3
        cl_x4 += 0.3
        cl_x5 += 0.3
        cl_x6 += 0.3
        cl_x7 += 0.3
        cl_x8 += 0.3
        cl_x9 += 0.3
        cl_x10 += 0.3
        cl_x11 += 0.3
        cl_x12 += 0.3
        
        if cl_x1 > 805:
            cl_x1 = -400
        if cl_x2 > 805:
            cl_x2 = -400
        if cl_x3 > 805:
            cl_x3 = -400
        if cl_x4 > 805:
            cl_x4 = -400
        if cl_x5 > 805:
            cl_x5 = -400
        if cl_x6 > 805:
            cl_x6 = -400
        if cl_x7 > 805:
            cl_x7 = -400
        if cl_x8 > 805:
            cl_x8 = -400
        if cl_x9 > 805:
            cl_x9 = -400
        if cl_x10 > 805:
            cl_x10 = -400
        if cl_x11 > 805:
            cl_x11 = -400
        if cl_x12 > 805:
            cl_x12 = -400
            
            
        if selectTeam == False and 290 > mouse_pos[0] > 200 and 315 > mouse_pos[1] > 275:
            anyText40(200, 275, "RED", (255,0,0))
            if click1:
                selectTeam = True
                team = 'red'
                click1 = False
                
        elif selectTeam == False:
            anyText40(200, 275, "RED", (255,255,255))	
        
        if selectTeam == False and 700 > mouse_pos[0] > 580 and 315 > mouse_pos[1] > 275:
            anyText40(580, 275, "BLUE", (0,0,255))	
            if click1:
                selectTeam = True
                team = 'blue'
                click1 = False

        elif selectTeam == False:
            anyText40(580, 275, "BLUE", (255,255,255))
        
        if selectTeam == False and 530 > mouse_pos[0] > 350 and 415 > mouse_pos[1] > 375:
            anyText40(350, 375, "RANDOM", (255,255,0))
            if click1:
                selectTeam = True
                team = 'random'
                
                click1 = False
                
        elif selectTeam == False:
            anyText40(350, 375, "RANDOM", (255,255,255))

        if team != 'none':
            client.setTeam(team)
            
        if not selectChar1:
            
                if row1 and column1:
                    gameDisplay.blit(marrom[2], (col1,r1))	
                    if click1:
                        escolha1 = marrom
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(marrom[0], (col1,r1)) 
                    
                if row1 and column2:
                    gameDisplay.blit(rosa[2], (col2,r1))	
                    if click1:
                        escolha1 = rosa
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(rosa[0], (col2,r1)) 
                    
                if row1 and column3:
                    gameDisplay.blit(amarelo[2], (col3,r1))	
                    if click1:
                        escolha1 = amarelo
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(amarelo[0], (col3,r1)) 
                    
                if row1 and column4:
                    gameDisplay.blit(jerry[2], (col4,r1))	
                    if click1:
                        escolha1 = jerry
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(jerry[0], (col4,r1)) 
                    
                if row1 and column5:
                    gameDisplay.blit(obama[2], (col5,r1))	
                    if click1:
                        escolha1 = obama
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(obama[0], (col5,r1)) 
                    
                if row2 and column1:
                    gameDisplay.blit(fred[2], (col1,r2))	
                    if click1:
                        escolha1 = fred
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(fred[0], (col1,r2)) 
                    
                if row2 and column2:
                    gameDisplay.blit(luscas[2], (col2,r2))	
                    if click1:
                        escolha1 = luscas
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(luscas[0], (col2,r2))
                    
                if row2 and column3:
                    gameDisplay.blit(gui[2], (col3,r2))	
                    if click1:
                        escolha1 = gui
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(gui[0], (col3,r2)) 
                    
                if row2 and column4:
                    gameDisplay.blit(ayres[2], (col4,r2))	
                    if click1:
                        escolha1 = ayres
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(ayres[0], (col4,r2)) 
                    
                if row2 and column5:
                    gameDisplay.blit(hage[2], (col5,r2))	
                    if click1:
                        escolha1 = hage
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(hage[0], (col5,r2)) 
                    
                if row3 and column1:
                    gameDisplay.blit(superman[2], (col1,r3))	
                    if click1:
                        escolha1 = superman
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(superman[0], (col1,r3)) 
                    
                if row3 and column2:
                    gameDisplay.blit(batman[2], (col2,r3))	
                    if click1:
                        escolha1 = batman
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(batman[0], (col2,r3))
                    
                if row3 and column3:
                    gameDisplay.blit(link[2], (col3,r3))	
                    if click1:
                        escolha1 = link
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(link[0], (col3,r3))
                    
                if row3 and column4:
                    gameDisplay.blit(goku[2], (col4,r3))	
                    if click1:
                        escolha1 = goku
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(goku[0], (col4,r3))
                    
                if row3 and column5:
                    gameDisplay.blit(ash[2], (col5,r3))	
                    if click1:
                        escolha1 = ash
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(ash[0], (col5,r3))
                    
                if row4 and column1:
                    gameDisplay.blit(dilma[2], (col1,r4))	
                    if click1:
                        escolha1 = dilma
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(dilma[0], (col1,r4)) 
                    
                if row4 and column2:
                    gameDisplay.blit(terminator[2], (col2,r4))	
                    if click1:
                        escolha1 = terminator
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(terminator[0], (col2,r4))
                    
                if row4 and column3:
                    gameDisplay.blit(sakura[2], (col3,r4))	
                    if click1:
                        escolha1 = sakura
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(sakura[0], (col3,r4))
                    
                if row4 and column4:
                    gameDisplay.blit(leprichon[2], (col4,r4))	
                    if click1:
                        escolha1 = leprichon
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(leprichon[0], (col4,r4))
                    
                if row4 and column5:
                    gameDisplay.blit(ash[2], (col5,r4))	
                    if click1:
                        escolha1 = ash
                        click1 = False
                        selectChar1 = True
                        
                else:
                    gameDisplay.blit(ash[0], (col5,r4)) 
                
        if selectTeam and selectChar1: 

            if not ThreadOnce2:# and ThreadWaitSendDone: 
                def Send():
                    global WaitStartTheGame
                    client.SendInfos() 
                    WaitStartTheGame = True

                nameThread = Thread(target=Send)      
                nameThread.start() 
                ThreadOnce2 = True

            anyText40(260, 10, "JOIN GAME", (255, 255, 255))
            anyText40(420, 100, "IP: {0}".format(ip), (255, 255, 255))
            
            rectHeight = 25
            rectWidth = 300
            
            pygame.draw.rect(gameDisplay, (0,0,255),     (50,70+ 0*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (100,100,255), (50,70+ 1*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (0,0,255),     (50,70+ 2*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (100,100,255), (50,70+ 3*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (0,0,255),     (50,70+ 4*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (100,100,255), (50,70+ 5*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (0,0,255),     (50,70+ 6*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (100,100,255), (50,70+ 7*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (0,0,255),     (50,70+ 8*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (100,100,255), (50,70+ 9*rectHeight,rectWidth, rectHeight), 0)
            
            pygame.draw.rect(gameDisplay, (255,0,0),     (50,70+ 10*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (255,100,100), (50,70+ 11*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (255,0,0),     (50,70+ 12*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (255,100,100), (50,70+ 13*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (255,0,0),     (50,70+ 14*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (255,100,100), (50,70+ 15*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (255,0,0),     (50,70+ 16*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (255,100,100), (50,70+ 17*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (255,0,0),     (50,70+ 18*rectHeight,rectWidth, rectHeight), 0)
            pygame.draw.rect(gameDisplay, (255,100,100), (50,70+ 19*rectHeight,rectWidth, rectHeight), 0)
            
            anyText(55, 72 + 0*rectHeight, nome, (255, 255, 255))
            anyText(55, 72+ 10*rectHeight, "Luscas", (255, 255, 255))
            anyText(55, 72+ 4*rectHeight, "Freddy", (255, 255, 255))
            
            
            #condições para o botão start        
            if not client.waitStart():        
                startonline = True
                break           
        
       # click1 = False
    
        pygame.display.update()        
    
    ######################################################################################################
    
    contadorFrames = 0
    w = -7
    back = False
    
    #condição p/ parar o jogo
    crashed = False
    
    valorPress = 0
    
    bg_color = ((121, 202, 249))
    
    selectChar1 = False
    selectChar2 = False
    
    #online game loop
    while startonline:
        click = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                client.Close()
                server.Close()
            if ev.type == pygame.MOUSEBUTTONUP:
                click1 = True
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE: pygame.quit()
            
            if team == 'red':
            #computar pontos 
                if ev.type == pygame.KEYDOWN and back == False:
                    if ev.key == pygame.K_f and px < 400 and px > 0:
                        px += valorPress 
                    if ev.key == pygame.K_j and px > 0 and px < 400:
                        px += valorPress
                        
            if team == 'blue':
            #computar pontos    
                if ev.type == pygame.KEYDOWN and back == False:
                    if ev.key == pygame.K_f and px < 400 and px > 0:
                        px -= valorPress 
                    if ev.key == pygame.K_j and px > 0 and px < 400:
                        px -= valorPress
    
                
        gameDisplay.fill(bg_color)
        
        if contadorFrames > 600:
            bgINSANE(0, 0 + camera(x) + Tela)
        elif contadorFrames > 400:
            bgHIGH(0, 0 + camera(x) + Tela)
        else:
            bgLOW(0, 0 + camera(x) + Tela)
        
        mountain_bg(-30, 400 + camera(x) + Tela)
        
    
        cloud2(cl_x3, -100 + camera(x) + Tela - 2000)
        cloud1(cl_x4, 0 + camera(x) + Tela - 2000)
        cloud2(cl_x5, -150 + camera(x) + Tela - 1600)
        cloud1(cl_x6, 50 + camera(x) + Tela - 1600)
        cloud2(cl_x7, -250 + camera(x) + Tela - 1200)
        cloud1(cl_x8, 0 + camera(x) + Tela - 1200)
        cloud2(cl_x9, -150 + camera(x) + Tela - 800)
        cloud1(cl_x10, 50 + camera(x) + Tela - 800)
        cloud2(cl_x11, -50 + camera(x) + Tela - 400)
        cloud1(cl_x12, 100 + camera(x) + Tela - 400)
        cloud2(cl_x1, -50 + camera(x) + Tela)
        cloud1(cl_x2, 0 + camera(x) + Tela)
        
        cl_x1 += 0.3    
        cl_x2 += 0.3
        cl_x3 += 0.3    
        cl_x4 += 0.3
        cl_x5 += 0.3
        cl_x6 += 0.3
        cl_x7 += 0.3
        cl_x8 += 0.3
        cl_x9 += 0.3
        cl_x10 += 0.3
        cl_x11 += 0.3
        cl_x12 += 0.3
        
        if cl_x1 > 805:
            cl_x1 = -400
        if cl_x2 > 805:
            cl_x2 = -400
        if cl_x3 > 805:
            cl_x3 = -400
        if cl_x4 > 805:
            cl_x4 = -400
        if cl_x5 > 805:
            cl_x5 = -400
        if cl_x6 > 805:
            cl_x6 = -400
        if cl_x7 > 805:
            cl_x7 = -400
        if cl_x8 > 805:
            cl_x8 = -400
        if cl_x9 > 805:
            cl_x9 = -400
        if cl_x10 > 805:
            cl_x10 = -400
        if cl_x11 > 805:
            cl_x11 = -400
        if cl_x12 > 805:
            cl_x12 = -400   
        
        taxa = 1.5    
        
        floatMountain(80, 285 + camera(x) *taxa + 1000 + Tela)        
        floatMountain1(520, 285 + camera(x) *taxa + 1000 + Tela)  
        
        redflag_pos = (200, 240 + camera(x) *taxa + 1000 + Tela)
        blueflag_pos = (440, 240 + camera(x) *taxa + 1000 + Tela)
        
        if contadorFrames%56 > 7*7:
            flagR7(redflag_pos)
            flagB4(blueflag_pos)
        elif contadorFrames%56 > 6*7:
            flagR6(redflag_pos)
            flagB3(blueflag_pos)
        elif contadorFrames%56 > 5*7:
            flagR5(redflag_pos)
            flagB2(blueflag_pos)
        elif contadorFrames%56 > 4*7:
            flagR4(redflag_pos)
            flagB1(blueflag_pos)
        elif contadorFrames%56 > 3*7:
            flagR3(redflag_pos)
            flagB0(blueflag_pos)
        elif contadorFrames%56 > 2*7:
            flagR2(redflag_pos)
            flagB7(blueflag_pos)
        elif contadorFrames%56 > 1*7:
            flagR1(redflag_pos)
            flagB6(blueflag_pos)
        else:
            flagR0(redflag_pos)
            flagB5(blueflag_pos)
        
        QZ_bg(40,155 + camera(x) *taxa + 1000 + Tela)
        PM_bg(620,155 + camera(x) *taxa + 1000 + Tela)
        
        x += 0.1
    
        anyText(200, 550 + camera(x) *taxa + 1000 + Tela, ("WINS: {0}".format(contadorRed)), (255,0,0))
        anyText(510, 550 + camera(x) *taxa + 1000 + Tela, ("WINS: {0}".format(contadorBlue)), (0,0,255))    
        
        
        # if px > 100:
        #     if pygame.key.get_pressed()[pygame.K_f] and px < 400 and team == 'red' or pygame.key.get_pressed()[pygame.K_j] and px < 400 and team == 'red':
        #         p_fred2(185,206 + 25 + camera(x) *taxa + 1000 + Tela)
        #     else:
        #         p_fred1(185,206 + 25 + camera(x) *taxa + 1000 + Tela)
        # else:
        #     if pygame.key.get_pressed()[pygame.K_f] and px < 400 and team == 'red' or pygame.key.get_pressed()[pygame.K_j] and px < 400 and team == 'red':
        #         p_fred2d(185,206 + 25 + camera(x) *taxa + 1000 + Tela)
        #     else:
        #         p_fred1d(185,206 + 25 + camera(x) *taxa + 1000 + Tela)
            
        # if px < 300: 
        #     if pygame.key.get_pressed()[pygame.K_f] and px < 400 and team == 'blue' or pygame.key.get_pressed()[pygame.K_j] and px < 400 and team == 'blue':
        #         p_gui20(567, 206 + 25 + camera(x) *taxa + 1000 + Tela)
        #     else:
        #         p_gui10(567, 206 + 25 + camera(x) *taxa + 1000 + Tela)
        # else: 
        #     if pygame.key.get_pressed()[pygame.K_f] and px < 400 and team == 'blue' or pygame.key.get_pressed()[pygame.K_j] and px < 400 and team == 'blue':
        #         p_gui20d(567, 206 + 25 + camera(x) *taxa + 1000 + Tela)
        #     else:
        #         p_gui10d(567, 206 + 25 + camera(x) *taxa + 1000 + Tela)
        
        
        
        
        if pygame.key.get_pressed()[pygame.K_q] and px < 400 or pygame.key.get_pressed()[pygame.K_z] and px < 400:
            corda_i(198, 245 + 25 + camera(x) *taxa + 1000 + Tela)
        elif pygame.key.get_pressed()[pygame.K_p] and px < 400 or pygame.key.get_pressed()[pygame.K_m] and px < 400:
            corda_i(202, 245 + 25 + camera(x) *taxa + 1000 + Tela)
        else:
            corda_i(200, 245 + 25 + camera(x) *taxa + 1000 + Tela)
    
        
        pygame.draw.rect(gameDisplay, (0,0,255), (0,580 + camera(x) *taxa + 1000 + Tela,800,50), 0)
        pygame.draw.rect(gameDisplay, (255,0,0), (0,580 + camera(x) *taxa +1000 + Tela,px*2,50), 0)
        
                
        
        button_pressed = False
        
        if contadorFrames > 600:
            ilevel = "INSANE"
            intensityLevel = 2
            bg_color = (150, 50, 50)
            valorPress = 20
        elif contadorFrames > 400:
            ilevel = "HIGH"
            intensityLevel = 1
            bg_color = (80, 80, 130)
            valorPress = 10
        elif 210 < contadorFrames:
            ilevel = "LOW"
            intensityLevel = 0
            bg_color = (121, 202, 249)
            valorPress = 5
        else:
            ilevel = "NONE"
        
        intensity(100, 100 + camera(x) *taxa + 1000 + Tela, "INTENSITY LEVEL: {0}".format(ilevel), intensityLevel)
        
        if px < 1:
                    
            px = 0
            s = pygame.Surface((800,600))  # the size of your rect
            s.set_alpha(200)                # alpha level
            s.fill((255,255,255))           # this fills the entire surface
            
            if w > 3:
                j = 0.0
    
            gameDisplay.blit(s, (0,600 + camera_win(w)))
            
            win(-70, 600 + camera_win(w), "BLUE WINS!", (0,0,200))
                
            if 465 > mouse_pos[0] > 335 and (575 + 600 + camera_win(w)) > mouse_pos[1] > (525 + 600 + camera_win(w)):
                gameDisplay.blit(start1,(335, 525 + 600 + camera_win(w)))	
                if click[0] == 1:
                    #px = 200
                    contadorFrames = 0
                    j = -0.15
                    back = True		
            else:
                gameDisplay.blit(start0,(335, 525 + 600 + camera_win(w)))
         
            w += j
            
        s = pygame.Surface((800,600))  # the size of your rect
        s.set_alpha(200)                # alpha level
        s.fill((255,255,255))
            
            
        if px > 399:
                 
            px = 400
            if w > 3:
                j = -0.0
            
                
            gameDisplay.blit(s, (0,600 + camera_win(w)))
            win(-30, 600 + camera_win(w), "RED WINS!", (200,0,0))
            
            if 465 > mouse_pos[0] > 335 and (575 + 600 + camera_win(w)) > mouse_pos[1] > (525 + 600 + camera_win(w)):
                gameDisplay.blit(start1,(335, 525 + 600 + camera_win(w)))	
                if click[0] == 1:
                    #px = 200
                    contadorFrames = 0
                    j = -0.15
                    back = True
            else:
                gameDisplay.blit(start0,(335, 525 + 600 + camera_win(w)))        
            
            w += j
    
        if contadorFrames > 90 and contadorFrames < 130:
            N3(400 - 200*0.5, 300 - 300*0.5)
        if contadorFrames > 130 and contadorFrames < 170:
            N2(400 - 200*0.5, 300 - 300*0.5)
        if contadorFrames > 170 and contadorFrames < 210:
            N1(400 - 200*0.5, 300 - 300*0.5)
            
        if back and w < -7 and px < 200:
            px += 5
            j = 0.15
            if px > 199:
                back = False
                contadorBlue += 1
                valorPress = 0
                
        if back and w < -7 and px > 200:
            px -= 5
            j = 0.15
            if px < 201:
                back = False
                contadorRed += 1
                valorPress = 0
        
        contadorFrames += 1
        click1 = False
        pygame.display.update()
        
    ########################################################################## 

        #offline game loop
    while start:
        click = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                client.Close()
                server.Close()
            if ev.type == pygame.MOUSEBUTTONUP:
                click1 = True
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE: pygame.quit()
            
            #computar pontos 
            if ev.type == pygame.KEYDOWN and back == False:
                if ev.key == pygame.K_q and px < 400 and px > 0:
                    px += valorPress 
                if ev.key == pygame.K_p and px > 0 and px < 400:
                    px -= valorPress
                if ev.key == pygame.K_z and px < 400 and px > 0:
                    px += valorPress
                if ev.key == pygame.K_m and px > 0 and px < 400:
                    px -= valorPress

        
        row1 = (270 > mouse_pos[1] > 200)
        row2 = (370 > mouse_pos[1] > 300)
        row3 = (470 > mouse_pos[1] > 400)
        row4 = (570 > mouse_pos[1] > 500)
        r1 = 200
        r2 = 300
        r3 = 400
        r4 = 500
        
        column1 = (180 > mouse_pos[0] > 135)
        column2 = (300 > mouse_pos[0] > 255)
        column3 = (300 + 120 > mouse_pos[0] > 255 + 120)
        column4 = (300 + 120 + 120 > mouse_pos[0] > 255 + 120 + 120)
        column5 = (300 + 120 + 120 + 120 > mouse_pos[0] > 255 + 120 + 120 + 120)
        col1 = 135
        col2 = 255
        col3 = 255 + 120
        col4 = 255 + 120 + 120
        col5 = 255 + 120 + 120 + 120
        
        

                
        gameDisplay.fill(bg_color)
        
        if contadorFrames > 600:
            bgINSANE(0, 0 + camera(x) + Tela)
            sunR(0, 220 + camera(x) + Tela)
            mountain_bg(-30, 400 + camera(x) + Tela)
            cloud22(cl_x3, -100 + camera(x) + Tela - 2000)
            cloud12(cl_x4, 0 + camera(x) + Tela - 2000)
            cloud22(cl_x5, -150 + camera(x) + Tela - 1600)
            cloud12(cl_x6, 50 + camera(x) + Tela - 1600)
            cloud22(cl_x7, -250 + camera(x) + Tela - 1200)
            cloud12(cl_x8, 0 + camera(x) + Tela - 1200)
            cloud22(cl_x9, -150 + camera(x) + Tela - 800)
            cloud12(cl_x10, 50 + camera(x) + Tela - 800)
            cloud22(cl_x11, -50 + camera(x) + Tela - 400)
            cloud12(cl_x12, 100 + camera(x) + Tela - 400)
            cloud22(cl_x1, -50 + camera(x) + Tela)
            cloud12(cl_x2, 0 + camera(x) + Tela)
        elif contadorFrames > 400:
            bgHIGH(0, 0 + camera(x) + Tela)
            sun(0, 220 + camera(x) + Tela)
            mountain_bg(-30, 400 + camera(x) + Tela)
            cloud21(cl_x3, -100 + camera(x) + Tela - 2000)
            cloud11(cl_x4, 0 + camera(x) + Tela - 2000)
            cloud21(cl_x5, -150 + camera(x) + Tela - 1600)
            cloud11(cl_x6, 50 + camera(x) + Tela - 1600)
            cloud21(cl_x7, -250 + camera(x) + Tela - 1200)
            cloud11(cl_x8, 0 + camera(x) + Tela - 1200)
            cloud21(cl_x9, -150 + camera(x) + Tela - 800)
            cloud11(cl_x10, 50 + camera(x) + Tela - 800)
            cloud21(cl_x11, -50 + camera(x) + Tela - 400)
            cloud11(cl_x12, 100 + camera(x) + Tela - 400)
            cloud21(cl_x1, -50 + camera(x) + Tela)
            cloud11(cl_x2, 0 + camera(x) + Tela)
        else:
            bgLOW(0, 0 + camera(x) + Tela)
            sun(0, 220 + camera(x) + Tela)
            mountain_bg(-30, 400 + camera(x) + Tela)
            cloud2(cl_x3, -100 + camera(x) + Tela - 2000)
            cloud1(cl_x4, 0 + camera(x) + Tela - 2000)
            cloud2(cl_x5, -150 + camera(x) + Tela - 1600)
            cloud1(cl_x6, 50 + camera(x) + Tela - 1600)
            cloud2(cl_x7, -250 + camera(x) + Tela - 1200)
            cloud1(cl_x8, 0 + camera(x) + Tela - 1200)
            cloud2(cl_x9, -150 + camera(x) + Tela - 800)
            cloud1(cl_x10, 50 + camera(x) + Tela - 800)
            cloud2(cl_x11, -50 + camera(x) + Tela - 400)
            cloud1(cl_x12, 100 + camera(x) + Tela - 400)
            cloud2(cl_x1, -50 + camera(x) + Tela)
            cloud1(cl_x2, 0 + camera(x) + Tela)
        
        cl_x1 += 0.3    
        cl_x2 += 0.3
        cl_x3 += 0.3    
        cl_x4 += 0.3
        cl_x5 += 0.3
        cl_x6 += 0.3
        cl_x7 += 0.3
        cl_x8 += 0.3
        cl_x9 += 0.3
        cl_x10 += 0.3
        cl_x11 += 0.3
        cl_x12 += 0.3
        
        if cl_x1 > 805:
            cl_x1 = -400
        if cl_x2 > 805:
            cl_x2 = -400
        if cl_x3 > 805:
            cl_x3 = -400
        if cl_x4 > 805:
            cl_x4 = -400
        if cl_x5 > 805:
            cl_x5 = -400
        if cl_x6 > 805:
            cl_x6 = -400
        if cl_x7 > 805:
            cl_x7 = -400
        if cl_x8 > 805:
            cl_x8 = -400
        if cl_x9 > 805:
            cl_x9 = -400
        if cl_x10 > 805:
            cl_x10 = -400
        if cl_x11 > 805:
            cl_x11 = -400
        if cl_x12 > 805:
            cl_x12 = -400   
            
        
        
        if not selectChar1:
            
            anyText40(250, 70, "RED SELECT", (255,0,0))
            
            if row1 and column1:
                gameDisplay.blit(marrom[2], (col1,r1))	
                if click1:
                    escolha1 = marrom
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(marrom[0], (col1,r1)) 
                
            if row1 and column2:
                gameDisplay.blit(rosa[2], (col2,r1))	
                if click1:
                    escolha1 = rosa
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(rosa[0], (col2,r1)) 
                
            if row1 and column3:
                gameDisplay.blit(amarelo[2], (col3,r1))	
                if click1:
                    escolha1 = amarelo
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(amarelo[0], (col3,r1)) 
                
            if row1 and column4:
                gameDisplay.blit(jerry[2], (col4,r1))	
                if click1:
                    escolha1 = jerry
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(jerry[0], (col4,r1)) 
                
            if row1 and column5:
                gameDisplay.blit(obama[2], (col5,r1))	
                if click1:
                    escolha1 = obama
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(obama[0], (col5,r1)) 
                
            if row2 and column1:
                gameDisplay.blit(fred[2], (col1,r2))	
                if click1:
                    escolha1 = fred
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(fred[0], (col1,r2)) 
                
            if row2 and column2:
                gameDisplay.blit(luscas[2], (col2,r2))	
                if click1:
                    escolha1 = luscas
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(luscas[0], (col2,r2))
                
            if row2 and column3:
                gameDisplay.blit(gui[2], (col3,r2))	
                if click1:
                    escolha1 = gui
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(gui[0], (col3,r2)) 
                
            if row2 and column4:
                gameDisplay.blit(ayres[2], (col4,r2))	
                if click1:
                    escolha1 = ayres
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(ayres[0], (col4,r2)) 
                
            if row2 and column5:
                gameDisplay.blit(hage[2], (col5,r2))	
                if click1:
                    escolha1 = hage
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(hage[0], (col5,r2)) 
                
            if row3 and column1:
                gameDisplay.blit(superman[2], (col1,r3))	
                if click1:
                    escolha1 = superman
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(superman[0], (col1,r3)) 
                
            if row3 and column2:
                gameDisplay.blit(batman[2], (col2,r3))	
                if click1:
                    escolha1 = batman
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(batman[0], (col2,r3))
                
            if row3 and column3:
                gameDisplay.blit(link[2], (col3,r3))	
                if click1:
                    escolha1 = link
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(link[0], (col3,r3))
                
            if row3 and column4:
                gameDisplay.blit(goku[2], (col4,r3))	
                if click1:
                    escolha1 = goku
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(goku[0], (col4,r3))
                
            if row3 and column5:
                gameDisplay.blit(ash[2], (col5,r3))	
                if click1:
                    escolha1 = ash
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(ash[0], (col5,r3))
                
            if row4 and column1:
                gameDisplay.blit(dilma[2], (col1,r4))	
                if click1:
                    escolha1 = dilma
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(dilma[0], (col1,r4)) 
                
            if row4 and column2:
                gameDisplay.blit(terminator[2], (col2,r4))	
                if click1:
                    escolha1 = terminator
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(terminator[0], (col2,r4))
                
            if row4 and column3:
                gameDisplay.blit(sakura[2], (col3,r4))	
                if click1:
                    escolha1 = sakura
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(sakura[0], (col3,r4))
                
            if row4 and column4:
                gameDisplay.blit(leprichon[2], (col4,r4))	
                if click1:
                    escolha1 = leprichon
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(leprichon[0], (col4,r4))
                
            if row4 and column5:
                gameDisplay.blit(ash[2], (col5,r4))	
                if click1:
                    escolha1 = ash
                    click1 = False
                    selectChar1 = True
                    
            else:
                gameDisplay.blit(ash[0], (col5,r4))
                
        if not selectChar2 and selectChar1:
            
            anyText40(230, 70, "BLUE SELECT", (0,0, 255))
            
            if row1 and column1:
                gameDisplay.blit(marrom[6], (col1,r1))	
                if click1:
                    escolha2 = marrom
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(marrom[4], (col1,r1)) 
                
            if row1 and column2:
                gameDisplay.blit(rosa[6], (col2,r1))	
                if click1:
                    escolha2 = rosa
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(rosa[4], (col2,r1)) 
                
            if row1 and column3:
                gameDisplay.blit(amarelo[6], (col3,r1))	
                if click1:
                    escolha2 = amarelo
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(amarelo[4], (col3,r1)) 
                
            if row1 and column4:
                gameDisplay.blit(jerry[6], (col4,r1))	
                if click1:
                    escolha2 = jerry
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(jerry[4], (col4,r1)) 
                
            if row1 and column5:
                gameDisplay.blit(obama[6], (col5,r1))	
                if click1:
                    escolha2 = obama
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(obama[4], (col5,r1)) 
                
            if row2 and column1:
                gameDisplay.blit(fred[6], (col1,r2))	
                if click1:
                    escolha2 = fred
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(fred[4], (col1,r2)) 
                
            if row2 and column2:
                gameDisplay.blit(luscas[6], (col2,r2))	
                if click1:
                    escolha2 = luscas
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(luscas[4], (col2,r2))
                
            if row2 and column3:
                gameDisplay.blit(gui[6], (col3,r2))	
                if click1:
                    escolha2 = gui
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(gui[4], (col3,r2)) 
                
            if row2 and column4:
                gameDisplay.blit(ayres[6], (col4,r2))	
                if click1:
                    escolha2 = ayres
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(ayres[4], (col4,r2)) 
                
            if row2 and column5:
                gameDisplay.blit(hage[6], (col5,r2))	
                if click1:
                    escolha2 = hage
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(hage[4], (col5,r2)) 
                
            if row3 and column1:
                gameDisplay.blit(superman[6], (col1,r3))	
                if click1:
                    escolha2 = superman
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(superman[4], (col1,r3)) 
        
            if row3 and column2:
                gameDisplay.blit(batman[6], (col2,r3))	
                if click1:
                    escolha2 = batman
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(batman[4], (col2,r3))
                
            if row3 and column3:
                gameDisplay.blit(link[6], (col3,r3))	
                if click1:
                    escolha2 = link
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(link[4], (col3,r3))
                
            if row3 and column4:
                gameDisplay.blit(goku[6], (col4,r3))	
                if click1:
                    escolha2 = goku
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(goku[4], (col4,r3))
                
            if row3 and column5:
                gameDisplay.blit(ash[6], (col5,r3))	
                if click1:
                    escolha2 = ash
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(ash[4], (col5,r3))
                
            if row4 and column1:
                gameDisplay.blit(dilma[6], (col1,r4))	
                if click1:
                    escolha2 = dilma
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(dilma[4], (col1,r4)) 
                
            if row4 and column2:
                gameDisplay.blit(terminator[6], (col2,r4))	
                if click1:
                    escolha2 = terminator
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(terminator[4], (col2,r4))
        
            if row4 and column3:
                gameDisplay.blit(sakura[6], (col3,r4))	
                if click1:
                    escolha2 = sakura
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(sakura[4], (col3,r4))
                
            if row4 and column4:
                gameDisplay.blit(leprichon[6], (col4,r4))	
                if click1:
                    escolha2 = leprichon
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(leprichon[4], (col4,r4))
                
            if row4 and column5:
                gameDisplay.blit(ash[6], (col5,r4))	
                if click1:
                    escolha2 = ash
                    click1 = False
                    selectChar2 = True
                    
            else:
                gameDisplay.blit(ash[4], (col5,r4))
                    
            
            
        
        if selectChar1 and selectChar2:
            taxa = 1.5    
            
            TitleSize = int((15*(1+math.sin(2*3.14*n*0.01)))*0.5)
            n -= 1
            
            floatMountain(80, 285 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2)        
            floatMountain1(520, 285 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2)  
            
            redflag_pos = (200, 240 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2)
            blueflag_pos = (440, 240 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2)
            
            if contadorFrames%56 > 7*7:
                flagR7(redflag_pos)
                flagB4(blueflag_pos)
            elif contadorFrames%56 > 6*7:
                flagR6(redflag_pos)
                flagB3(blueflag_pos)
            elif contadorFrames%56 > 5*7:
                flagR5(redflag_pos)
                flagB2(blueflag_pos)
            elif contadorFrames%56 > 4*7:
                flagR4(redflag_pos)
                flagB1(blueflag_pos)
            elif contadorFrames%56 > 3*7:
                flagR3(redflag_pos)
                flagB0(blueflag_pos)
            elif contadorFrames%56 > 2*7:
                flagR2(redflag_pos)
                flagB7(blueflag_pos)
            elif contadorFrames%56 > 1*7:
                flagR1(redflag_pos)
                flagB6(blueflag_pos)
            else:
                flagR0(redflag_pos)
                flagB5(blueflag_pos)
            
            QZ_bg(40,155 + camera(x) *taxa + 1000 + Tela  +  (15*(1+math.sin(2*3.14*(n+10)*0.01)))*0.25)
            PM_bg(620,155 + camera(x) *taxa + 1000 + Tela  +  (15*(1+math.sin(2*3.14*(n+10)*0.01)))*0.25)
            
            x += 0.1
        
            anyText(200, 550 + camera(x) *taxa + 1000 + Tela, ("WINS: {0}".format(contadorRed)), (255,0,0))
            anyText(510, 550 + camera(x) *taxa + 1000 + Tela, ("WINS: {0}".format(contadorBlue)), (0,0,255))    
            
            if px > 100:
                if pygame.key.get_pressed()[pygame.K_q] and px < 400 or pygame.key.get_pressed()[pygame.K_z] and px < 400:
                    gameDisplay.blit(escolha1[1], (185,206 + 25 + camera(x) *1.5 + 1000 + Tela  +  TitleSize/2))
                else:
                    gameDisplay.blit(escolha1[0], (185,206 + 25 + camera(x) *1.5 + 1000 + Tela  +  TitleSize/2))
            else:
                if pygame.key.get_pressed()[pygame.K_q] and px < 400 or pygame.key.get_pressed()[pygame.K_z] and px < 400:
                    gameDisplay.blit(escolha1[3], (185,206 + 25 + camera(x) *1.5 + 1000 + Tela  +  TitleSize/2))
                else:
                    gameDisplay.blit(escolha1[2], (185,206 + 25 + camera(x) *1.5 + 1000 + Tela  +  TitleSize/2))
                
            if px < 300: 
                if pygame.key.get_pressed()[pygame.K_p] and px < 400 or pygame.key.get_pressed()[pygame.K_m] and px < 400:
                    gameDisplay.blit(escolha2[5], (567, 206 + 25 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2))
                else:
                    gameDisplay.blit(escolha2[4], (567, 206 + 25 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2))
            else: 
                if pygame.key.get_pressed()[pygame.K_p] and px < 400 or pygame.key.get_pressed()[pygame.K_m] and px < 400:
                    gameDisplay.blit(escolha2[7], (567, 206 + 25 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2))
                else:
                    gameDisplay.blit(escolha2[6], (567, 206 + 25 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2))
            
            
            
            
            if pygame.key.get_pressed()[pygame.K_q] and px < 400 or pygame.key.get_pressed()[pygame.K_z] and px < 400:
                corda_i(198, 245 + 25 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2)
            elif pygame.key.get_pressed()[pygame.K_p] and px < 400 or pygame.key.get_pressed()[pygame.K_m] and px < 400:
                corda_i(202, 245 + 25 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2)
            else:
                corda_i(200, 245 + 25 + camera(x) *taxa + 1000 + Tela  +  TitleSize/2)
        
            
            pygame.draw.rect(gameDisplay, (0,0,255), (0,580 + camera(x) *taxa + 1000 + Tela,800,50), 0)
            pygame.draw.rect(gameDisplay, (255,0,0), (0,580 + camera(x) *taxa +1000 + Tela,px*2,50), 0)
            
                    
            
            button_pressed = False
            
            if contadorFrames > 600:
                ilevel = "INSANE"
                intensityLevel = 2
                bg_color = (150, 50, 50)
                valorPress = 20
            elif contadorFrames > 400:
                ilevel = "HIGH"
                intensityLevel = 1
                bg_color = (80, 80, 130)
                valorPress = 10
            elif 210 < contadorFrames:
                ilevel = "LOW"
                intensityLevel = 0
                bg_color = (121, 202, 249)
                valorPress = 5
            else:
                ilevel = "NONE"
            
            intensity(100, 100 + camera(x) *taxa + 1000 + Tela, "INTENSITY LEVEL: {0}".format(ilevel), intensityLevel)
            
            if px < 1:
                        
                px = 0
                s = pygame.Surface((800,600))  # the size of your rect
                s.set_alpha(200)                # alpha level
                s.fill((255,255,255))           # this fills the entire surface
                
                if w > 3:
                    j = 0.0
        
                gameDisplay.blit(s, (0,600 + camera_win(w)))
                
                win(-70, 600 + camera_win(w), "BLUE WINS!", (0,0,200))
                    
                if 465 > mouse_pos[0] > 335 and (575 + 600 + camera_win(w)) > mouse_pos[1] > (525 + 600 + camera_win(w)):
                    gameDisplay.blit(start1,(335, 525 + 600 + camera_win(w)))	
                    if click[0] == 1:
                        #px = 200
                        contadorFrames = 0
                        j = -0.15
                        back = True		
                else:
                    gameDisplay.blit(start0,(335, 525 + 600 + camera_win(w)))
             
                w += j
                
            s = pygame.Surface((800,600))  # the size of your rect
            s.set_alpha(200)               # alpha level
            s.fill((255,255,255))
                
                
            if px > 399:
                     
                px = 400
                if w > 3:
                    j = -0.0
                
                    
                gameDisplay.blit(s, (0,600 + camera_win(w)))
                win(-30, 600 + camera_win(w), "RED WINS!", (200,0,0))
                
                if 465 > mouse_pos[0] > 335 and (575 + 600 + camera_win(w)) > mouse_pos[1] > (525 + 600 + camera_win(w)):
                    gameDisplay.blit(start1,(335, 525 + 600 + camera_win(w)))	
                    if click[0] == 1:
                        #px = 200
                        contadorFrames = 0
                        j = -0.15
                        back = True
                else:
                    gameDisplay.blit(start0,(335, 525 + 600 + camera_win(w)))        
                
                w += j
        
            if contadorFrames > 90 and contadorFrames < 130:
                N3(400 - 200*0.5, 300 - 300*0.5)
            if contadorFrames > 130 and contadorFrames < 170:
                N2(400 - 200*0.5, 300 - 300*0.5)
            if contadorFrames > 170 and contadorFrames < 210:
                N1(400 - 200*0.5, 300 - 300*0.5)
                
            if back and w < -7 and px < 200:
                px += 5
                j = 0.15
                if px > 199:
                    back = False
                    contadorBlue += 1
                    valorPress = 0
                    
            if back and w < -7 and px > 200:
                px -= 5
                j = 0.15
                if px < 201:
                    back = False
                    contadorRed += 1
                    valorPress = 0
            
            contadorFrames += 1
        click1 = False
        pygame.display.update()
        
#how much FPS
clock.tick(60)

#quitar o jogo quando sair do loop    
pygame.quit()
quit()