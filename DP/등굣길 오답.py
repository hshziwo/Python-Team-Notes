def solution(m, n, puddles):
    def dfs(i, j) :
        nonlocal answer
        if dp[i][j] == 0 :
            return
        if i == n - 1 and j == m - 1 :
            answer += 1
            return
        
        down_i = i + 1
        if down_i < n :
            dfs(down_i, j)
        right_j = j + 1
        if right_j < m :
            dfs(i, right_j)
        
    dp = [[1]*m for _ in range(n)]
    for x in puddles :
        a, b = x
        dp[b-1][a-1] = 0

    answer = 0
    dfs(0,0)
    return answer % 1000000007


# 참고 : 여기서 m은 row수가 아니라 가로의 길이이므로 열의 수와 같아 column이고,
# n은 세로의 길이이므로 행의 수와 같아 row임
# 따라서 n * m 행렬임, array[n][m]
def solution(m, n, puddles):
    dp = [[1]*m for _ in range(n)]
    for x in puddles :
        column,row = x
        dp[row][column] = 0
        
    for i in range(len(dp)) :
        for j in range(len(dp[0])) :
            if i ==0 and j == 0 :
                dp[i][j] = 1
                continue
            if dp[i][j] == 0 :
                continue
                
            left = j - 1
            left_value = 0
            up = i - 1
            up_value = 0
            if left >= 0 :
                left_value = dp[i][left]
            if up >= 0 :
                up_value = dp[up][j]
            dp[i][j] = left_value + up_value
    
    
    answer = dp[n-1][m-1] % 1000000007
    return answer