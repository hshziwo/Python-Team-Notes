# 아이디어가 떠오르지 않아 정답보고 복습함
# 플로이드 워셜로 푸는 문제
def solution(n, results):
    # 0의 수로 정답 판정을 해야해서 1인덱스부터 시작하면 문제가 꼬이고
    # 0인덱스부터 방을 만들어야 계산이 편리함
    table = [[0] * n for _ in range(n)]

    # 이긴 상황은 1
    # 진 상황은 -1
    for a, b in results:
        i = a - 1
        j = b - 1
        table[i][j] = 1
        table[j][i] = -1

    # 플로이드 워셜 응용
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # "A를 이긴 사람들은 A에게 패배한 사람들을 무조건 이긴다."
                # i가 k를 이겼고 k가 이긴 경우 == 확실한 승리
                if table[i][k] == 1 and table[k][j] == 1:
                    # i는 j를 이길 것이고
                    # j는 i에게 졌다.
                    table[i][j] = 1
                    table[j][i] = -1

    count = 0
    for array in table:
        if array.count(0) == 1:
            # 자기자신만 빼고(== 0) 모든 경우가 확실한 경우 카운트 +1
            count += 1
    return count
