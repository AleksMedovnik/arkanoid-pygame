import pygame
from random import randrange as rnd


WIDTH, HEIGHT = 1200, 600
fps = 60

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

paddle_w = 330
paddle_h = 25
paddle_speed = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)

ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)

ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

bl_width = 100
bl_height = 50
margins = 20
first_ind = 10
blocks_hor = 10
blocks_vert = 4

block_list = [
    pygame.Rect(
        first_ind + (bl_width + margins) * i, first_ind + (bl_height + margins) * j, bl_width, bl_height
    ) for i in range(blocks_hor) for j in range(blocks_vert)
]

#####################################################
# №2
# устанавливаем цвет блокам
color_list = [
    (30, 90, 170) for i in range(blocks_hor) for j in range(blocks_vert)
]
#####################################################

img = pygame.image.load('images/sky.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.blit(img, (0, 0))
    #####################################################
    # №1
    # рисуеем блоки
    # [pygame.draw.rect(sc, pygame.Color(247, 176, 45), block) for block in block_list]

    # №3
    # рисуеем разноцветные блоки
    [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]
    #####################################################

    pygame.draw.rect(sc, pygame.Color('green'), paddle)
    pygame.draw.circle(sc, pygame.Color('red'), ball.center, ball_radius)

    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    if ball.centery < ball_radius:
        dy = -dy
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx

    if ball.colliderect(paddle) and dy > 0:
        dy = -dy

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    elif key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    pygame.display.flip()
    clock.tick(fps)

# ДЗ
# 1. Внести изменения в color_list. Цвет должен устанавливаться рандомно для каждого блока.
# Рандомный диапазон - от 30 до 256.

