"""A famous game HANGMAN"""
import random


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def print_picture(pict):
    for lst1 in pict:
        for item in lst1:
            print(item, end='')
        print()


def get_right_ending(num):
    if 11 <= num % 100 <= 19 or num % 10 in (5, 6, 7, 8, 9, 0):
        return "попыток"
    elif num % 10 == 1:
        return "попытка"
    elif num % 10 in (2, 3, 4):
        return "попытки"


def get_user_letter():
    user_choice = ''
    flag = False
    while not flag or len(user_choice) != 1 or not user_choice.isalpha():
        try:
            user_choice = input('Ваша буква: ').lower().strip()
            flag = True
        except ValueError:
            print('Введите именно ОДНУ букву!')
            flag = False
    return user_choice


PICTURES = [
    [
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '  '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ']
    ],
    [
        [' ', ' ', ' ', ' '],
        [' ', ' ', '     ', ' ', ],
        [' ', ' ', '     ', ' ', ' ', ' '],
        [' ', ' ', '    ', ' ', ' ', ' '],
        [' ', ' ', '     ', ' ', ' ', ' '],
        [' ', ' ', '---    ', '', ' ', ' ']
    ],
    [
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' |    ', '  ', ],
        [' ', ' ', ' |    ', ' ', ' ', ' '],
        [' ', ' ', ' |   ', ' ', ' ', ' '],
        [' ', ' ', ' |    ', ' ', ' ', ' '],
        [' ', ' ', '---   ', '', ' ', ' ']
    ],
    [
        [' ', ' ', '--------', ' '],
        [' ', ' ', ' |    ', ' ', ],
        [' ', ' ', ' |    ', ' ', ' ', ' '],
        [' ', ' ', ' |   ', ' ', ' ', ' '],
        [' ', ' ', ' |    ', ' ', ' ', ' '],
        [' ', ' ', '---    ', ' ', ' ', ' ']
    ],
    [
        [' ', ' ', '--------', ' '],
        [' ', ' ', ' |    ', ' | ', ],
        [' ', ' ', ' |    ', ' ', ' ', ' '],
        [' ', ' ', ' |   ', ' ', ' ', ' '],
        [' ', ' ', ' |    ', ' ', ' ', ' '],
        [' ', ' ', '---    ', ' ', ' ', ' ']
    ],
    [
        [' ', ' ', '--------', ' '],
        [' ', ' ', ' |    ', ' | ', ],
        [' ', ' ', ' |    ', ' O', ' ', ' '],
        [' ', ' ', ' |   ', ' ', ' ', ' '],
        [' ', ' ', ' |    ', ' ', ' ', ' '],
        [' ', ' ', '---    ', ' ', ' ', ' ']
    ],
    [
        [' ', ' ', '--------', ' '],
        [' ', ' ', ' |    ', ' | ', ],
        [' ', ' ', ' |    ', ' O', ' ', ' '],
        [' ', ' ', ' |   ', ' -|-', ' ', ' '],
        [' ', ' ', ' |    ', ' ', ' ', ' '],
        [' ', ' ', '---    ', '', ' ', ' ']
    ],
    [
        [' ', ' ', '--------', ' '],
        [' ', ' ', ' |    ', ' | ', ],
        [' ', ' ', ' |    ', ' O', ' ', ' '],
        [' ', ' ', ' |   ', ' -|-', ' ', ' '],
        [' ', ' ', ' |    ', ' Ʌ', ' ', ' '],
        [' ', ' ', '---    ', '', ' ', ' '],
    ]
]

words = ['авиадвигатель', 'авиагарнитура', 'автогенератор', 'автобиография', 'автоинспектор', 'авиасообщение',
         'автоотключение', 'мировоззрение', 'безоговорочность', 'ограничитель', 'обесцвечение', 'лесоохранение',
         'лексикография', 'лесопогрузчик', 'лактобактерия', 'нейродистрофия', 'нейрокомпьютер', 'невозмутимость']
ATTEMPTS = 7
lives = ATTEMPTS
random.shuffle(words)
unknown_word = random.choice(words)
length_of_word = len(unknown_word)
user_attepts = ['_'] * length_of_word
user_letters = []

print(f'Добро пожаловать в игру "Виселица"! Вам будет предложено отгадать слово.\
У вас будет всего {ATTEMPTS} ' + get_right_ending(
    ATTEMPTS) + '! Если вы пытаетесь угадать слово целиком и не угадываете, вы проигрываете мгновенно!')
print('\t\t\t\t\t\t\t\t\t\t\tУДАЧИ!')

print(f'Итак, загадано слово из {length_of_word} букв.')
while True:
    print(Color.BOLD + f'Вы уже назвали следующие буквы: ' + Color.END, end='')
    print(Color.PURPLE, end='')
    print(*user_letters, end='')
    print(Color.END)
    print(Color.DARKCYAN + 'Одгадываемое слово на данный момент выглядит так: ' + Color.END, end='')
    print(*user_attepts, sep='')
    get_whole_word = input('Попытаете счастье угадать слово целиком?(да/нет) ').lower().strip()
    while get_whole_word not in ('да', 'нет'):
        print('Введите именно "да" или "нет"!!!')
        get_whole_word = input('Попытаете счастье угадать слово целиком?(да/нет) ').lower().strip()
    if get_whole_word == 'да':
        whole_word = input('Введите слово целиком! ').lower().strip()
        if whole_word == unknown_word:
            print(f'Наши поздравления! Вы угадали слово: {unknown_word.upper()}! Приходите поиграть ещё!')
        else:
            print(f'Увы, Вы проиграли! Ничего, повезет в следующий раз! Загаданное слово: {unknown_word.upper()}')
        break
    user_letter = get_user_letter()
    user_letters.append(user_letter.upper())
    if user_letter in unknown_word:
        for i, letter in enumerate(unknown_word):
            if letter == user_letter:
                user_attepts[i] = letter
        if '_' not in user_attepts:
            print(Color.GREEN + f'Наши поздравления! Вы угадали слово: {unknown_word.upper()}! '
                                f'Приходите поиграть ещё!' + Color.END)
            break
        print(f'Действительно, буква {user_letter.upper()} есть в загаданном слове!')

    else:
        lives -= 1
        if lives == 0:
            print(Color.RED + 'Вы израсходовали все попытки и Вас повесили! Повезет в следующей жизни!' + Color.END)
            print_picture(PICTURES[ATTEMPTS - lives])
            print(f'Загаданное слово было {unknown_word.upper()} :-)')
            break
        else:
            print('Упс! Вы не угадали! Рисуем виселицу:')
            print_picture(PICTURES[ATTEMPTS - lives])
