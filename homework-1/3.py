from math import factorial


def zeros(num: int) -> int:
    fact = str(factorial(num))[::-1]
    count_zeros = 0
    for num in fact:
        if num == '0':
            count_zeros += 1
        else:
            break
    return count_zeros


if __name__ == '__main__':
    zeros(int(input('Input int number: ')))
