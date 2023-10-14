def dfs(v, graph, visited):
    visited[v] = True
    return sum([1] + [dfs(u, graph, visited) for u in graph[v] if not visited[u]])

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for v, u in wires:
        graph[v].append(u)
        graph[u].append(v)

    answer = 100
    for i in range(n-1):
        visited = [False for _ in range(n+1)]
        v1, v2 = wires[i]
        visited[v2] = True
        tmp = abs(dfs(v1, graph, visited) - dfs(v2, graph, visited))
        answer = min(tmp, answer)

    return answer