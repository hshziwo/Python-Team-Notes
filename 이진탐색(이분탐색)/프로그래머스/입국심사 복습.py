# times의 원소들로 나눠서 합하는 방법은 최단시간을 찾는게 아니라 해당 시간동안 몇명을 처리할 수 있는지를 확인하는 것입니다.
# 시간을 정해놓고 각 원소들로 나눈 합을 구하면 당연히 해당 시간 동안 각 심사대에서 몇명을 처리할 수 있는지 합을 구할 수 있으니까요!

# 첫번째 테스트 케이스인 n = 6, times = [7, 10] 일 때 정답이 28에 대해서 보면, (28 // 7) + (28 // 10) = 4 + 2 = 6 으로 6명을 처리할 수 있습니다.

# 해당 방식으로 보면 29 또한 6명을 처리할 수 있습니다.

# 이분탐색은 처리할 수 있는 수 중에 가장 작은 값을 찾기 위한 방법입니다. 저 28이 최소가 된다는 보장을 받아야 하니까요.
# mid 값을 정해진 시간으로 보고 mid 시간 동안 n명 이상 처리할 수 있는지를 계속 확인하는 겁니다. 가능하면 좀 더 적은 시간을 줘보는 방식으로요


# 못풀어서 정답 및 아이디어 보고
# 이코테 복습해서 문제 풀었음
def binary_search(start, end, n, times):
    # start와 end가 같을 때 종료됨
    while start < end:
        mid_time = (start + end) // 2
        # 이 문제의 공식
        # (28 // 7) + (28 // 10) = 4 + 2 = 6
        count = sum([mid_time // time for time in times])

        if n <= count:
            # n과 count가 같을때도 계속 end가 start와 같아질때까지 왼쪽으로 가야함
            end = mid_time
        else:
            start = mid_time + 1

        # 0 30
        # 16 30
        # 24 30
        # 28 30
        # 28 29
        # 28 28 --> 도달 및 while문 탈출

    return start


def solution(n, times):
    start_time = 0
    end_time = int(max(times) * n)

    return binary_search(start_time, end_time, n, times)


# 아래는 깨끗한 정답
def solution(n, times):
    answer = 0
    # start, end, mid 순으로 대입 (1, times[-1] * n, 0)
    start, end, mid = 1, times[-1] * n, 0

    while start < end:
        mid = (start + end) // 2
        total = 0
        for time in times:
            total += mid // time

        if total >= n:
            end = mid
        else:
            start = mid + 1
    answer = start
    return answer
