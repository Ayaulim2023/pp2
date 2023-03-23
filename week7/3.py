import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

W,H = 800,600
x,y = 50,50
sc = pygame.display.set_mode((W, H))
sc.fill('white')

pygame.draw.circle(sc,'red',(200,200),25)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w :
                if y<45:
                    y += 0
                else:
                  y-=20
            elif event.key == pygame.K_s:
               if y >555:
                   y +=0
               else:
                   y+=20
            elif event.key == pygame.K_a:
                if x <45:
                    x+=0
                else:
                  x-=20
            elif event.key == pygame.K_d:
                if x >755:
                    x+=0
                else:
                   x+=20
           
        sc.fill(WHITE)
# redraw the circle
        pygame.draw.circle(sc,'red', (x,y), 25)

   
    pygame.display.update()