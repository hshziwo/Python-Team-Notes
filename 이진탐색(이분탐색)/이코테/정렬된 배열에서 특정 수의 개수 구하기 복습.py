import sys

input = lambda: sys.stdin.readline().rstrip()
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))


def find_value_count(array, x):
    left_index = bisect_left(array, x)
    right_index = bisect_right(array, x)

    return right_index - left_index


print(find_value_count(array, x))
