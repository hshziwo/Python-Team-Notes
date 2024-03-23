def solution(n, results):
    table = [[0]*n for _ in range(n)]
    for a, b in results :
        i = a - 1
        j = b - 1
        table[i][j] = 1
        table[j][i] = -1
    
    # "A를 이긴 사람들은 A에게 패배한 사람들을 무조건 이긴다." 를 기억해주시면 되는데, 위의 예제에서는 5번 선수는 1,3,4에게 무조건 패배한다가 성립되겠죠? 반대로 1,3,4선수는 5번선수를 무조건 이기는게 성립이 될 것입니다.
    # 3중 for문 k,i,j를 지켜야 하는 이유가 뭔가요?? i,j,k로 하면 틀리네요.
    # i->k->j 에서 i->j의 새로운 엣지를 생성하면,
    # i와 j 를 참조하는 다른 정점들을 다시 검사해야 합니다.
    # 하지만 i나 j가 제일 제일 바깥쪽 for에 위치하게 되면, 지나간 i나 j 를 다시 검사할 수 없습니다.
    # 따라서 for의 순서는 k, i, j, 혹은 k, j, i 순서가 되어야 합니다.
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                # 플로이드 워셜 유사
                if table[i][k] == 1 and table[k][j] == 1:
                        # i는 j를 이길 것이고
                        # j는 i에게 졌다.
                        table[i][j] = 1
                        table[j][i] = -1
    
    answer = 0
    for array in table :
        if array.count(0) == 1 :
            answer += 1
    return answer