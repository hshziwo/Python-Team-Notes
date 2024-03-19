from collections import deque
def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0] #상하
    dy = [0,0,-1,1] # 좌우
    n = len(maps)
    m = len(maps[0])
    
    def bfs(x, y) :
        queue = deque()
        queue.append((x, y))
        
        while queue :
            x, y = queue.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m :
                    continue
                    
                value = maps[nx][ny]
                if value == 0 :
                    continue
                
                if value == 1 :
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
                    
    bfs(0,0)
    answer = maps[n-1][m-1]
    if answer == 1 :
        return -1
                
    return answer