import sys

input = lambda: sys.stdin.readline().rstrip()

# 아래 직접 푼거 틀렸음 DP로 정답처럼 풀어야 함


t = int(input())
result_array = []
for i in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    matrix = []
    for i in range(n):
        tmp_array = []
        for j in range(m):
            tmp_array.append(array[(i * m + j)])

        matrix.append(tmp_array)

    result = 0
    for j in range(m):
        # 여기서 안맞는 부분이 2행 차이가 나는 건 이동이 안되기 때문
        # 즉, dp로 풀었어야 함
        value = 0
        for i in range(n):
            value = max(value, matrix[i][j])

        result += value

    result_array.append(result)

print(result_array)
