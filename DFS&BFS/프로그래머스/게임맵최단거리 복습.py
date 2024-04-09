# 못 풀어서 정답 보고 품
# dfs가 아니라 전형적인 queue를 이용한 BFS 문제였다!!!!
# 미로탈출과 같은 상하좌우 문제는 BFS문제!!!! deque을 이용한 queue문제!!!!! 꼭 기억!!!!!
from collections import deque


def solution(maps):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    start_n = 0
    start_m = 0
    end_n = len(maps) - 1
    end_m = len(maps[0]) - 1
    queue.append((start_n, start_m))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > end_n or ny > end_m:
                continue

            if maps[nx][ny] == 1:
                # 여기가 중요!!! 다음 순서가 가능하다면(maps[nx][ny] == 1)
                # 현재 테이블값에서 +1 시켜서 다음 테이블값을 업데이트 시켜주는게
                # BFS의 핵심이다. 정말 중요
                # 즉, 현재의 경우에서 한칸 더 갈 수 있다는 뜻이므로
                maps[nx][ny] = maps[x][y] + 1
                # 계속 BFS를 진행시키기 위해 queue에 넣어줌
                queue.append((nx, ny))
                # 이렇게 queue가 끝나면 모든 최적의 값에 대해 테이블이 갱신됨

    # 마지막으로 최종 목표 테이블값을 따지기
    if maps[end_n][end_m] < 2:
        return -1
    else:
        return maps[end_n][end_m]
