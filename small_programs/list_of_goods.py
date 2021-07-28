"""
A program for calculating the number of units of each type of product
from the purchased by each customer of the online store in lexicographic order,
after the name of each product - the number of units of the product.
Sample Input 1:
5
Руслан Пирог 1
Тимур Карандаш 5
Руслан Линейка 2
Тимур Тетрадь 12
Руслан Хлеб 3
Sample Output 1:
Руслан:
Линейка 2
Пирог 1
Хлеб 3
Тимур:
Карандаш 5
Тетрадь 12
"""
from collections import defaultdict


def create_dict_with_information(n):
    all_users = defaultdict(dict)
    for _ in range(n):
        name, good, count = input().split()
        all_users[name][good] = all_users[name].setdefault(good, 0) + int(count)
    return all_users


def show_list(all_users):
    for name, goods in sorted(all_users.items()):
        print(f'{name}:')
        for good, count in sorted(goods.items()):
            print(f'{good} {count}')


def main():
    n = int(input())
    all_users = create_dict_with_information(n)
    show_list(all_users)


if __name__ == '__main__':
    main()
