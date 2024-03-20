import sys

input = lambda: sys.stdin.readline().rstrip()

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    # 처음 0,0 을 넣음
    queue.append((x, y))

    # 큐가 계속 있을 동안 진행
    while queue:
        x, y = queue.popleft()
        # 큐에서 빼서 상하좌우 테스트
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인경우
            if graph[nx][ny] == 0:
                continue

            # 첫 방문일경우만
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                # 값을 1 증가시키고 해당 좌표에서 bfs하기 위해 queue에 넣음
                queue.append((nx, ny))

    # queue가 빌때까지 계속 진행되었다면 마지막 끝점은 최소 길이 값이 들어가 있음
    return graph[n - 1][m - 1]


print(bfs(0, 0))


# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
