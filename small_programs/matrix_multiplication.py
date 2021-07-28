"""
Just matrix multiplication, nothing else.
"""


def get_element(a, b, i, j):
    element = 0
    for k in range(len(b)):
        element += a[i][k] * b[k][j]
    return element


def matrix_multiplication(a, b):
    temp_matrix = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            row.append(get_element(a, b, i, j))
        temp_matrix.append(row)
    return temp_matrix


def main():
    s = input().split()
    n, m = int(s[0]), int(s[1])
    a = [[int(item) for item in input().split()] for _ in range(n)]
    input()
    s = input().split()
    n, m = int(s[0]), int(s[1])
    b = [[int(item) for item in input().split()] for _ in range(n)]
    matrix = matrix_multiplication(a, b)
    for row in matrix:
        print(*row)


if __name__ == '__main__':
    main()