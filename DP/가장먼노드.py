from collections import deque
def solution(n, edge):
    def bfs(start) :
        count = 0
        queue = deque()
        queue.append((start,count))
        while queue :
            node, count = queue.popleft()
            if visited[node] == True:
                continue
            else :
                visited[node] = True
            count += 1
            nodes[node] = count
            next_nodes = graph[node]
            for next_node in next_nodes :
                if visited[next_node] == False :
                    queue.append((next_node, count))
        
    graph = [[] for _ in range(n+1)]
    for a, b in edge :
        graph[a].append(b)
        graph[b].append(a)
    nodes = [0]*(n+1)
    visited = [False]*(n+1)
    bfs(1)
    answer = nodes.count(max(nodes))
    return answer