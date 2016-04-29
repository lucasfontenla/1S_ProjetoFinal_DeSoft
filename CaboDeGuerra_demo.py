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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
    gameDisplay.fill((30, 35, 40))
#    player(px, py)
    
    pygame.draw.rect(gameDisplay, (0,0,255), (200,275,400,50), 0)
    pygame.draw.rect(gameDisplay, (255,0,0), (200,275,px,50), 0)

    if pygame.key.get_pressed()[pygame.K_q] and px > 0 or pygame.key.get_pressed()[pygame.K_p] and px > 0:
        px -= 1
    if pygame.key.get_pressed()[pygame.K_RSHIFT] and px < 400 or pygame.key.get_pressed()[pygame.K_LSHIFT] and px < 400:
        px += 1
            
    pygame.display.update()
    
    #how much FPS
    clock.tick(60)

#quitar o jogo quando sair do loop    
pygame.quit()
quit()