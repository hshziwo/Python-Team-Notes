dp_table = [0] * 100

# 가장 밑에 값인 1번째, 2번째 값을 미리 넣어줌
dp_table[1] = 1
dp_table[2] = 1

n = 99
# 3번째부터 출발해서 99까지 수행
for i in range(3, n + 1):
    # for문 돌면서 계속 점화식 수행하면 dp테이블에 값 기입
    dp_table[i] = dp_table[i - 1] + dp_table[i - 2]

# 모든 게 끝나면 99번째 값을 dp테이블에서 꺼내서 출력
print(dp_table[n])
