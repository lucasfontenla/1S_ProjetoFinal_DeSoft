import pygame

pygame.init()

display_width = 800
display_height = 600

car = pygame.image.load("White_Square50.png")

def player(x, y):
    gameDisplay.blit((car), (x, y))
    
px = 375
py = 275
    
#window size
gameDisplay = pygame.display.set_mode((display_width, display_height))

#Title
pygame.display.set_caption("A Bit Racey")

#FPS
clock = pygame.time.Clock()

#condição p/ parar o jogo
crashed = False

#game loop
while not crashed:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
    gameDisplay.fill((0, 0, 0))
    player(px, py)
            
    if pygame.key.get_pressed()[pygame.K_DOWN] and py < display_height - 50:
        py += 5
    if pygame.key.get_pressed()[pygame.K_UP] and py > 0:
        py -= 5
    if pygame.key.get_pressed()[pygame.K_LEFT] and px > 0:
        px -= 5
    if pygame.key.get_pressed()[pygame.K_RIGHT] and px < display_width - 50:
        px += 5
            
    pygame.display.update()
    
    #how much FPS
    clock.tick(60)

#quitar o jogo quando sair do loop    
pygame.quit()
quit()