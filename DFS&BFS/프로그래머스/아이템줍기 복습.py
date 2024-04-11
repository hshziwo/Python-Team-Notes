# 좌표, 그림을 2배로 확장시킨뒤에 문제를 푸시면 쉽게 진행이됩니다.

# 예를들어서, 예제 1번 그림에 ㄷ 자로 파인부분을 2배로 확대시켜서 풀이하셔야 움푹 파인부분을 0.5 좌표로 구분이가능합니다.

# 만약 , 확대를 안하시면, 자칫하다가 프로그램이 ㄷ자를 ㅁ자로 오해합니다.

# 먼저 사각형들 다 내부까지 1로 칠하고

# 그래프 2중 for문 돌면서 자기자신은 1이고 주위 8개중에 0이 하나라도 있다면 테두리라는 것을 표현하기 위해 2로 바꿔줌

# 2를 따라서 bfs 돌리면 끝


# 못 풀었음 정답보고 복습함
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    max_x = 0
    max_y = 0

    for x1, y1, x2, y2 in rectangle:
        max_x = max(x2 * 2, max_x)
        max_y = max(y2 * 2, max_y)

    # 그래프 초기화
    # 여기서 x는 가로, y는 세로임
    graph = [[0] * (max_x + 2) for _ in range(max_y + 2)]

    # 1로 안쪽 칠하기
    for x1, y1, x2, y2 in rectangle:
        for i in range((x1 * 2), (x2 * 2) + 1):
            for j in range((y1 * 2), (y2 * 2) + 1):
                graph[j][i] = 1

    # 전체 돌면서 주위 8개중에 하나가 0이면서 자기 자신이 1이면 2로 바꿈 테두리 경로
    for y in range(1, max_y + 1):
        for x in range(1, max_x + 1):
            for i in range(3):
                for j in range(3):
                    if graph[y + i - 1][x + j - 1] == 0 and graph[y][x] == 1:
                        graph[y][x] = 2
                        break

    # 여기선 x가 가로 y가 세로
    # 좌우상하
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 두 배의 크기로 늘려줌
    queue = deque([(characterX * 2, characterY * 2, 0)])
    itemX *= 2
    itemY *= 2

    while queue:
        x, y, length = queue.popleft()
        graph[y][x] = 1
        if x == itemX and y == itemY:
            answer = length // 2
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[ny][nx] == 2:
                queue.append((nx, ny, length + 1))

    return answer
