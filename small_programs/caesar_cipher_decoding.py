"""
This program can help you to decode the text using Caesar cipher
"""


def make_shift_decode(left, right, code, shift):
    if code - shift < left:
        return chr(right - (left - 1 - (code - shift)))
    else:
        return chr(code - shift)


def encrypt_an_sentence(sentense, shift, lang='en'):
    left_upper, right_upper = 97, 122 if lang == 'en' else (1040, 1071)
    left_lower, right_lower = 65, 90 if lang == 'en' else (1072, 1103)
    final_word = ''
    for letter in sentense:
        code = ord(letter)
        if left_lower <= code <= right_lower:
            final_word += make_shift_decode(left_lower, right_lower, code, shift)
        elif left_upper <= code <= right_upper:
            final_word += make_shift_decode(left_upper, right_upper, code, shift)
        else:
            final_word += letter
    return final_word


def full_decoding(sentence, lang):
    amount_letters = {'en': 26, 'ru': 33}
    return [encrypt_an_sentence(sentence, i, lang) for i in range(1, amount_letters.get(lang, 26))]


def main():
    shift = int(input('Введите сдвиг(> 0): '))
    while shift <= 0:
        shift = int(input('Введите сдвиг(> 0): '))
    s = input('Введите предложение для расшифровки: ')
    language = input('Введите язык предложения: "ru" - русский, "en" - английский ')
    while language.lower() != 'ru' and language.lower() != 'en':
        language = input('Введите язык предложения: "ru" - русский, "en" - английский ')
    encrypted_sentence = encrypt_an_sentence(s, shift, language)
    print(encrypted_sentence)


if __name__ == '__main__':
    main()
"""
s = input('Введите предложение для расшифровки: ')
    language = input('Введите язык предложения: "ru" - русский, "en" - английский ')
    while language.lower() != 'ru' and language.lower() != 'en':
        language = input('Введите язык предложения: "ru" - русский, "en" - английский ')
    print(*full_decoding(s, language), sep='\n')
"""