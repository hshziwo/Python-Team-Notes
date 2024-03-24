import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)

# 노드의 개수, 간선의 개수, 시작 노드를 입력받기
n, m, start = map(int, input().split())
# 그래프를 나타내기 위한 메트릭스 선언
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 먼저 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    # X번 노드에서 Y번 노드로 가는 비용이 Z라는 의미
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여 큐에 삽입
    # (비용, 노드)
    heapq.heappush(q, (0, start))
    # 최단 거리 테이블에 비용 추가
    distance[start] = 0

    # 큐가 빌때까지
    while q:
        # 우선순위 큐에 들어있는 비용이 제일 작은 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 최단 거리 테이블에 있는 노드의 비용이 더 싸면 업데이트 하지 않고 다음 for문으로 넘어감
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 노드들 확인
        for i in graph[now]:
            # 연결된 노드의 비용을 더해봄
            cost = dist + i[1]
            # 더한 비용이 i노드의 최단거리 테이블의 비용보다 작으면 최단거리 테이블 업데이트
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 최단 거리 테이블을 업데이트하고
                # 그 인접 노드를 계산된 비용과 함께 우선 순위 큐에 담는다
                # 그리고 계속 while문 진행
                # BFS와는 다른 점이 heap이기 떄문에 우선순위대로 정렬이 되어서 스택이나 큐처럼 넣는대로 순서가 되는 것이 아니다.
                # 즉 heappush할때 마다 비용이 적은 순으로 정렬이 계속 이루어짐
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# 여기서는 전보의 문제에 대한 답
count = 0  # 도달할 수 있는 노드 수
max_distance = 0  # 가장 멀리있는 최단 거리 비용
for d in distance:
    if d != INF:
        # 도달할 수 있는 경우에 카운트를 하나 세고
        count += 1
        # 도달할 수 있는 노드 중 계산된 최단거리 테이블 값 중에 최단 거리 비용이 가장 큰 값을 기록
        max_distance = max(max_distance, d)

# 시작노드는 제외해야 하므로 count - 1
print(count - 1, max_distance)


# 여기서 주의할 점은 만약에 문제가 시작 노드에서 어떤 특정 노드까지의 최단 거리를 묻는 문제라면
# print(distance[특정노드]) 이렇게 한다면 정답이 될 수 있을 거 같다.

# 입력값
# 3 2 1
# 1 2 4
# 1 3 2
# 출력값
# 2 4
