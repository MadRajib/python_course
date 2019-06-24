import sys,pygame

pygame.init()
size = width,height = 800 , 800

white = (255,255,255)
screen = pygame.display.set_mode(size)
pos = x,y = 0,0
speed = 0.5
delta = dx,dy = 0,0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1*speed
            elif event.key == pygame.K_RIGHT:
                dx = 1*speed

            if event.key == pygame.K_UP:
                dy = -1*speed
            elif event.key == pygame.K_DOWN:
                dy = 1*speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 1*0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 1*0
    x += dx
    y += dy
    screen.fill(white)
    
    pygame.draw.rect(screen,(255,0,255),[x,y,140,140],0)

    pygame.display.update()
    