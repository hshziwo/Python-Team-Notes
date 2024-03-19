import copy
# 아래처럼 풀어도 되지만 비효율적이다
# 왜냐하면 dfs로 풀면 쭉쭉 타고 들어가는 것이기 때문에
# target까지 도달하지 못했다면 백트래킹해서 돌아오려면 pop을 해줘야 하는 것이고 이것은 복잡해지고 비효율
# 따라서 bfs로 미리 방문할 수 있는 곳은 방문해서 방문처리 해놓고 모두 끝났을 때의 최종값을 호출하면 정답이다.
def solution(begin, target, words):
    def dfs(words, array, path, word) :
        path.append(word)
        
        if word == target :
            array.append(copy.deepcopy(path))
            path.pop()
            return
        
        cands = []
        for tmp in words :
            count = 0
            if word == tmp :
                continue
            for i in range(len(word)) :
                if word[i] == tmp[i] :
                    count += 1
            if count == len(word) - 1 :
                cands.append(tmp)
                
        for cand in cands :
            # tmp는 visited 역할인데 백트래킹을 위해서
            tmp = copy.deepcopy(words)
            tmp.remove(cand)
            dfs(tmp, array, path, cand)

        # 여기서 pop을 꼭 cands for문 바깥에서 해줘야함
        # cands 끝난후 path pop을 해주기 위함임    
        path.pop()
        
    if target not in words :
        return 0

    path = []
    array = []
    dfs(words,array,path,begin)
    # print(min(array))
    return len(min(array)) - 1