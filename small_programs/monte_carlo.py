"""Train Monte-Carlo method with random area"""
import random

n, k, s0 = 10 ** 6, 0, 16
for _ in range(n):
    x = random.uniform(-2, 2)  # случайное число с плавающей точкой от -2 до 2
    y = random.uniform(-2, 2)  # случайное число с плавающей точкой от -2 до 2
    if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:  # если попадает в нужную область
        k += 1

print((k / n) * s0)
