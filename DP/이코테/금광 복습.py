# 여기서 중요한 문제 해결 아이디어는
# 왼쪽에서 오른쪽 위, 오른쪽 중간, 오른쪽 아래 로 간다고 생각해야 하는 게 아니라!!!!!!!
# 둘째 줄부터해서 내꺼에서 왼쪽 위, 왼쪽 중간, 왼쪽 오른쪽 에서 나한테 올 수가 있다고 생각해야 하는 게 정답 포인트고 DP해결 방법!
# 점화식 : dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
# 해석 : dp현재위치 옵티멀값은 : 현재 위치의 비용 + max(왼쪽 위, 왼쪽 중간, 왼쪽 오른쪽 중 가장 큰값)
# 그래서!!!! 마지막 정답은!! DP테이블이 다 완성되고 가장 마지막 열에서 가장 큰 값이 가장 많은 금광을 캔 옵티멀 값이다!!!!

import sys

input = lambda: sys.stdin.readline().rstrip()

results = []
for tc in range(int(input())):
    # n x m 메트릭스
    n, m = map(int, input().split())
    # 한줄로 된 원소값들
    array = list(map(int, input().split()))

    dp = []
    # 한줄로 된 원소값들을 이걸 n x m 에 맞게 값 넣어줘야함
    # 일단 원소값들을 먼저 채우고 보텀업으로 옵티멀 값을 갱신 해줄꺼임
    index = 0
    for i in range(n):
        # 행의 길이는 m이다.
        dp.append(array[index : index + m])
        # 다음 행 인덱스를 맞추기 위해 +m 해줌
        index += m

    # DP 시작
    # 보텀업 방식으로 옵티멀 값 업데이트 진행 시작
    # 1열은 갱신이 일어나지 않으므로 2열부터 시작
    for j in range(1, m):
        for i in range(n):
            # j - 1 : 왼쪽이란 뜻
            # i -1 , i, i + 1 : 왼쪽 위, 왼쪽 중간, 왼쪽 아래

            # 왼쪽 위에서 오는 경우
            if i == 0:
                # IndexError 처리
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]

            # 왼쪽 아래서 오는 경우
            if i == n - 1:
                # IndexError 처리
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]

            # 왼쪽 중간에서 오는 경우
            left = dp[i][j - 1]

            # 점화식에 따른 dp 업데이트
            # 해석 : dp현재위치 옵티멀값은 : 현재 위치의 비용 + max(왼쪽 위, 왼쪽 중간, 왼쪽 오른쪽 중 가장 큰값)
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    # 가장 마지막 열의 옵티멀 값을 출력하기 위한 변수
    result = 0
    for i in range(n):
        # 가장 마지막 열 중 가장 큰 값 출력
        result = max(result, dp[i][m - 1])
    results.append(result)

for result in results:
    print(result)

# input값
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
# output값
# 19
# 16
