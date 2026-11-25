import pygame
from time import sleep
from random import uniform as func

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# м'яч
x, y = WIDTH // 2, HEIGHT // 2
radius = 10

# границі для центра м'яча
border_l = bound + radius
border_r = WIDTH - bound - radius
border_u = bound + radius
border_d = HEIGHT - bound - radius

# швидкість м'яча
velocity = 8
vx = velocity * func(-1, 1)
vy = velocity * func(-1, 1)

# майданчик
height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height
vp = 10

# збільшення швидкості на 50% після кожного відбиття від майданчика
num = 1.5

# очки
score = 0
points = 10   # скільки очок дається за одне відбиття


def drawScore():
    win.fill(black)
    pygame.font.init()
    path = pygame.font.match_font("arial")
    Font = pygame.font.Font(path, 30)
    text = "Your score: " + str(score)
    a = Font.render(text, 1, (255, 255, 255))
    win.blit(a, a.get_rect(center=(WIDTH // 2, HEIGHT // 3)))
    pygame.display.update()


def drawWindow():
    win.fill(black)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))  # up
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))  # left
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))  # right
    # pygame.draw.rect(win, white, (0, HEIGHT - bound, WIDTH, bound))  # down
    pygame.draw.circle(win, green, (x, y), radius)
    pygame.draw.rect(win, white, (xp, yp, width, height))
    pygame.display.update()


run = True

while run:
    clock.tick(c2s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # рух майданчика
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - bound - width:
        xp += vp

    # відбиття від границь
    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    if y + vy < border_u:
        vy = -vy

    # нижня границя: відбиття від майданчика або кінець гри
    if y + vy > border_d:
        if xp <= x + vx <= xp + width:
            vy = -vy
            vx *= num
            vy *= num
            score += points
        else:
            drawScore()
            sleep(10)
            run = False

    # рух м'яча
    x += vx
    y += vy

    drawWindow()

pygame.quit()