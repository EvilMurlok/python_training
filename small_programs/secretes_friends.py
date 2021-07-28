"""
A program that randomly assigns each student his secret friend, who will solve programming problems with him.
Sample Input 1:
3
Светлана Зуева
Аркадий Белых
Борис Боков
Sample Output 1:
Светлана Зуева - Борис Боков
Аркадий Белых - Светлана Зуева
Борис Боков - Аркадий Белых
"""
import random


def create_dict(n):
    all_users = {}
    for i in range(n):
        all_users[i] = input()
    return all_users


def get_secret_friends(all_users):
    secret_friends, temp_list, i = {}, list(all_users.values()), 0
    while i < len(temp_list):
        index = random.choice(list(all_users.keys()))
        if temp_list[i] != all_users[index]:
            secret_friends[temp_list[i]] = all_users[index]
            all_users.pop(index)
            i += 1
    return secret_friends


def print_all_secretes(secret_friends):
    for key, val in secret_friends.items():
        print(f'{key} - {val}')


def main():
    n = int(input())
    all_users = create_dict(n)
    secret_friends = get_secret_friends(all_users)
    print_all_secretes(secret_friends)


if __name__ == '__main__':
    main()
