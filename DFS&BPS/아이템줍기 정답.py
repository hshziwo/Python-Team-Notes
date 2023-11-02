# x, y = (cur_x + next_x) / 2, (cur_y + next_y) / 2 << movable 한지 알아보기 위해서 next_x, next_y 만 필요한게 아니라 중간값이 필요한 이유가 있나요?
# 1칸짜리 ㄷ자모양을 돌아갈 때 자칫하면 회전구간 없이 그냥 건너가게 될 수도 있습니다. 이분은 2배율로 늘리는 대신 중간값을 체크하는걸로 문제를 해결하셨네요

"""Solution code for "Programmers 87694. 아이템 줍기".

- Problem link: https://programmers.co.kr/learn/courses/30/lessons/87694
- Solution link: http://www.teferi.net/ps/problems/programmers/87694
"""

import itertools


def is_movable(cur_x, cur_y, next_x, next_y, rectangles):
    x, y = (cur_x + next_x) / 2, (cur_y + next_y) / 2
    # 가장 자리와 똑같은지(in 에 있냐는 뜻) 확인
    is_on_any_border = any(
        (x in (x1, x2) and y1 <= y <= y2) or (y in (y1, y2) and x1 <= x <= x2)
        for x1, y1, x2, y2 in rectangles)
    # 내부에 있는 지 확인
    is_inside_any_rect = any(
        x1 < x < x2 and y1 < y < y2 for x1, y1, x2, y2 in rectangles)
    return is_on_any_border and not is_inside_any_rect


def solution(rectangle, characterX, characterY, itemX, itemY):
    cur_pos = (characterX, characterY)
    prev_pos = None
    for dist in itertools.count():
        if cur_pos == (characterX, characterY) and prev_pos:
            perimeter = dist
            break
        elif cur_pos == (itemX, itemY):
            dist_to_item = dist
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
            # *는 unpacking한 거 실제는 cur_x, cur_y, next_x, next_y 이렇게 들어감
            if next_pos != prev_pos and is_movable(*cur_pos, *next_pos,
                                                   rectangle):
                prev_pos, cur_pos = cur_pos, next_pos
                break
    return min(dist_to_item, perimeter - dist_to_item)



# 좌표, 그림을 2배로 확장시킨뒤에 문제를 푸시면 쉽게 진행이됩니다.

# 예를들어서, 예제 1번 그림에 ㄷ 자로 파인부분을 2배로 확대시켜서 풀이하셔야 움푹 파인부분을 0.5 좌표로 구분이가능합니다.

# 만약 , 확대를 안하시면, 자칫하다가 프로그램이 ㄷ자를 ㅁ자로 오해합니다.

# 먼저 사각형들 다 내부까지 1로 칠하고

# 그래프 2중 for문 돌면서 자기자신은 1이고 주위 8개중에 0이 하나라도 있다면 테두리라는 것을 표현하기 위해 2로 바꿔줌

# 2를 따라서 bfs 돌리면 끝

from collections import deque

def solution(rectangle, cx, cy, ix, iy):
    answer = 0
    maxX = 0
    maxY = 0

    for x,y,x2,y2 in rectangle:
        maxX = max(x2 * 2,maxX)
        maxY = max(y2 * 2,maxY)

    graph = [[0] * (maxX + 2) for _ in range(maxY + 2)]

    #1로 안쪽 다 칠하고
    for x,y,x2,y2 in rectangle:
        for i in range((x * 2),(x2 * 2) + 1):
            for j in range((y * 2),(y2 * 2) + 1):
                graph[j][i] = 1

    #전체 돌면서 주위 8개중에 하나가 0이면서 자기 자신이 1이면 2로 바꿈 테두리 경로
    for y in range(1,maxY + 1):
        for x in range(1,maxX + 1):
            for i in range(3):
                for j in range(3):
                    if graph[y + i - 1][x + j - 1] == 0 and graph[y][x] == 1:
                        graph[y][x] = 2
                        break

    dx = [1,0, 0, -1]
    dy = [0,1, -1, 0]
    queue = deque([(cx * 2,cy * 2,0)])
    ix *= 2
    iy *= 2
    while queue:
        x, y,length = queue.popleft()
        graph[y][x] = 1
        if x == ix and y == iy:
            answer = (length // 2)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[ny][nx] == 2:
                queue.append((nx,ny,length + 1))


    return answer