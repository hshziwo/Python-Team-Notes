import sys

input = lambda: sys.stdin.readline().rstrip()

x = int(input())

# 점화식 : a = min(조건) + 1
# 여기서 +1은 count +=1 처럼 계속 카운팅이 되는 역할
# x의 최대범위인 30000개까지의 값에 대한 dp값을 구하기 위해 30001개의 array를 만듬
# 근데 x + 1 까지만 만들어도 되지 않나??
# d = [0] * 30001
d = [0] * (x + 1)

# x = 1 일때는 for문을 수행할 필요가 없으므로 dp값은 0임 따라서 i=2 부터 보텀업 시작
# x값까지 dp테이블이 만들어져야 하므로 끝 범위를 x + 1로 설정
for i in range(2, x + 1):
    # 여기서 계속 +1이 붙는 거는 한번 돌면 카운트가 올라가기 떄문에 count +=1 해주는 거임

    # 일단 -1 뺀값을 현재 dp값에 저장
    d[i] = d[i - 1] + 1
    # -1을 뺀 카운트보다 2로 나눴을 때의 카운트가 더 작으면 그 값을 현재 dp테이블에 넣어줌
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 3으로 나눠 질때 위에서 벌어졌던(-1빼기 or 2로 나누기) 카운트 보다 3으로 나눴을 때 count가 작으면 dp에 넣어줌
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 5로 나눠 질때 위에서 벌어졌던(-1빼기 or 2 or 3으로 나누기) 카운트 보다 5로 나눴을 때 count가 작으면 dp에 넣어줌
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

    # 이 작업들이 x+1까지 진행되면 x범위에 해당하는 최적의 count값이 dp테이블에 만들어지고 출력은 x에 해당하는 dp테이블 값을 출력하면 된다

print(d[x])
