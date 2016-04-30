import pygame

pygame.init()

display_width = 800
display_height = 600

cl_x1 = -60
cl_x2 = 600
p11 = pygame.image.load("char1.1.png")
p110 = pygame.transform.flip(p11, True, False)
p12 = pygame.image.load("char1.2.png")
p120 = pygame.transform.flip(p12, True, False)
p21 = pygame.image.load("char2.1.png")
p210 = pygame.transform.flip(p21, True, False)
p22 = pygame.image.load("char2.2.png")
p220 = pygame.transform.flip(p22, True, False)
p31 = pygame.image.load("char3.1.png")
p310 = pygame.transform.flip(p31, True, False)
p32 = pygame.image.load("char3.2.png")
p320 = pygame.transform.flip(p32, True, False)
c1 = pygame.image.load("rope_igual.png")
c1 = pygame.transform.scale(c1, (400, 20))
c_e = pygame.image.load("rope_esquerda1.png")
c_e = pygame.transform.scale(c_e, (400, 20))
c_d = pygame.image.load("rope_direita1.png")
c_d = pygame.transform.scale(c_d, (400, 20))
mountain = pygame.image.load("Pixel_mountain.png")
mountain = pygame.transform.scale(mountain, (1000, 200))

def p_marrom1(x, y):
    gameDisplay.blit((p11), (x, y))
def p_amarelo1(x, y):
    gameDisplay.blit((p21), (x, y))
def p_rosa1(x, y):
    gameDisplay.blit((p31), (x, y))
def p_marrom2(x, y):
    gameDisplay.blit((p12), (x, y))
def p_amarelo2(x, y):
    gameDisplay.blit((p22), (x, y))
def p_rosa2(x, y):
    gameDisplay.blit((p32), (x, y))

def p_marrom10(x, y):
    gameDisplay.blit((p110), (x, y))
def p_amarelo10(x, y):
    gameDisplay.blit((p210), (x, y))
def p_rosa10(x, y):
    gameDisplay.blit((p310), (x, y))
def p_marrom20(x, y):
    gameDisplay.blit((p120), (x, y))
def p_amarelo20(x, y):
    gameDisplay.blit((p220), (x, y))
def p_rosa20(x, y):
    gameDisplay.blit((p320), (x, y))
    
def corda_i(x, y):
    gameDisplay.blit((c1), (x, y))
def corda_e(x, y):
    gameDisplay.blit((c_e), (x, y))
def corda_d(x, y):
    gameDisplay.blit((c_d), (x, y))
    
def mountain_bg(x, y):
    gameDisplay.blit((mountain), (x, y))
    
def cloud1(x, y):
    gameDisplay.blit(pygame.transform.scale((pygame.image.load("Pixel_cloud.png")), (400, 400)), (x, y))
    
    
#def puxar (player, x, y):
    
    
px = 200
    
#window size
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Title
pygame.display.set_caption("Cabo de Guerra")

#FPS
clock = pygame.time.Clock()

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
    
    mountain_bg(-30, 400)
    
    cloud1(cl_x1, -50)
    cloud1(cl_x2, 0)
    cl_x1 += 0.3    
    cl_x2 += 0.3
    
    if cl_x1 > 805:
        cl_x1 = -400
    
    if cl_x2 > 805:
        cl_x2 = -400    
    
    if pygame.key.get_pressed()[pygame.K_q] and px < 400 or pygame.key.get_pressed()[pygame.K_z] and px < 400:
        p_marrom2(185,306)
    else:
        p_marrom1(185,306)
    if pygame.key.get_pressed()[pygame.K_p] and px < 400 or pygame.key.get_pressed()[pygame.K_m] and px < 400:
        p_rosa20(567, 306)
    else:
        p_rosa10(567, 306)
    
    if pygame.key.get_pressed()[pygame.K_q] and px < 400 or pygame.key.get_pressed()[pygame.K_z] and px < 400:
        corda_i(198, 345)
    elif pygame.key.get_pressed()[pygame.K_p] and px < 400 or pygame.key.get_pressed()[pygame.K_m] and px < 400:
        corda_i(202, 345)
    else:
        corda_i(200, 345)
    
    
    
    
    pygame.draw.rect(gameDisplay, (0,0,255), (200,375,400,50), 0)
    pygame.draw.rect(gameDisplay, (255,0,0), (200,375,px,50), 0)
    button_pressed = False
    
    

    pygame.display.update()
    
    #how much FPS
    clock.tick(60)

#quitar o jogo quando sair do loop    
pygame.quit()
quit()