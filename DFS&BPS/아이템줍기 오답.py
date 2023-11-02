def add_line(rectangle) :
    line = set([])
    for rect in rectangle :
        x1 = rect[0]
        y1 = rect[1]
        x2 = rect[2]
        y2 = rect[3]

        # 밑과 위 x
        for i in range(x1, x2 + 1) :
            value1 = True
            value2 = True
            value3 = False
            value4 = False
            for tmp_rect in rectangle :
                if i in (tmp_rect[0], tmp_rect[2]) and tmp_rect[1] <= y1 <= tmp_rect[3]:
                    value3 = True
                if i in (tmp_rect[0], tmp_rect[2]) and tmp_rect[1] <= y2 <= tmp_rect[3]:
                    value4 = True
                if tmp_rect[0] < i < tmp_rect[2] and tmp_rect[1] < y1 < tmp_rect[3]:
                    value1 = False
                if tmp_rect[0] < i < tmp_rect[2] and tmp_rect[1] < y2 < tmp_rect[3]:
                    value2 = False

            if value1 == True and value3 == True:
                line.add((i,y1))
            if value2 == True  and value4 == True:
                line.add((i,y2))

        # 밑과 위 y
        for i in range(y1, y2 + 1) :
            value1 = True
            value2 = True
            value3 = False
            value4 = False
            for tmp_rect in rectangle :
                if tmp_rect[0] <= x1 <= tmp_rect[2] and i in (tmp_rect[1], tmp_rect[3]) :
                    value3 = True
                if tmp_rect[0] <= x2 <= tmp_rect[2] and i in (tmp_rect[1], tmp_rect[3]) :
                    value4 = True
                if tmp_rect[0] < x1 < tmp_rect[2] and tmp_rect[1] < i < tmp_rect[3]:
                    value1 = False
                if tmp_rect[0] < x2 < tmp_rect[2] and tmp_rect[1] < i < tmp_rect[3]:
                    value2 = False

            if value1 == True and value3 == True :
                line.add((x1,i))
            if value2 == True and value4 == True:
                line.add((x2,i))

    return line

from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    line = add_line(rectangle)
    dx = [-1,1,0,0] #좌우
    dy = [0,0,-1,1] #상하
    visited = []
    for i in range(51) :
        tmp = [False for _ in range(51)]
        visited.append(tmp)
    
    queue = deque([(characterX, characterY)])
    visited[characterX][characterY] = 0
    while queue :
        x, y = queue.popleft()
        
        if x == itemX and y == itemY :
            break

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 51 or ny < 0 or ny >= 51 :
                continue

            if (nx,ny) in line and visited[nx][ny] == False:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

    return visited[itemX][itemY]