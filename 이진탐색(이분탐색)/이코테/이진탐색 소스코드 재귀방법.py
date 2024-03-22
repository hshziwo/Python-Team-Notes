import sys

input = lambda: sys.stdin.readline().rstrip()

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))


def binary_search(array, target, start, end):
    # 시작보다 종료가 크면 에러
    if start > end:
        return None
    # 중앙값 설정
    mid = (start + end) // 2

    if array[mid] == target:
        # 값 찾았으면 종료
        return mid
    elif array[mid] > target:
        # 찾는 값이 중앙값보다 작을때
        # 시작 ~ 중앙값-1 만큼 범위로 좁힘
        return binary_search(array, target, start, mid - 1)
    else:
        # 찾는 값이 중앙값보다 클때
        # 중앙값+1 ~ end 까지로 범위 좁힘
        return binary_search(array, target, mid + 1, end)


# 이진탐색 실행
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    # index가 0부터니까 +1을 해야 몇번째 원소인지 출력(첫번째 원소입니다 등등)
    print(result + 1)
