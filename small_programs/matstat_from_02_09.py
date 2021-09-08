"""Задания 19.49-19.54 из сборника по матстату Ефимов"""


def get_data():
    frequency = tuple(map(int, input("Введите частоты через пробел: ").split()))
    data = []
    for i, freq in enumerate(frequency):
        left_border, right_border = map(int, input(f"Введите границы {i + 1}-го интервала через пробел: ").split())
        data.append((left_border, right_border))
    return frequency, data


def get_max_freq_interval(freq, data):
    return data[freq.index(max(freq))]


def get_new_sample(b, sample_mode, data):
    return [(sum(item) / 2 - sample_mode) / b for item in data]


def get_product(freq, new_sample, power):
    return [n_i * u_i ** power for n_i, u_i in zip(freq, new_sample)]


def get_mean(sum_first_pow, n, b, d):
    return b * (sum_first_pow / n) + d


def get_u_dispersion(sum_first_pow, sum_second_pow, n):
    return (sum_second_pow - (sum_first_pow ** 2 / n)) / n


def get_x_dispersion(sum_first_pow, sum_second_pow, n, b):
    return get_u_dispersion(sum_first_pow, sum_second_pow, n) * b * b


def get_asymmetry_coefficient(u_dispersion, sum_first_pow, sum_second_pow, sum_third_pow, n):
    temp = (sum_third_pow / n) - 3 * (sum_second_pow / n) * (sum_first_pow / n) + 2 * ((sum_first_pow / n) ** 3)
    return temp * (1 / (u_dispersion ** 1.5))


def get_kurtosis_coefficient(u_dispersion, sum_first_pow, sum_second_pow, sum_third_pow, sum_fourth_pow, n):
    temp = (sum_fourth_pow / n) - 4 * (sum_third_pow / n) * (sum_first_pow / n) + 6 * (sum_second_pow / n) * \
           ((sum_first_pow / n) ** 2) - 3 * ((sum_first_pow / n) ** 4)
    return temp * (1 / u_dispersion ** 2) - 3


def main():
    frequency, data = get_data()
    # frequency = [1, 4, 5, 8, 14, 9, 6, 1, 1, 1]
    # data = [(61, 65), (65, 69), (69, 73), (73, 77), (77, 81), (81, 85), (85, 89), (89, 93), (93, 97), (97, 101)]
    n = sum(frequency)
    b = data[0][1] - data[0][0]
    d = (get_max_freq_interval(frequency, data)[1] + get_max_freq_interval(frequency, data)[0]) / 2
    new_sample = get_new_sample(b, d, data)
    # print(f"Новая выборка: {new_sample}")
    first_pow, second_pow = get_product(frequency, new_sample, 1), get_product(frequency, new_sample, 2)
    third_pow, fourth_pow = get_product(frequency, new_sample, 3), get_product(frequency, new_sample, 4)
    sum_first_pow, sum_second_pow, = sum(first_pow), sum(second_pow)
    sum_third_pow, sum_fourth_pow = sum(third_pow), sum(fourth_pow)
    # print(sum_first_pow / n, sum_second_pow / n, sum_third_pow / n, sum_fourth_pow / n)
    answer_mean = get_mean(sum_first_pow, n, b, d)
    answer_u_dispersion = get_u_dispersion(sum_first_pow, sum_second_pow, n)
    answer_x_dispersion = get_x_dispersion(sum_first_pow, sum_second_pow, n, b)
    answer_asymmetry_coefficient = get_asymmetry_coefficient(answer_u_dispersion, sum_first_pow, sum_second_pow,
                                                             sum_third_pow, n)
    answer_kurtosis_coefficient = get_kurtosis_coefficient(answer_u_dispersion, sum_first_pow, sum_second_pow,
                                                           sum_third_pow, sum_fourth_pow, n)
    print(f"OH, MY GOD, WE've done it!\nMean: {answer_mean}, u_dispersion: {answer_u_dispersion}, "
          f"x_dispersion: {answer_x_dispersion},\nasymmetry_coefficient: {answer_asymmetry_coefficient}, "
          f"kurtosis_coefficient: {answer_kurtosis_coefficient}")


if __name__ == '__main__':
    main()
