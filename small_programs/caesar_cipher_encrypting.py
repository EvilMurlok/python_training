"""
This program can help you to encrypt the text using Caesar cipher
"""


def make_shift(left, right, code, shift):
    if code + shift > right:
        return chr(left + code + shift - right - 1)
    else:
        return chr(code + shift)


def encrypt_an_sentence(sentense, shift, lang='en'):
    left_upper, right_upper = 97, 122 if lang == 'en' else (1040, 1071)
    left_lower, right_lower = 65, 90 if lang == 'en' else (1072, 1103)
    final_word = ''
    for letter in sentense:
        code = ord(letter)
        if left_lower <= code <= right_lower:
            final_word += make_shift(left_lower, right_lower, code, shift)
        elif left_upper <= code <= right_upper:
            final_word += make_shift(left_upper, right_upper, code, shift)
        else:
            final_word += letter
    return final_word


def main():
    shift = int(input('Введите сдвиг(> 0): '))
    while shift <= 0:
        shift = int(input('Введите сдвиг(> 0): '))
    s = input('Введите предложение: ')
    language = input('Введите язык предложения: "ru" - русский, "en" - английский')
    while language.lower() != 'ru' and language.lower() != 'en':
        language = input('Введите язык предложения: "ru" - русский, "en" - английский')
    encrypted_sentence = encrypt_an_sentence(s, shift, language)
    print(encrypted_sentence)


if __name__ == '__main__':
    main()
