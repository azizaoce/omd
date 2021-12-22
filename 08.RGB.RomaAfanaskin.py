from abc import ABC, abstractmethod


class ComputerColor(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass


class Color(ComputerColor):
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    def __str__(self):
        return f'{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other):
        if self.red == other.red and self.green == other.green and self.blue == other.blue:
            return True
        else:
            return False

    def __add__(self, other):
        return Color((self.red + other.red) // 2, (self.green + other.green) // 2, (self.blue + other.blue) // 2)

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    def __mul__(self, c):
        contrast_level = - 256 * (1 - c)
        F = 259 * (contrast_level + 255) / (255 * (259 - contrast_level))
        L_red_new = int(F * (self.red - 128) + 128)
        L_green_new = int(F * (self.green - 128) + 128)
        L_blue_new = int(F * (self.blue - 128) + 128)
        new_color = Color(L_red_new, L_green_new, L_blue_new)
        return new_color

    def __rmul__(self, c):
        return self.__mul__(c)


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]

    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    print('функция, которая выводит букву А в определенном цвете')
    print_a(green)
    
