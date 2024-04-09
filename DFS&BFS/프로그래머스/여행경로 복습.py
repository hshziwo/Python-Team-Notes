# 틀렸음
# 정답보고 복습한거
import copy


def dfs(node, graph):
    global path_list, path
    path.append(node)
    cands = graph[node]

    if not cands:
        # 더 이상 진행할 수 없을 경우
        # 현재 까지의 경로를 deepcopy로 list에 넣어줌
        path_list.append(copy.deepcopy(path))
        # 백트래킹을 위해 pop해줌
        path.pop()
        return
    else:
        for to_node in cands:
            # graph를 visited처럼 쓰기 위해
            # remove로 줄어드는 graph를 복사해서 다음 dfs로 넘김
            # 백트래킹 시 원래의 edge를 보존하기 위함
            tmp_graph = copy.deepcopy(graph)
            tmp_graph[node].remove(to_node)
            dfs(to_node, tmp_graph)

        # path를 pop으로 복구해줘야 백트래킹 제대로 돌아감
        path.pop()


def solution(tickets):
    global graph, path_list, path
    node_set = []
    for ticket in tickets:
        node_set += ticket

    graph = {}
    for node in set(node_set):
        if node not in graph:
            graph[node] = []

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    path = []
    path_list = []
    dfs("ICN", graph)

    # 방문 전체의 길이는 간선의 수 + 1 이다.
    total_length = len(tickets) + 1
    path_list = [path for path in path_list if len(path) == total_length]
    path_list.sort()
    return path_list[0]
