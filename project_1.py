# pip install pygame

################################################
# №1
import pygame

WIDTH, HEIGHT = 300, 300  # размеры окна
fps = 30  # частота кадров в секунду

pygame.init()  # запускаем pygame
sc = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем окно для отображения
clock = pygame.time.Clock()  # создаем объект для отслеживания времени
################################################

# 2
while True:
    ################################################
    # 4
    for event in pygame.event.get():  # цикл по списку событий
        if event.type == pygame.QUIT:  # когда нажали на Крестик,
            exit()  # выйти из программы
    ################################################

    # 3
    pygame.display.flip()  # обновляем дисплей
    clock.tick(fps)  # устанавливаем tick - частоту кадров в секунду
################################################



# ДЗ
# 1. Установить ширину окна - 1200 пикселей, а высоту - 600 пикселей.
# 2. Установить частоту обновления экрана - 60 кадров в секунду.
# 3. Найти и скачать фоновое изображение большого размера (желательно, не меньше 1000/500).
# 4. В папку с проектом добавить папку images для картинок. Добавить в нее фоновое изображение.