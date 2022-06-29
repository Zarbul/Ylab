from math import factorial


def zeros(num: int) -> int:
    count_zeros = 0
    while num > 0:
        num //= 5
        count_zeros += num
    return count_zeros


if __name__ == '__main__':
    zeros(int(input('Input int number: ')))
