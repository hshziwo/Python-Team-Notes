# 팁
# 완전탐색이라고 떡하니 적혀있습니다.
# 완전탐색 모든 경우를 다 따져라 이므로
# 전선을 자를 수 있는 모든 경우를 잘라보고
# 각각의 영역이 가지는 정점의 개수 차이가 가장 적을 때가 답이 됩니다.
# 자세한 풀이는 링크 두겠습니다.
# https://dev-musa.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level-2-%EC%A0%84%EB%A0%A5%EB%A7%9D-%EC%9E%90%EB%A5%B4%EA%B8%B0-BFS


def solution(n, wires):
    def dfs(set_elem, node, visited) :
        set_elem.add(node)
        connected_nodes = graph[node]
        for c_node in connected_nodes :
            if (node, c_node) in visited or (c_node, node) in visited :
                continue
            else :
                visited.add((node, c_node))

            dfs(set_elem, c_node, visited)

    cut_count_array = []
    for cut_edge in wires :
        graph = {}
        for i in range(1, n+1):
            graph[i] = set([])
        for edge in wires :
            if cut_edge == edge :
                continue
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
                
        first_set = set([])
        first_set_visited = set([])
        dfs(first_set, cut_edge[0],first_set_visited)
        second_set = set([])
        second_set_visited = set([])
        dfs(second_set, cut_edge[1],second_set_visited)
        
        cut_count_array.append(abs(len(first_set) - len(second_set)))
    return min(cut_count_array)