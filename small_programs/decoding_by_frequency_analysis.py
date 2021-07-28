"""Write a program to decode a secret word using frequency analysis. Example:
Sample Input 1:
*!*!*?
3
а: 3
н: 2
с: 1

Sample Output 1:
ананас
"""
from collections import Counter


def get_dict_of_symbols(encrypted_str):
    symbols_dict = {}
    for char, number in Counter(encrypted_str).most_common():
        symbols_dict[number] = char
    return symbols_dict


def word_decoding(symbols_dict, encrypted_string):
    for _ in range(int(input())):
        letter, amount = input().split(': ')
        encrypted_string = encrypted_string.replace(symbols_dict[int(amount)], letter)
    return encrypted_string


def main():
    encrypted_string = input()
    symbols_dict = get_dict_of_symbols(encrypted_string)
    decoded_string = word_decoding(symbols_dict, encrypted_string)
    print(decoded_string)


if __name__ == '__main__':
    main()
