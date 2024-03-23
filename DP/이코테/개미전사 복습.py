import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
array = list(map(int, input().split()))

# dp테이블 초기화
d = [0] * 100

# 0번째는 처음값 넣어줌
d[0] = array[0]
# 1번째 꺼는 0번째값과 1번째값 중 큰 값을 넣어줌
d[1] = max(array[0], array[1])
# 0, 1번째 dp테이블은 초기값이 있으므로 건너뛰고 2번째 인덱스부터 시작
for i in range(2, n):
    # 현재 i번째 dp테이블 점화식은 이전값(d[i-1])과 한칸 전 값(d[i-2])에 현재값(array[i])를 더한 것 중 큰 것을 dp테이블에 기입
    # 이렇게 흘러가면 마지막 dp테이블에는 최적의 값이 넣어져 있을 것임
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 보텀업 끝난 마지막 값 출력하면 최적의 값
print(d[n - 1])

# 아래는 내가 푼 건데 부족해보임ㅠㅠ
# d = [0] * n

# for i in range(n):
#     tmp_d = 0
#     index = i + 2
#     if index > n - 1:
#         break
#     for j in range(index, n):
#         tmp_d = max(tmp_d, array[i] + array[j])

#     d[i] = tmp_d

# print(max(d))
