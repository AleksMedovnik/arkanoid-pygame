import pygame

WIDTH, HEIGHT = 1200, 600
fps = 60

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#########################################
# №3
# настройки платформы
paddle_w = 50  # ширина
paddle_h = 10  # высота
paddle_speed = 3  # скорость движения
# определяем объект платформы
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
#########################################

#########################################
# №1
img = pygame.image.load('images/sky.jpg').convert()  # для PNG - convert_alpha
# convert - для ускорения перерисовки
#########################################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #########################################
    # №2
    sc.blit(img, (0, 0))  # Добавляем изображение на карту
    #########################################

    #########################################
    # №4
    # рисуем платформу
    pygame.draw.rect(sc, pygame.Color('green'), paddle)

    # управление платформой
    key = pygame.key.get_pressed()  # кортеж с информацией о состоянии клавиш
    # если стрелка влево нажата И платформа не вышла за макет влево, то...
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed  # перемещаем платформу влево
    # elif key[pygame.K_RIGHT] and paddle.right < WIDTH:
    #     paddle.right += paddle_speed

    #########################################

    pygame.display.flip()
    clock.tick(fps)

# ДЗ
# 1. Установить скорость движения платформы - 15 пикселей.
# 2. Установить ширину платформы - 330 пикселей, а высоту - 35
# 3. При нажатии на стрелку вправо, платформа должна двигаться вправо. При этом, платформа не должна
# # выходить за пределы макета
