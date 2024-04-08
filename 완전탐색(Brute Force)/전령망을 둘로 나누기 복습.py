# 못 풀었음
# 그냥 정답보고 다시 해석해서 푼거
def dfs(visited, node, graph, connect_count):
    if not graph[node]:
        return connect_count

    visited[node] = True
    connect_count += 1

    for to_node in graph[node]:
        if not visited[to_node]:
            connect_count = max(
                connect_count, dfs(visited, to_node, graph, connect_count)
            )

    return connect_count


def solution(n, wires):
    answer = 1e9
    graph = [[] for _ in range(n + 1)]
    for wire in wires:
        graph[wire[0]].append(wire[1])
        # 양방향 그래프 연결이 문제에서 중요
        graph[wire[1]].append(wire[0])

    for edge in wires:
        visited = [False] * (n + 1)
        # 첫번째 간선의 to노드를 미리 방문처리 시키므로써 연결이 끊어진 역할을 해줌.
        visited[edge[1]] = True
        # 왼쪽 연결수
        # 양방향 그래프이기 때문에 끊어진 간선의 왼쪽 노드로부터 찾아냄
        left_count = dfs(visited, edge[0], graph, 0)
        # 오른쪽 연결수
        # 양방향 그래프이기 때문에 끊어진 간선의 오른쪽 노드로부터 찾아냄
        right_count = dfs(visited, edge[1], graph, 0)

        # 양쪽이 제일 균등한 차
        answer = min(answer, abs(left_count - right_count))

    return answer
