import sys, pygame, random, math
pygame.init()

SCREEN = pygame.display.Info()
WIDTH, HEIGHT = SCREEN.current_w, SCREEN.current_h
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = pygame.image.load("lake.jpg")
BACKGROUND = pygame.transform.smoothscale(BACKGROUND, (WIDTH, HEIGHT))

IMG = pygame.image.load("leaf.png")
IMG = pygame.transform.smoothscale(IMG, (100, HEIGHT * 0.25))
PADDLE_1 = IMG.get_rect(topleft = (0, HEIGHT * 0.375))
PADDLE_2 = IMG.get_rect(topleft = (WIDTH - (WIDTH * 0.055), HEIGHT * 0.375))

BALL = pygame.image.load("frog.png").convert_alpha()
BALL = pygame.transform.smoothscale(BALL, (100, 100))
BALL_RECT = BALL.get_rect(center = (WIDTH / 2, HEIGHT / 2))

DIR = random.randint(0, 10) * 360
SPEED = [3 * math.sin(DIR), 3 * math.cos(DIR)]

while 1:
    SCREEN.blit(BACKGROUND, (0, 0))
    pygame.display.set_caption("Frog front pong")
    pygame.display.set_icon(BALL)
    SCREEN.blit(IMG, PADDLE_1)
    SCREEN.blit(IMG, PADDLE_2)
    SCREEN.blit(BALL, BALL_RECT)

    BALL_RECT = BALL_RECT.move(SPEED)

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and PADDLE_1.top > 0:
        PADDLE_1.move_ip(0, -8)
    if key[pygame.K_s] and PADDLE_1.bottom < HEIGHT - 100:
        PADDLE_1.move_ip(0, 8)
    if key[pygame.K_UP] and PADDLE_2.top > 0:
        PADDLE_2.move_ip(0, -8)
    if key[pygame.K_DOWN] and PADDLE_2.bottom < HEIGHT - 100:
        PADDLE_2.move_ip(0, 8)

    if BALL_RECT.top < 0 or BALL_RECT.bottom > HEIGHT - 100:
        SPEED[0], SPEED[1] = SPEED[0] * 1.05, -SPEED[1] * 1.05
    if BALL_RECT.colliderect(PADDLE_1) or BALL_RECT.colliderect(PADDLE_2):
        SPEED[0], SPEED[1] = -SPEED[0] * 1.1, -SPEED[1] * 1.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()
