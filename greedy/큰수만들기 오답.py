import itertools
def solution(number, k):
    array = [x for x in number]
    combi = itertools.combinations(array, len(number) - k)
    value_array = [int(''.join(x)) for x in list(combi)]
    return str(max(value_array))