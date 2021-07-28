"""
The input to the program is a line of text in English, in which you need to encrypt all the words.
Each word in the string should be encrypted using the Caesar cipher (cyclic shift by the length of that word).
Lowercase letters remain lowercase, while uppercase letters remain uppercase.
"""


def get_clear_word(word):
    answ = ''
    for letter in word:
        if letter.isalpha():
            answ += letter
    return answ


def make_shift(left, right, code, shift):
    if code + shift > right:
        return chr(left + code + shift - right - 1)
    else:
        return chr(code + shift)


def transform_word(word):
    shift = len(get_clear_word(word))
    final_word = ''
    left_upper, right_upper = 97, 122
    left_lower, right_lower = 65, 90
    for letter in word:
        code = ord(letter)
        if left_lower <= code <= right_lower:
            final_word += make_shift(left_lower, right_lower, code, shift)
        elif left_upper <= code <= right_upper:
            final_word += make_shift(left_upper, right_upper, code, shift)
        else:
            final_word += letter
    return final_word


words = input().split()
for i, word in enumerate(words):
    words[i] = transform_word(word)

print(*words)

