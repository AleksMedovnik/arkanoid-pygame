import pygame
from random import randrange as rnd

# ДЗ
# lst = [10, 20, 30, 40, 50]
# index = int(input('Enter the index: '))
# print(lst.pop(index))
# print(lst)


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


#####################################################
# №1
# определим направление движения шарика
def detect_collision(dx, dy, ball, rect):
    if dx > 0:  # если шарик движется враво
        delta_x = ball.right - rect.left  # delta_x > 0 - пересечение есть
    else:  # если шарик движется влево
        delta_x = rect.right - ball.left  # delta_x > 0 - пересечение есть
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:  # если шарик касается угла объекта
        dx, dy = -dx, -dy  # шарик движется в противоположных направлениях
    elif delta_x > delta_y:  # если шарик касается верхней части блока
        dy = -dy  # изменить направление вверх
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#####################################################


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
        #####################################################
        # №2
        # настроить столкновение шарика с платформой
        dx, dy = detect_collision(dx, dy, ball, paddle)
        #####################################################

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    elif key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    pygame.display.flip()
    clock.tick(fps)

# ДЗ
# Дан список: lst = [10, 20, 30, 40, 50]
# Запросить у пользователя ввести число. Затем вывести элемент списка с таким индексом и удалить его.
# Попробуйте вывести элемент в консоль и удалить его в одной инструкции
