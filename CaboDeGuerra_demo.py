import pygame

pygame.init()

display_width = 800
display_height = 600

car = pygame.image.load("White_Square50.png")

def player(x, y):
    gameDisplay.blit((car), (x, y))
    
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
            if ev.key == pygame.K_q and px > 0:
                px += 5
            if ev.key == pygame.K_p and px > 0:
                px -= 5
            if ev.key == pygame.K_LSHIFT and px < 400:
                px += 5
            if ev.key == pygame.K_RSHIFT and px < 400:
                px -= 5
            
            
    gameDisplay.fill((30, 35, 40))
#    player(px, py)
    
    pygame.draw.rect(gameDisplay, (0,0,255), (200,375,400,50), 0)
    pygame.draw.rect(gameDisplay, (255,0,0), (200,375,px,50), 0)
    button_pressed = False
    
        
#    if pygame.key.get_pressed()[pygame.K_RSHIFT] and px < 400 or \
#       pygame.key.get_pressed()[pygame.K_LSHIFT] and px < 400:
#        px += 1
            
    pygame.display.update()
    
    #how much FPS
    clock.tick(60)

#quitar o jogo quando sair do loop    
pygame.quit()
quit()