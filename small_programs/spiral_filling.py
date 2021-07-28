"""
Two natural numbers are fed to the program n and m.
Write a program that creates a matrix of size n × m, filling it with a "spiral".
"""


def create_matrix(n, m):
    d = {'right': 1, 'down': 0, 'left': 0, 'up': 0}
    temp_matrix = [[0] * m for _ in range(n)]
    num_filled_elem = 0
    i, j, cur_val = 0, 0, 1
    while num_filled_elem < n * m:
        temp_matrix[i][j] = cur_val
        num_filled_elem += 1
        cur_val += 1
        if d['right']:
            if j + 1 < m and temp_matrix[i][j + 1] == 0:
                j += 1
            else:
                d['right'], d['down'] = 0, 1
                i += 1
        elif d['down']:
            if i + 1 < n and temp_matrix[i + 1][j] == 0:
                i += 1
            else:
                d['down'], d['left'] = 0, 1
                j -= 1
        elif d['left']:
            if j - 1 > -1 and temp_matrix[i][j - 1] == 0:
                j -= 1
            else:
                d['left'], d['up'] = 0, 1
                i -= 1
        else:
            if i - 1 > -1 and temp_matrix[i - 1][j] == 0:
                i -= 1
            else:
                d['up'], d['right'] = 0, 1
                j += 1
    return temp_matrix


def print_matrix(temp_matrix, n, m, width=3):
    for r in range(n):
        for c in range(m):
            print(str(temp_matrix[r][c]).ljust(width), end=' ')
        print()


def main():
    s = input().split()
    n, m = int(s[0]), int(s[1])
    matrix = create_matrix(n, m)
    print_matrix(matrix, n, m)


if __name__ == '__main__':
    main()