"""The input to the program is a line of text with the name of a text file in which the code is written in Python.
Write a program that displays the names of all functions for which there is no explanatory comment.
Let's assume that any line starting with the word def and a space is the beginning of a function definition.
The function contains a comment if the first character of the previous line is #.
If all functions in the file have explanatory comments, then you should output: Best Programming Team.
"""
with open('words.txt') as file:
    prev_line, bad_funcs = ' ', []
    for line in file:
        if line.startswith('def ') and prev_line[0] != '#':
            bad_funcs.append(line[line.find(' ') + 1: line.find('(')])
        prev_line = line
print('\n'.join(bad_funcs) if bad_funcs else 'Best Programming Team')
