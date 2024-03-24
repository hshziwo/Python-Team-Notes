# 플로이드 워셜 알고리즘 문제
# 시작노드 -> 중간 K 거침 -> 종료노드 문제
# (시작 ~ K까지 최단 거리 + K에서 종료노드)까지의 최단거리 로 계산하면 정답 판정
# 점화식: Distance(a,b) = min(Distance(a,b), Distance(a,k) + Distance(k,b))

INF = int(1e9)

n, m = map(int, input().split())

# 그래프 메트릭스를 만들고 모든 값을  무한으로 초기화
# 노드가 1번부터 출발한다고 가정해서 n+1크기만큼으로 만듬
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    # 여기 문제는 양방향 그래프임
    graph[a][b] = 1
    graph[b][a] = 1

# 최종목적지 x와 거쳐갈 노드 K 입력
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘을 점화식에 따라 수행해서 그래프 업데이트
# 점화식 : min(현재 최단 거리, 시작 ~ K까지 최단 거리 + K에서 종료노드)
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# (시작 ~ K까지 최단 거리 + K에서 종료노드)까지의 최단거리 로 계산하면 정답 판정
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    # 도달할수 없으면
    print(-1)
else:
    print(distance)

# 입력값
# 5 7 # 노드수, 간선수
# 1 2 # from -> to 정보
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5 # x, k
# 출력값
# 3
