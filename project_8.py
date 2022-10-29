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

color_list = [
    (rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(blocks_hor) for j in range(blocks_vert)
]

img = pygame.image.load('images/sky.jpg').convert()


def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.blit(img, (0, 0))
    [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)]

    pygame.draw.rect(sc, pygame.Color('green'), paddle)
    pygame.draw.circle(sc, pygame.Color('red'), ball.center, ball_radius)

    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    if ball.centery < ball_radius:
        dy = -dy
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx

    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)


    ###########################################################
    # №1
    # индекс столкновения шарика со списком блоков
    # вернет индекс блока или -1, если столкновения нет
    hit_index = ball.collidelist(block_list)
    if hit_index != -1: # если столкновения было
        # block_list.pop(hit_index)
        # color_list.pop(hit_index)

        hit_rect = block_list.pop(hit_index) # удаляем блок по индексу
        hit_color = color_list.pop(hit_index) # удаляем цвет из списка

        # эффект увеличения блока при столкновении
        hit_rect.inflate_ip(ball.width * 1.5, ball.height * 1.5)
        # рисуем временный объект увеличения
        pygame.draw.rect(sc, hit_color, hit_rect)

        # ДЗ
        # dx, dy = detect_collision(dx, dy, ball, hit_rect)
        # ball_speed += 0.2
    ###########################################################

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    elif key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    pygame.display.flip()
    clock.tick(fps)

# ДЗ
# 1. При столкновении шарика с блоками необходимо оттолкнуть шарик при помощи функции detect_collision.
# 2. После удаления блока скорость шарика увеличить на 0.2
