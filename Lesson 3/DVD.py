import sys, pygame, time
pygame.init()

size = width, height = 800, 600
speed = [5, 5]
white = 255, 255, 255

screen = pygame.display.set_mode(size)

dvd = pygame.image.load("dvd.png")
dvd_rect = dvd.get_rect()
dvd = pygame.transform.scale(dvd, (100, int(dvd_rect[3] / dvd_rect[2]*100)))
dvd_rect = dvd.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    dvd_rect = dvd_rect.move(speed)
    if dvd_rect.left < 0 or dvd_rect.right > width:
        speed[0] = -speed[0]
    if dvd_rect.top < 0 or dvd_rect.bottom > height:
        speed[1] = -speed[1]
    time.sleep(0.01)
    #screen.fill(white)
    screen.blit(dvd, dvd_rect)
    pygame.display.update()
