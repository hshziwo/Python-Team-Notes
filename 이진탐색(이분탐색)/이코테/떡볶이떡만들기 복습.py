import sys

input = lambda: sys.stdin.readline().rstrip()

#!!!!!! 절단기의 높이는 0부터 10억까지 정수이므로
# 이렇게 큰 탐색 범위를 보면 이진 탐색을 떠올려야 함!!!!!

# !!! 중요한 점!!! 이진탐색을 했을 때 값을 비교해서 다음 스텝으로 왼쪽에 둘꺼나 오른쪽에 둘꺼냐 일때
# 해당 인덱스 -1 +1 로 해도 되지만
# 문제에 따라서는 값에서 +1 -1 로 해서 조건을 만족시켜 이진탐색을 진행해도 됨
# ex) 떡볶이만들기 문제
# 여기서는 중간점을 값을 기준을 만들어야 풀이가 됨 index nono

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)


def binary_search(items, start, end):

    while start <= end:
        mid = (start + end) // 2

        sum_value = sum(map(lambda x: x - mid if x > mid else 0, items))
        if sum_value == m:
            return mid
        elif sum_value > m:
            # 칼 높이가 작다는 뜻이니까 오른쪽으로 이동 시킴
            start = mid + 1
        elif sum_value < m:
            # 칼 높이가 크다 왼쪽으로 이동 시킴
            end = mid - 1


print(binary_search(array, start, end))


# 잘못됐음!!! 이 문제는 10억범위라 순차 탐색은 하면 안됨
# 역순 방향 역순방향이 더 효율적으로 보이긴 하는 데 잘....
# items.sort(reverse=True)
# high = items[0]

# for i in range(high, items[-1] - 1, -1):
#     sum_value = sum(map(lambda x: x - i if x > i else 0, items))
#     if sum_value == m:
#         high = i
#         break

# print(high)

# 순차방향
# items.sort()
# high = items[0]

# for i in range(high, items[-1] + 1):
#     sum_value = sum(map(lambda x: x - i if x > i else 0, items))
#     if sum_value == m:
#         high = i
#         break

# print(high)
