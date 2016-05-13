import pygame, math, eztext, eztextNum, os
from Servidor.UDPgameClient import Client 

#os.system('UDPgameServer.py')

pygame.init()

display_width = 800
display_height = 600



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


#class Thing:

#    def Object(self, img, position, size, orientation):
#        self.img = pygame.image.load(img)
#        if orientation == left:
#            self.img = pygame.transform.flip(self.img, True, False)
#        if size != original:
#            self.img = pygame.transform.scale(self.img, size)
#        gameDisplay.blit(self.img, position)
#        
def character(img, position, orientation):
#    Thing.Object(img, position, 0, orientation)
    im = pygame.image.load(img)
    if orientation == left:
        im = pygame.transform.flip(im, True, False)
#    if size != original:
#        self.img = pygame.transform.scale(self.img, size)
    gameDisplay.blit(im, position)    
    
        

c1 = pygame.image.load("CDG_Images/rope_igual.png")
c1 = pygame.transform.scale(c1, (400, 20))
c_e = pygame.image.load("CDG_Images/rope_esquerda1.png")
c_e = pygame.transform.scale(c_e, (400, 20))
c_d = pygame.image.load("CDG_Images/rope_direita1.png")
c_d = pygame.transform.scale(c_d, (400, 20))
mountain = pygame.image.load("CDG_Images/Pixel_mountain.png")
mountain = pygame.transform.scale(mountain, (1000, 200))
PM = pygame.image.load("CDG_Images/Pixel_PM.png")
QZ = pygame.image.load("CDG_Images/Pixel_QZ.png")
start0 = pygame.image.load("CDG_Images/START_0.png")
start0 = pygame.transform.scale(start0, (200, 200))
start1 = pygame.image.load("CDG_Images/START_1.png")
start1 = pygame.transform.scale(start1, (200, 200))
localW = pygame.image.load("CDG_Images/Pixel_local_W.png")
localW = pygame.transform.scale(localW, (600, 50))
localY = pygame.image.load("CDG_Images/Pixel_local_Y.png")
localY = pygame.transform.scale(localY, (600, 50))
onlineW = pygame.image.load("CDG_Images/Pixel_online_W.png")
onlineW = pygame.transform.scale(onlineW, (600, 50))
onlineY = pygame.image.load("CDG_Images/Pixel_online_Y.png")
onlineY = pygame.transform.scale(onlineY, (600, 50))
n3 = pygame.image.load("CDG_Images/No_3.png")
n3 = pygame.transform.scale(n3, (300, 300))
n2 = pygame.image.load("CDG_Images/No_2.png")
n2 = pygame.transform.scale(n2, (300, 300))
n1 = pygame.image.load("CDG_Images/No_1.png")
n1 = pygame.transform.scale(n1, (300, 300))
win_font = pygame.font.SysFont("pixelmix Regular", 100)
wintext = win_font.render("YOU WIN!", True, (0,0,0))


bgLow = pygame.image.load("CDG_Images/new_background.png")
bgHigh = pygame.image.load("CDG_Images/background_hard.png")
bgInsane = pygame.image.load("CDG_Images/background_insane.png")

#win_bg = pygame.Color.a(30)

def p_marrom1(x, y):
    character("CDG_Images/char1.1.png", (x, y), right)
def p_amarelo1(x, y):
    character("CDG_Images/char2.1.png", (x, y), right)
def p_rosa1(x, y):
    character("CDG_Images/char3.1.png", (x, y), right)
def p_marrom2(x, y):
    character("CDG_Images/char1.2.png", (x, y), right)
def p_amarelo2(x, y):
    character("CDG_Images/char2.2.png", (x, y), right)
def p_rosa2(x, y):
    character("CDG_Images/char3.2.png", (x, y), right)

def p_marrom10(x, y):
    character("CDG_Images/char1.1.png", (x, y), left)
def p_amarelo10(x, y):
    character("CDG_Images/char2.1.png", (x, y), left)
def p_rosa10(x, y):
    character("CDG_Images/char3.1.png", (x, y), left)
def p_marrom20(x, y):
    character("CDG_Images/char1.2.png", (x, y), left)
def p_amarelo20(x, y):
    character("CDG_Images/char2.2.png", (x, y), left)
def p_rosa20(x, y):
    character("CDG_Images/char3.2.png", (x, y), left)
    
def corda_i(x, y):
    gameDisplay.blit((c1), (x, y))
def corda_e(x, y):
    gameDisplay.blit((c_e), (x, y))
def corda_d(x, y):
    gameDisplay.blit((c_d), (x, y))
    
def mountain_bg(x, y):
    gameDisplay.blit((mountain), (x, y))
    
#def cloud1(x, y):
#    gameDisplay.blit(pygame.transform.scale((pygame.image.load("CDG_Images/Pixel_cloud1.png")), (400, 400)), (x, y))
    
