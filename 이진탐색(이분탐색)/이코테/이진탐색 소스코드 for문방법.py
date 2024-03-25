import sys

input = lambda: sys.stdin.readline().rstrip()

# n은 길이, target은 찾고자하는 값
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))


def binary_search(array, target, start, end):
    # 종료보다 시작이 작아야 시작됨 아니면 맨 밑에 None을 리턴
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        # 찾는 값이 중앙값보다 왼쪽에 있을때 == 작을때
        elif array[mid] > target:
            # end를 mid 왼쪽으로 당겨줌
            end = mid - 1
        else:
            # 찾는 값이 중앙값보다 클때 == 오른쪽에 있을때
            # 시작을 중앙값 오른쪽으로 당김
            start = mid + 1

    return None


# 이진탐색 실행
# start = 0, end = n - 1(마지막인덱스)
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    # index가 0부터니까 +1을 해야 몇번째 원소인지 출력(첫번째 원소입니다 등등)
    print(result + 1)
