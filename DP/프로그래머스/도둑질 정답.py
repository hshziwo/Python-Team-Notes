# 근데 n이 1000000 이하....
# 이코테의 DP문제 중 개미전사와 동일해보이지만
# 원형 탐색의 함정을 생각해야 한다!!!
# https://school.programmers.co.kr/questions/31576


# 정답ㅠㅠ
# 원형 탐색으로써 아예 dp테이블을 2가지의 경우로 따로 생각해야 함
def solution(money):
    # 기본형이나 마지막 인덱스까지 도달하지 않는 경우
    dp1 = [0] * len(money)
    dp1[0], dp1[1] = money[0], max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 1인덱스부터 시작해서 끝까지 가는 경우
    dp2 = [0] * len(money)
    dp2[0], dp2[1] = 0, money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    # dp의 마지막 인덱스(-1)가 이 원형 탐색의 경우에는 옵티멀값이 아닐 수도 있기 때문에
    # 각 dp의 최대값을 구해서 비교해줘야 함
    return max(max(dp1), max(dp2))


# 위 주소의 해설을 보고 풀었는데도 틀렸다.....ㅠㅠ
def execute_dp(array):
    dp = [0] * len(array)
    dp[0] = array[0]
    dp[1] = max(dp[0], array[1])
    # 계속 len(money) + 1까지 range를 잡으려는데 실수하면 안됨
    # 여기서는 0인덱스부터 출발했기 때문에 len(money)까지 해서 n-1 인덱스까지 따지면 됨
    for i in range(2, len(array)):
        dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

    return dp


def solution(money):
    # 여기서 원형 탐색의 함정 주의!!!
    # 두가지의 배열로 생각해야함
    # 둘 모두 길이는 같아야 하나
    # 첫번째 배열은 마지막 인덱스가 빠진 경우를 생각하고
    # 두번째 배열은 1인덱스부터 시작하는 경우를 생각
    # 원형 탐색에서는 마지막 종점은 빼야하기 때문임
    # 위의 주소의 해설을 꼭 참고
    money1 = [0] + money[: len(money)]
    money2 = [0] + money[1:]
    dp1 = execute_dp(money1)
    dp2 = execute_dp(money2)

    return max(dp1[-1], dp2[-1])
