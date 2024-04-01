import heapq, sys

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)

# 노드 수 n, 간선 수 m
n, m = map(int, input().split())
# 시작노드 입력받기
start = int(input())

# 그래프 메트릭스를 표현하기 위한 이차원 배열 선언
# 시작이 1이여서 0은 안쓸려고 n + 1 까지의 배열을 만들어줌
graph = [[] for _ in range(n + 1)]
# heap을 이용한 우선순위 큐의 다익스트라는 visited 테이블이 필요없음
# visited = [False] * (n + 1)
# 최단 거리 테이블을 처음에 무한으로 초기화 선언
distance = [INF] * (n + 1)

# 그래프 데이터 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # 그래프 정보를 입력하는데
    # a 노드에서 b 노드로 가는 비용이 c라는 의미로
    # a 노드에 튜플 형태로 (b, c)를 넣어줌
    # a에서의 간선은 여러개일 수 있음
    # graph[a] = [( ),( ),( )]
    graph[a].append((b, c))


def dijkstra(start):
    q = (
        []
    )  # heap 자료형이 있는 것이 아니라 list를 heapq라이브러리를 사용하여 heap처럼 이용함
    # 큐에 시작 노드의 거리 비용인 0을 넣음 (0, start)
    heapq.heappush(q, (0, start))
    distance[start] = 0  # 시작노드 거리 0

    # q가 빌때까지 수행
    while q:
        # queue에서 하나 꺼냄
        # 우선순위 큐에서 꺼냈기 때문에 제일 작은 거리값이 제일 먼저 나옴
        # 거리, 노드이름 순서임
        dist, now = heapq.heappop(q)
        # 현재 노드의 거리가 힙에 있는 거리보다 작으면 다음 while문으로 넘어가란 얘기인데
        # 이 말은 이미 더 작은 거리 비용으로 업데이트 됐었다는 말
        # 즉, visited 테이블 없이 visited 역할을 함
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 노드들 순회하며 업데이트
        for i in graph[now]:
            next_node = i[0]
            next_cost = i[1]
            cost = dist + next_cost

            # 현재 노드를 거쳐서 다음 노드로 가는 것이 기존값보다 거리가 짧을 때 업데이트
            if cost < distance[next_node]:
                distance[next_node] = cost
                # 조건을 만족하면 거리 비용, 노드 이름 순으로 다시 우선순위 큐에 넣음
                # 중복된 노드에 대한 값이 여러개 들어가도
                # 결국 while문 상위에서 heappop이 될꺼고 이미 옵티멀이면 continue할꺼니까 queue는 종료되게 되어 있음
                heapq.heappush(q, (cost, next_node))


# 알고리즘 시작
# 함수 완료 후 distance 테이블이 모두 옵티멀 해져있을 것임
dijkstra(start)

# 요거는 시작노드에서 출발해서 모든 노드에 대해서 도착 거리 비용을 출력하는 거임
# 그냥 시작노드에서 B노드까지의 최소 거리 비용을 출력하려면 그냥 distance[b]로 하면 됨
for i in range(1, n + 1):
    # 시작노드에서 도달할 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    else:
        # 도달 할 수 있는 경우 거리 출력
        print(distance[i], end=" ")


# input값
# 6 11
# 1
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
