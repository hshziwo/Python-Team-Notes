n, m = map(int, input().split())
array = []
for i in range(n) :
    array.append(int(input()))

# 10001은 여기서 임의INF값
# 인덱스는 0부터여서 m+1 공간까지
d = [10001] * (m+1)

d[0] = 0
# i = 동전마다
for i in range(n) :
    # 전체 m원까지 최소동전 갯수를 갱신
    for j in range(array[i], m+1) :
        if d[j - array[i]] != 10001 :
            # 여기서 +1인 것은 동전을 하나 추가함으로 완성된다는 뜻
            # 7 = 2 + 5
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001 :
    print(-1)
else :
    print(d[m])