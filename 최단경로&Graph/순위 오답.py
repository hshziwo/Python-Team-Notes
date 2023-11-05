def solution(n, results):
    win_graph = [[] for _ in range(n+1)]
    lose_graph = [[] for _ in range(n+1)]
    for a,b in results :
        win_graph[a].append(b)
        lose_graph[b].append(a)
    
    answer = 0
    for i in range(1, n+1) :
        win = len(win_graph[i])
        lose = len(lose_graph[i])
        if n - 1 == win + lose :
            answer += 1
    return answer


def solution(n, results):
    table = [[0]*n for _ in range(n)]
    for a, b in results :
        i = a - 1
        j = b - 1
        table[i][j] = 1
        table[j][i] = -1
    
    # "A를 이긴 사람들은 A에게 패배한 사람들을 무조건 이긴다." 를 기억해주시면 되는데, 위의 예제에서는 5번 선수는 1,3,4에게 무조건 패배한다가 성립되겠죠? 반대로 1,3,4선수는 5번선수를 무조건 이기는게 성립이 될 것입니다.
    for i in range(n) :
        for j in range(n) :
            if table[i][j] == 1 :
                for k in range(n) :
                    if table[j][k] == 1 :
                        # i는 k를 이길 것이고
                        # k는 i에게 졌다.
                        table[i][k] = 1
                        table[k][i] = -1
    
    answer = 0
    for array in table :
        if array.count(0) == 1 :
            answer += 1
    return answer