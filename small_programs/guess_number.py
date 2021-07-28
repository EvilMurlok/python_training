"""
A game in which you have to guess a number based on your intuition and hints.
"""
import random


def input_right_border():
    flag = False
    right = 0
    while not flag or right < 1:
        try:
            right = int(input('Введите правую границу диапазона, откуда будет загадано число (>= 1): '))
            flag = True
        except ValueError:
            print('Введите именно число!')
            flag = False

    return right


def input_number(n):
    flag = False
    number = 0
    while not flag or number < 1 or number > n:
        try:
            number = int(input(f'Введите число от 1 до {n}: '))
            flag = True
        except ValueError:
            print('Введите именно число!')
            flag = False
    return number


def main():
    right_border = input_right_border()
    unknown_number = random.randint(1, right_border)
    print(f'Добро пожаловать в числовую угадайку!\nЗагадано число от 1 до {right_border}, попытайтесь угадать его.')
    user_number = input_number(right_border)
    k = 1
    while user_number != unknown_number:
        if user_number < unknown_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            user_number = input_number(right_border)
        elif user_number > unknown_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            user_number = input_number(right_border)
        k += 1
    print(f'Вы угадали, поздравляем!\nЗагаданное число: {unknown_number}\nПопыток было сделано: {k}')


if __name__ == '__main__':
    main()
