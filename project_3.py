import pygame
##########################################
# №1
from random import randrange as rnd

# print(rnd(1, 50, 10))
##########################################

WIDTH, HEIGHT = 1200, 600
fps = 60

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

paddle_w = 330
paddle_h = 25
paddle_speed = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)

##########################################
# №2
# настройки шарика
ball_radius = 10  # радиус
ball_speed = 2  # скорость движения
ball_rect = int(ball_radius * 2 ** 0.5)  # сторона квадрата внутри шарика по теореме Пифагора
# определяем объект шарика
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1  # напрвление движения шарика
##########################################

img = pygame.image.load('images/sky.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.blit(img, (0, 0))
    pygame.draw.rect(sc, pygame.Color('green'), paddle)

    ##########################################
    # №3
    # рисуем шарик
    pygame.draw.circle(sc, pygame.Color('red'), ball.center, ball_radius)
    # движение шарика
    ball.x += ball_speed * dx  # по оси X
    ball.y += ball_speed * dy  # по оси Y
    # столкновение шарика с верхним бортом макета
    if ball.centery < ball_radius:
        dy = -dy

    # столкновение лево-право
    # if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
    #     dx = -dx
    ##########################################

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    elif key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    pygame.display.flip()
    clock.tick(fps)

# ДЗ
# 1. Установить радиус шарика 20 пикселей.
# 2. Установить скорость движения шарика 6 пикселей.
# 3. Настроить столкновение шарика с левым и правым бортами макета
