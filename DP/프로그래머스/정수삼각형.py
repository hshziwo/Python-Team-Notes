def solution(triangle):
    # 참고로 [0,0,0,0,0] 으로 초기화해서 만들려면
    # dp = [0] * 5 로 하면 됨
    # 아래는 2차원 배열이라 저렇게 처리
    dp = [[0]*len(triangle[i]) for i in range(len(triangle))]
    dp[0] = triangle[0]
    
    for i in range(1, len(triangle)) :
        for j in range(len(triangle[i])) :
            left = j - 1
            left_value = 0
            right = j
            right_value = 0
            # 상위 left가 있는 index면 dp 테이블에서 찾음
            # 상위 left가 없으면 0
            if left >= 0 :
                left_value = dp[i-1][left]
            # 상위 right가 있는 index면 dp 테이블에서 찾음
            # 상위 right가 없으면 0
            if right < len(triangle[i-1]) :
                right_value = dp[i-1][right]
                
            cur_value = triangle[i][j]
            # 상위 들을 더한 것중 큰 것을 현재 dp테이블에 저장
            dp[i][j] = max(cur_value+left_value, cur_value+right_value)
    
    # 마지막 줄에서 가장 큰 수를 리턴
    answer = max(dp[len(dp) - 1])
    return answer
    