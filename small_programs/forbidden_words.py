"""The input to the program is a line of text with the name of a text file. Write a program that displays the
contents of this file, but replacing all forbidden words with asterisks * (the number of asterisks is equal to the
number of letters in a word). Forbidden words, separated by a space character, are stored in the forbidden_words.txt
text file. """
with open('forbidden_words.txt') as file:
    f_words = {word.lower(): '*' * len(word) for word in file.read().split()}
with open(input()) as file:
    for line in file:
        lower_line = line.lower()
        for f_word in f_words:
            lower_line = lower_line.replace(f_word, f_words[f_word])
        print(*map(lambda char1, char2: char1 if char2 != '*' else char2, line, lower_line), sep='', end='')
