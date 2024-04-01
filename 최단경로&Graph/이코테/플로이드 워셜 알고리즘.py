# 플로이드 워셜 알고리즘 문제
# 시작노드 -> 중간 K 거침 -> 종료노드 문제
# (시작 ~ K까지 최단 거리 + K에서 종료노드)까지의 최단거리 로 계산하면 정답 판정
# 점화식: Distance(a,b) = min(Distance(a,b), Distance(a,k) + Distance(k,b))

INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
# 노드가 1번부터 출발한다고 가정해서 n+1크기만큼으로 만듬
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
# 메트릭스에서 대각선은 0인거와 같음
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    # 여기서는 단방향 그래프라 가정
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
# k == 거쳐가는 노드, a == 시작 노드, b == 종료 노드
# 즉 a->b가 거리가 짧냐, a->k->b가 거리가 짧냐로 테이블 업데이트
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()

# input값
# 6
# 11
# 1 2 2
# 1 4 1
# 1 3 5
# 2 4 2
# 2 3 3
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# output값
# 0 2 3 1 2 4
# INFINITY 0 3 2 3 5
# INFINITY 3 0 5 6 5
# INFINITY 5 2 0 1 3
# INFINITY 4 1 6 0 2
# INFINITY INFINITY INFINITY INFINITY INFINITY 0