def cloud1(x, y):
    cld1 = pygame.image.load("CDG_Images/fred_cloud1.png")
    cld1 = pygame.transform.flip(cld1, True, False)
    cld1 = pygame.transform.scale((cld1), (500, 350))
    gameDisplay.blit((cld1), (x, y))
def cloud2(x, y):
    cld1 = pygame.image.load("CDG_Images/fred_cloud2.png")
    cld1 = pygame.transform.flip(cld1, True, False)
    cld1 = pygame.transform.scale((cld1), (300, 150))
    gameDisplay.blit((cld1), (x, y))
    
    
def PM_bg(x, y):
    gameDisplay.blit((PM), (x, y))
def QZ_bg(x, y):
    gameDisplay.blit((QZ), (x, y))
    
def TugWar(x, y):
    gameDisplay.blit((Tug), (x, y))
    
def N3(x, y):
    gameDisplay.blit((n3), (x, y))
def N2(x, y):
    gameDisplay.blit((n2), (x, y))
def N1(x, y):
    gameDisplay.blit((n1), (x, y))
    
def anyText(x, y, txt, colour):
    fonte = pygame.font.SysFont("pixelmix Regular", 20)
    ay = fonte.render(txt, True, colour)
    gameDisplay.blit((ay), (x, y))
    
def anyText40(x, y, txt, colour):
    fonte = pygame.font.SysFont("pixelmix Regular", 40)
    ay = fonte.render(txt, True, colour)
    gameDisplay.blit((ay), (x, y))
    
def win(x, y, txt, colour):
#    gameDisplay.blit((win_bg), (x, y))
    win_font = pygame.font.SysFont("pixelmix Regular", 100)
    wintext = win_font.render(txt, True, colour)
    gameDisplay.blit((wintext), (x + 150, y + 200))
    
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
        
def bgLOW(x, y):
    gameDisplay.blit((bgLow), (x, y))
def bgHIGH(x, y):
    gameDisplay.blit((bgHigh), (x, y))
def bgINSANE(x, y):
    gameDisplay.blit((bgInsane), (x, y))

    
px = 200
    
#window size
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Title
pygame.display.set_caption("Tug War - O melhor jogo do Brasil")

#FPS
clock = pygame.time.Clock()

Tela = 2000

def camera(x):
    cam = Tela*(1/(1 + math.e**-(0.7*x)))
    return -cam
    
def camera_win(x):
    cam = 600*(1/(1 + math.e**-(2*x)))
    return -cam
    
x = -12

select0 = False
select1 = False
select10 = False
select11 = False
enter = False

pixelFont = pygame.font.SysFont("pixelmix Regular", 40)
white = (255,255,255)
question = eztextNum.Input(maxlength=20, color=white, prompt='IP: ')

while not select0 or not select1:
    gameDisplay.fill((121, 202, 249))
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
#            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SLASH:
                enter = True

          
            
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
        if click[0] == 1:
            select0 = True
            break
    elif select1 == False:
        gameDisplay.blit(localW,(120, 520))
        
    if select1 == False and 700 > mouse_pos[0] > 500 and 570 > mouse_pos[1] > 520:
        gameDisplay.blit(onlineY,(500, 520))	
        if click[0] == 1:
            select1 = True
            break
    elif select1 == False:
        gameDisplay.blit(onlineW,(500, 520))
    

    pygame.display.update()
    
    
    
    
    
while select1:
    gameDisplay.fill((121, 202, 249))
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
#            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SLASH:
                enter = True
            
    if enter:
        print("oi")
          
            
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
    

    
#    gameDisplay.blit(onlineW,(300, 520))
        
    if select11 == False and 300 > mouse_pos[0] > 120 and 570 > mouse_pos[1] > 520:
        anyText40(120, 520, "CREATE", (255,255,0))	
        if click[0] == 1:
            select10 = True		
    elif select11 == False:
        anyText40(120, 520, "CREATE", (255,255,255))	
            
    if select11 == False and 700 > mouse_pos[0] > 500 and 570 > mouse_pos[1] > 520:
        anyText40(500, 520, "JOIN", (255,255,0))	
        if click[0] == 1:
            select11 = True		
    elif select11 == False:
        anyText40(500, 520, "JOIN", (255,255,255))            
        
    if select11 == True:
        question.set_pos(200, 520)
        question.set_font(pixelFont)
        question.draw(gameDisplay)
        question.update(pygame.event.get())
        print(question.value)
        if question.enter:
            pesquisarIP = True
               
            select0 = True
            break

    pygame.display.update()
    
    
    
    
    
    
    
    
    

