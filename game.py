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


class NumberCard(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


# класс с игрой
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.numbers = arcade.SpriteList()
        self.num_coords = []
        self.game = True
        self.endgame = arcade.load_texture('numbers/win.jpg')
        self.number = namedtuple('Number', 'number center_x center_y')
        self.is_move = False

    # начальные значения
    def setup(self):
        number_choices = list(range(1, 9))
        propusk = random.randint(1, 9)
        counter = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                counter += 1
                if counter == propusk:
                    self.num_coords.append(self.number(9, 200 * row + TILE_WIDTH / 2, 200 * column + TILE_HEIGHT / 2))
                    continue
                random.shuffle(number_choices)
                num_tile = number_choices.pop()
                num = NumberCard(f'numbers/{num_tile}.jpg', 0.39)
                num.center_x = 200 * row + TILE_WIDTH / 2
                num.center_y = 200 * column + TILE_HEIGHT / 2
                self.num_coords.append(self.number(num_tile, num.center_x, num.center_y))
                self.numbers.append(num)
        print(self.num_coords)

    # отрисовка
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        self.numbers.draw()
        if self.game == False:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.endgame)

    # игровая логика
    def update(self, delta_time):
        if self.is_move:
            self.numbers.update()

        if self.num_coords == sorted(self.num_coords):
            self.game = False

    # нажать на клавишу
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        for num, center_x, center_y in self.num_coords:
            if abs(x - center_x) < TILE_WIDTH / 2 and abs(y - center_y) < TILE_HEIGHT / 2:

                change_number = self.number(num, center_x, center_y)  # это число, на которое ткнули
                change_number_index = self.num_coords.index(change_number)
                print(f'change_number = {change_number}')
                for num, center_x, center_y in self.num_coords:
                    # проверки того, что находится по сторонам
                    left = change_number.center_x - TILE_WIDTH == center_x and change_number.center_y == center_y
                    right = change_number.center_x + TILE_WIDTH == center_x and change_number.center_y == center_y
                    top = change_number.center_y + TILE_HEIGHT == center_y and change_number.center_x == center_x
                    bottom = change_number.center_y - TILE_HEIGHT == center_y and change_number.center_x == center_x
                    is_empty = num == 9  # проверка пустого места

                    def left_right():
                        empty_number_index = self.num_coords.index(self.number(num, center_x, center_y))

                        for card in self.numbers:
                            if card.center_x == change_number.center_x and card.center_y == change_number.center_y:
                                change_card = card  # спрайт с change_number

                        change_card.center_x = center_x
                        self.num_coords[change_number_index] = self.number(change_number.number, change_card.center_x,
                                                                           change_card.center_y)
                        self.num_coords[empty_number_index] = self.number(9, change_number.center_x,
                                                                          change_number.center_y)
                        print(self.num_coords[change_number_index])
                        self.num_coords[change_number_index], self.num_coords[empty_number_index] = self.num_coords[
                                                                                                        empty_number_index], \
                                                                                                    self.num_coords[
                                                                                                        change_number_index]

                    def top_bottom():
                        empty_number_index = self.num_coords.index(self.number(num, center_x, center_y))

                        for card in self.numbers:
                            if card.center_x == change_number.center_x and card.center_y == change_number.center_y:
                                change_card = card  # спрайт с change_number

                        change_card.center_y = center_y
                        self.num_coords[change_number_index] = self.number(change_number.number, change_card.center_x,
                                                                           change_card.center_y)
                        self.num_coords[empty_number_index] = self.number(9, change_number.center_x,
                                                                          change_number.center_y)
                        print(self.num_coords[change_number_index])
                        self.num_coords[change_number_index], self.num_coords[empty_number_index] = self.num_coords[
                                                                                                        empty_number_index], \
                                                                                                    self.num_coords[
                                                                                                        change_number_index]

                    if left and is_empty:
                        print(f'слева {num}, его х = {center_x}, его y = {center_y}')
                        left_right()

                    if right and is_empty:
                        print(f'справа {num}')
                        left_right()

                    if top and is_empty:
                        print(f'сверху {num}')
                        top_bottom()

                    if bottom and is_empty:
                        print(f'снизу {num}')
                        top_bottom()


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
