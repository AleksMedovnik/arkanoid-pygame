import pygame
from random import randrange as rnd

#####################################################
# №2
# генератор списка
lst = [i for i in range(10) if i % 2]
print(lst)  # [1, 3, 5, 7, 9]

# ДЗ №2
# lst = [i * 3 for i in range(10) if i % 2]

#####################################################
# №3
# enumerate
arr = [10, 20, 30, 40, 50]
enum = enumerate(arr, start=1)
for i, val in enum:
    print(f'Номер: {i}, значение: {val}')

# Номер: 1, значение: 10
# Номер: 2, значение: 20
# Номер: 3, значение: 30
# Номер: 4, значение: 40
# Номер: 5, значение: 50

# ДЗ №3
# users = ['Denis', 'John', 'Peter']
# enum = enumerate(users, start=10)
# for i, val in enum:
#     print(f'ID: {i}, Name: {val}')

#####################################################

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

img = pygame.image.load('images/sky.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.blit(img, (0, 0))

    pygame.draw.rect(sc, pygame.Color('green'), paddle)
    pygame.draw.circle(sc, pygame.Color('red'), ball.center, ball_radius)

    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    if ball.centery < ball_radius:
        dy = -dy
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx

    #####################################################
    # №1
    # Столкновение шарика с платформой
    # если шарик пересекается с платформой и движется вниз, ...
    if ball.colliderect(paddle) and dy > 0:
        # dy = -dy
        pass  # ДЗ - изменить направление движения

    #####################################################

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    elif key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += paddle_speed

    pygame.display.flip()
    clock.tick(fps)

# ДЗ
# 1. Если шарик пересекается с платформой и движется вниз, оттолкнуть его от платформы
# 2. Сгенерировать список, состоящий из нечетных чисел от 1 до 10, умноженных на три. [3, 9, 15, 21, 27]
# 3. При помощи enumerate вывести в консоль следующие сообщения:
# ID: 10, Name: Denis
# ID: 11, Name: John
# ID: 12, Name: Peter
