import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First game")


x = 50
y = 50
width = 60
height = 40
vel = 5

bounce = True
bounce_counter = 0

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    if x < (500 - width) and bounce:
        x += vel
    else:
        bounce = False
    if x != 0 and not bounce:
        x -= vel
    else:
        bounce = True

    if 500 - width == x:
        bounce_counter += 1
        print(bounce_counter)

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
