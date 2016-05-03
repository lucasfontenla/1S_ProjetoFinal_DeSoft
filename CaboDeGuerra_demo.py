import pygame
import math

pygame.init()

display_width = 800
display_height = 600

cl_x1 = -60
cl_x2 = 600

TitleSize = 0

n = 0

original = 0
right = 0
left = 1

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
    
        

c1 = pygame.image.load("rope_igual.png")
c1 = pygame.transform.scale(c1, (400, 20))
c_e = pygame.image.load("rope_esquerda1.png")
c_e = pygame.transform.scale(c_e, (400, 20))
c_d = pygame.image.load("rope_direita1.png")
c_d = pygame.transform.scale(c_d, (400, 20))
mountain = pygame.image.load("Pixel_mountain.png")
mountain = pygame.transform.scale(mountain, (1000, 200))
PM = pygame.image.load("Pixel_PM.png")
QZ = pygame.image.load("Pixel_QZ.png")
start0 = pygame.image.load("START_0.png")
start0 = pygame.transform.scale(start0, (200, 200))
start1 = pygame.image.load("START_1.png")
start1 = pygame.transform.scale(start1, (200, 200))

def p_marrom1(x, y):
    character("char1.1.png", (x, y), right)
def p_amarelo1(x, y):
    character("char2.1.png", (x, y), right)
def p_rosa1(x, y):
    character("char3.1.png", (x, y), right)
def p_marrom2(x, y):
    character("char1.2.png", (x, y), right)
def p_amarelo2(x, y):
    character("char2.2.png", (x, y), right)
def p_rosa2(x, y):
    character("char3.2.png", (x, y), right)

def p_marrom10(x, y):
    character("char1.1.png", (x, y), left)
def p_amarelo10(x, y):
    character("char2.1.png", (x, y), left)
def p_rosa10(x, y):
    character("char3.1.png", (x, y), left)
def p_marrom20(x, y):
    character("char1.2.png", (x, y), left)
def p_amarelo20(x, y):
    character("char2.2.png", (x, y), left)
def p_rosa20(x, y):
    character("char3.2.png", (x, y), left)
    
def corda_i(x, y):
    gameDisplay.blit((c1), (x, y))
def corda_e(x, y):
    gameDisplay.blit((c_e), (x, y))
def corda_d(x, y):
    gameDisplay.blit((c_d), (x, y))
    
def mountain_bg(x, y):
    gameDisplay.blit((mountain), (x, y))
    
def cloud1(x, y):
    gameDisplay.blit(pygame.transform.scale((pygame.image.load("Pixel_cloud1.png")), (400, 400)), (x, y))
    
def PM_bg(x, y):
    gameDisplay.blit((PM), (x, y))
def QZ_bg(x, y):
    gameDisplay.blit((QZ), (x, y))
    
def TugWar(x, y):
    gameDisplay.blit((Tug), (x, y))
    
    
#def puxar (player, x, y):
    
    
px = 200
    
#window size
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Title
pygame.display.set_caption("Cabo de Guerra")

#FPS
clock = pygame.time.Clock()

Tela = 2000

def camera(x):
    cam = Tela*(1/(1 + math.e**-(0.7*x)))
    return -cam
    
x = -20

select = False

while not select:
    gameDisplay.fill((9, 120, 236))
    gameDisplay.blit(start0,(400 - 65, 550 - 25))
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
#           sys.exit()
    
    Tug = pygame.image.load("Tug_War.png")
    Tug = pygame.transform.scale(Tug, (800 + TitleSize, 800 + TitleSize))
            
    TitleSize = int((15*(1+math.sin(2*3.14*n*0.01)))*0.5)
    n -= 1
            
            
    TugWar(40 - TitleSize/3, -200 - TitleSize/3) 
    if 400 - 65 + 130 > mouse_pos[0] > 400 - 65 and 575 > mouse_pos[1] > 550 - 25:
        gameDisplay.blit(start1,(400 - 65, 550 - 25))	
        if click[0] == 1:
            select = True		
    else:
        gameDisplay.blit(start0,(400 - 65, 550 - 25))
            
    pygame.display.update()


######################################################################################################



#condição p/ parar o jogo
crashed = False

#game loop
while not crashed:
    
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            crashed = True
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_q and px < 400:
                px += 5  
            if ev.key == pygame.K_p and px > 0:
                px -= 5
            if ev.key == pygame.K_z and px < 400:
                px += 5
            if ev.key == pygame.K_m and px > 0:
                px -= 5
    

    
            
    gameDisplay.fill((9, 120, 236))
    
    mountain_bg(-30, 400 + camera(x) + Tela)
    

    cloud1(cl_x1 + 60, -100 + camera(x) + Tela - 2000)
    cloud1(cl_x1 + 600, 0 + camera(x) + Tela - 2000)
    cloud1(cl_x1 - 50, -150 + camera(x) + Tela - 1600)
    cloud1(cl_x1 + 500, 50 + camera(x) + Tela - 1600)
    cloud1(cl_x1 + 200, -250 + camera(x) + Tela - 1200)
    cloud1(cl_x1 + 650, 0 + camera(x) + Tela - 1200)
    cloud1(cl_x1 - 100, -150 + camera(x) + Tela - 800)
    cloud1(cl_x1 + 300, 50 + camera(x) + Tela - 800)
    cloud1(cl_x1 - 200, -50 + camera(x) + Tela - 400)
    cloud1(cl_x1 + 400, 100 + camera(x) + Tela - 400)
    cloud1(cl_x1, -50 + camera(x) + Tela)
    cloud1(cl_x2, 0 + camera(x) + Tela)
    cl_x1 += 0.3    
    cl_x2 += 0.3
    
    if cl_x1 > 805:
        cl_x1 = -400
    
    if cl_x2 > 805:
        cl_x2 = -400
        
    
        
    QZ_bg(90,215 + camera(x) + Tela)
    PM_bg(570,215 + camera(x) + Tela)
    
    x += 0.1    
    
    if pygame.key.get_pressed()[pygame.K_q] and px < 400 or pygame.key.get_pressed()[pygame.K_z] and px < 400:
        p_marrom2(185,206 + 25 + camera(x) + Tela)
    else:
        p_marrom1(185,206 + 25 + camera(x) + Tela)
    if pygame.key.get_pressed()[pygame.K_p] and px < 400 or pygame.key.get_pressed()[pygame.K_m] and px < 400:
        p_rosa20(567, 206 + 25 + camera(x) + Tela)
    else:
        p_rosa10(567, 206 + 25 + camera(x) + Tela)
    
    if pygame.key.get_pressed()[pygame.K_q] and px < 400 or pygame.key.get_pressed()[pygame.K_z] and px < 400:
        corda_i(198, 245 + 25 + camera(x) + Tela)
    elif pygame.key.get_pressed()[pygame.K_p] and px < 400 or pygame.key.get_pressed()[pygame.K_m] and px < 400:
        corda_i(202, 245 + 25 + camera(x) + Tela)
    else:
        corda_i(200, 245 + 25 + camera(x) + Tela)
    
    
    
    pygame.draw.rect(gameDisplay, (0,0,255), (200,300 + camera(x) + Tela,400,50), 0)
    pygame.draw.rect(gameDisplay, (255,0,0), (200,300 + camera(x) + Tela,px,50), 0)
    button_pressed = False
    
    

    pygame.display.update()
    
    #how much FPS
    clock.tick(60)

#quitar o jogo quando sair do loop    
pygame.quit()
quit()