import sys, pygame

pygame.init()

size = width,height = 600 , 600

screen = pygame.display.set_mode(size)
white =  (255,255,255)

x = 0
y = 0
speed = 0.5
dx = dy = 0
while True:

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

    #                       (R  , G, B),[x,y  , height,width],
    pygame.draw.rect(screen,(255,0,255),[x,y,140,140],0)

    x +=1*speed
    
    pygame.display.update()
