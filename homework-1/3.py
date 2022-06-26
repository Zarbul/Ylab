from math import factorial


def zeros(num: int) -> int:
    fact = factorial(num)

    count_zeros = 0
    while fact % 10 == 0:
        fact //= 10
        count_zeros += 1
    return count_zeros


if __name__ == '__main__':
    zeros(int(input('Input int number: ')))
