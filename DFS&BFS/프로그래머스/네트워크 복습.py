def dfs(index, computers):
    global visited

    visited[index] = True
    connect = computers[index]
    for i in range(len(connect)):
        # 방문한 노드이거나 자기자신일때는 넘기는 게 중요 포인트
        if visited[i] or i == index:
            continue

        # 연결된 노드이면 계속 dfs 수행
        if connect[i] == 1:
            dfs(i, computers)


def solution(n, computers):
    global visited
    visited = [False] * n
    answer = 0
    while False in visited:
        # 남아있는 방문하지 않은 노드를 추출
        tmp_visited = [i for i in range(len(visited)) if visited[i] == False]
        # 방문하지 않은 노드부터 dfs 수행
        dfs(tmp_visited[0], computers)
        # dfs가 한번 돌면 1개의 네트워크가 완성되었다는 애기
        answer += 1
    return answer
