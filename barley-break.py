import arcade
import random
from collections import namedtuple

# устанавливаем константы
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Пятнашки"

ROW_COUNT = 3
COLUMN_COUNT = 3
TILE_WIDTH = 200
TILE_HEIGHT = 200





# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.numbers = arcade.SpriteList()

    # начальные значения
    def setup(self):
        number_choices = list(range(1, 9))
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                num = arcade.Sprite('numbers/1.jpg', 0.39)
                num.center_y = TILE_HEIGHT / 2 + TILE_HEIGHT * row
                num.center_x = TILE_WIDTH / 2 + TILE_WIDTH * column
                self.numbers.append(num)


    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        self.numbers.draw()
        pass

    # игровая логика
    def update(self, delta_time):
        pass
        pass
window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
