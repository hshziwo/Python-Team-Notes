import copy
def solution(tickets):
    graph = {}
    for edge in tickets :
        a, b = edge
        if a not in graph :
            graph[a] = []
        if b not in graph :
            graph[b] = []
        graph[a].append(b)
        
    def dfs(graph, start, answer, path) :
        path.append(start)
        cands = graph[start]
            
        if not cands :
            answer.append(copy.deepcopy(path))
            # path를 pop으로 복구해줘야 백트래킹 제대로 돌아감
            path.pop()
            return
        else :
            for cand in cands :
                # graph를 visited처럼 쓰기 위해 복사해서 넘김
                # 백트래킹 시 원래의 edge를 보존하기 위함
                tmp = copy.deepcopy(graph)
                tmp[start].remove(cand)
                dfs(tmp, cand, answer, path)
            # path를 pop으로 복구해줘야 백트래킹 제대로 돌아감
            path.pop()
                    
    def dfs_recursive(graph, start) :
        path = []
        answer = []
        dfs(graph, start, answer, path)
        
        return answer
    
    array = dfs_recursive(graph, "ICN")
    array = [path for path in array if len(path) == len(tickets)+1]
    array.sort()
    return array[0]