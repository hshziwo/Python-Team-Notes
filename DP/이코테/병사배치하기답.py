n = int(input())
array = list(map(int, input().split()))
# 본 문제는 가장 긴 감소하는 부분 수열을 찾는 문제
# 따라서 LIS 알고리즘을 조금 바꿔서 적용해야함 reverse
# 현재 문제는 감소하는 인데 이것을 최장 증가 부분수열로 바꾸기 위해 reverse
array.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
