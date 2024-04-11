# dfs가 아니라 bfs로 풀어야 함!!!

from collections import deque


def solution(n, edge):
    # 1부터 n까지 노드 선언
    graph = [[] for _ in range(n + 1)]
    # 방문 처리용
    visited = [False] * (n + 1)
    # 비용 계산용
    values = [0] * (n + 1)
    # 양방향으로 edge 정보 입력
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # bfs로 풀기 위해 queue 선언
    queue = deque()
    # 1번부터 시작하므로 1번에 대한 정보 입력
    queue.append(1)
    values[1] = 1
    visited[1] = True

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                # 다음 노드가 방문하지 않은 노드 일때
                # 방문처리 및 현재 노드거리 + 1 값을 다음 노드에 세팅하고
                # queue에 넣음
                visited[next_node] = True
                values[next_node] = values[node] + 1
                queue.append(next_node)
                # 방문된 노드들은 큐에 들어가지 않기 때문에 모두 수행 후 종료됨

    # 가장 거리가 먼 노드들의 수를 리턴하면 정답
    return values.count(max(values))
