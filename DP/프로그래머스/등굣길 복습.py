# 못 풀어서 정답 보고 복습함.
def solution(m, n, puddles):
    # 여기서 m이 column, n이 row임
    # dp 테이블 (1,1) 부터 시작 위해 (n + 1) * (m+1) 메트릭스로 초기화
    # 여기서 중요한 게 길이 있으면 1 웅덩이면 0으로 세팅하는 이유는
    # dp테이블 값의 누적으로 최단거리 값을 구할 것이기 때문이다. 아래 로직에서 중요
    dp = [[1] * (m + 1) for _ in range(n + 1)]

    # 웅덩이 dp 테이블에서 0으로 만들기
    # puddles의 값 순서가 column, row임
    for x in puddles:
        column, row = x
        dp[row][column] = 0

    # (1,1) 부터 시작
    # target은 (len(dp) - 1, len(dp[0]) - 1) 까지
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            # 처음 (1,1)은 1으로 세팅
            if i == 1 and j == 1:
                dp[i][j] = 1
                continue

            # 웅덩이이면 넘어감
            if dp[i][j] == 0:
                continue

            # 현재 좌표를 기준으로 왼쪽과 위쪽에서 오는 경우만 따지면 됨
            # (1,1)인 경우는 넘어갔으므로 index out of range는 피함
            left = j - 1
            left_value = 0
            if left >= 1:
                # 현재 row의 left까지의 dp 누적값
                # 왼쪽좌표가 1 이상일때만 가능
                # 1 이하면 경계 넘어감
                left_value = dp[i][left]

            up = i - 1
            up_value = 0
            if up >= 1:
                # 현재 좌표의 윗행(up)까지의 dp누적값
                # 위쪽좌표가 1 이상일때만 가능
                # 1 이하면 경계 넘어감
                up_value = dp[up][j]

            # 지금까지의 경우의 수는 현재 좌표를 기준으로
            # 왼쪽에서 올 수 있는 경우 + 위쪽에서 올 수 있는 경우이다.
            # 문제의 조건이 좌표는 오른쪽과 아래로만 갈 수 있다고 했기 때문
            # 현재 좌표 dp 누적값을 왼쪽 dp 누적값 + 위쪽 dp 누적값으로 갱신해준다.
            dp[i][j] = left_value + up_value

    # 목표 좌표의 dp값을 리턴하면 정답
    return dp[n][m] % 1000000007
