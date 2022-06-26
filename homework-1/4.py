import itertools


def bananas(s) -> set:
    result = set()
    for comb in itertools.combinations(range(len(s)), len(s) - len('banana')):
        arr = list(s)
        for i in comb:
            arr[i] = '-'
        intermediate_result = ''.join(arr)
        if intermediate_result.replace('-', '') == 'banana':
            result.add(intermediate_result)
    print(result)
    return result


if __name__ == '__main__':
    bananas('bbananana')
