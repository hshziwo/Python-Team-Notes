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
        
        # for node in graph[start] :
        #     cands.append(node)
            
        if not cands :
            answer.append(copy.deepcopy(path))
            return
        else :
            for cand in cands :
                # 틀린 접근 if graph[cand]
                # 생각해보면 다음 그래프가 있든 말든 상관없음 재귀 dfs에서 cands 따질꺼기 때문에
                # if graph[cand] :
                #     if cand in graph[start] :
                #         graph[start].remove(cand)
                #     dfs(graph, cand, answer, path)
                # 아래가 맞는 접근
                graph[start].remove(cand)
                dfs(graph, cand, answer, path)
                    
    def dfs_recursive(graph, start) :
        path = []
        answer = []
        dfs(graph, start, answer, path)
        
        return answer
    
    array = dfs_recursive(graph, "ICN")
    print(array)
    return array