#select = False
#
#while not select:
#    gameDisplay.fill((121, 202, 249))
#    mouse_pos = pygame.mouse.get_pos()
#    click = pygame.mouse.get_pressed()
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
##           sys.exit()
#          
#            
#    cloud1(cl_x3, -100 + camera(x) + Tela - 2000)
#    cloud1(cl_x4, 0 + camera(x) + Tela - 2000)
#    cloud1(cl_x5, -150 + camera(x) + Tela - 1600)
#    cloud1(cl_x6, 50 + camera(x) + Tela - 1600)
#    
#    cl_x1 += 0.3    
#    cl_x2 += 0.3
#    cl_x3 += 0.3    
#    cl_x4 += 0.3
#    cl_x5 += 0.3
#    cl_x6 += 0.3
#    cl_x7 += 0.3
#    cl_x8 += 0.3
#    cl_x9 += 0.3
#    cl_x10 += 0.3
#    cl_x11 += 0.3
#    cl_x12 += 0.3
#    
#    if cl_x1 > 805:
#        cl_x1 = -400
#    if cl_x2 > 805:
#        cl_x2 = -400
#    if cl_x3 > 805:
#        cl_x3 = -400
#    if cl_x4 > 805:
#        cl_x4 = -400
#    if cl_x5 > 805:
#        cl_x5 = -400
#    if cl_x6 > 805:
#        cl_x6 = -400
#    if cl_x7 > 805:
#        cl_x7 = -400
#    if cl_x8 > 805:
#        cl_x8 = -400
#    if cl_x9 > 805:
#        cl_x9 = -400
#    if cl_x10 > 805:
#        cl_x10 = -400
#    if cl_x11 > 805:
#        cl_x11 = -400
#    if cl_x12 > 805:
#        cl_x12 = -400
#
#    if 300 > mouse_pos[0] > 120 and 570 > mouse_pos[1] > 520:
#        gameDisplay.blit(localY,(120, 520))	
#        if click[0] == 1:
#            select = True		
#    else:
#        gameDisplay.blit(localW,(120, 520))
#        
#    if 700 > mouse_pos[0] > 500 and 570 > mouse_pos[1] > 520:
#        gameDisplay.blit(onlineY,(500, 520))	
#        if click[0] == 1:
#            select = True
#            eztext.Input.update()
#    else:
#        gameDisplay.blit(onlineW,(500, 520))
#        
#                 
#    
#    pygame.display.update()


######################################################################################################
contadorFrames = 0

w = -7
back = False

#condição p/ parar o jogo
crashed = False

valorPress = 0

bg_color = ((121, 202, 249))

#game loop
while select0:
    click = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            select0 = False
        
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_q and px < 400 and px > 0:
                px += valorPress 
            if ev.key == pygame.K_p and px > 0 and px < 400:
                px -= valorPress
            if ev.key == pygame.K_z and px < 400 and px > 0:
                px += valorPress
            if ev.key == pygame.K_m and px > 0 and px < 400:
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
    
    QZ_bg(90,215 + camera(x) *taxa + 1000 + Tela)
    PM_bg(570,215 + camera(x) *taxa + 1000 + Tela)
    
    x += 0.1

    anyText(200, 350 + camera(x) *taxa + 1000 + Tela, ("WINS: {0}".format(contadorRed)), (255,0,0))
    anyText(510, 350 + camera(x) *taxa + 1000 + Tela, ("WINS: {0}".format(contadorBlue)), (0,0,255))    
    
    if pygame.key.get_pressed()[pygame.K_q] and px < 400 or pygame.key.get_pressed()[pygame.K_z] and px < 400:
        p_marrom2(185,206 + 25 + camera(x) *taxa + 1000 + Tela)
    else:
        p_marrom1(185,206 + 25 + camera(x) *taxa + 1000 + Tela)
    if pygame.key.get_pressed()[pygame.K_p] and px < 400 or pygame.key.get_pressed()[pygame.K_m] and px < 400:
        p_rosa20(567, 206 + 25 + camera(x) *taxa + 1000 + Tela)
    else:
        p_rosa10(567, 206 + 25 + camera(x) *taxa + 1000 + Tela)
    
    if pygame.key.get_pressed()[pygame.K_q] and px < 400 or pygame.key.get_pressed()[pygame.K_z] and px < 400:
        corda_i(198, 245 + 25 + camera(x) *taxa + 1000 + Tela)
    elif pygame.key.get_pressed()[pygame.K_p] and px < 400 or pygame.key.get_pressed()[pygame.K_m] and px < 400:
        corda_i(202, 245 + 25 + camera(x) *taxa + 1000 + Tela)
    else:
        corda_i(200, 245 + 25 + camera(x) *taxa + 1000 + Tela)

    
    pygame.draw.rect(gameDisplay, (0,0,255), (200,300 + camera(x) *taxa + 1000 + Tela,400,50), 0)
    pygame.draw.rect(gameDisplay, (255,0,0), (200,300 + camera(x) *taxa +1000 + Tela,px,50), 0)
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
    
    pygame.display.update()
    
    #how much FPS
    clock.tick(60)

#quitar o jogo quando sair do loop    
pygame.quit()
quit()




