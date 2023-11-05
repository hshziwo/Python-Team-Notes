from itertools import combinations
def solution(distance, rocks, n):
    rocks.sort()
    combi = combinations(rocks, len(rocks) - n)
    array = []
    for x in combi :
        inner = [0]
        for y in x :
            inner.append(y)
        inner.append(distance)
        array.append(inner)

    value = 0
    for inner in array :
        min_value = 9999
        for i in range(1, len(inner)) :
            tmp = inner[i] - inner[i-1]
            min_value = min(min_value, tmp)
        value = max(value, min_value)         

    return value