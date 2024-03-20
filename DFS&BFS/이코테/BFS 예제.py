from collections import deque

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

visited = [False] * 9


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        # 큐에서 가장 먼저들어온(가장왼쪽) 원소를 먼저 뽑기
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph, 1, visited)
