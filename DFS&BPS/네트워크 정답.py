# union하고 find의 역할을 잘 알아두어야 합니다.

# union은 단순히 자신의 부모 노드를 찾아서, 부모노드를 합쳐주는 작업을 수행하고,
# find는 자신이 현재 연결된 부모 노드를 찾아주는 역할을 수행합니다.

# 여기서 오해하면 안되는 부분이, union을 수행한다고하서, 항상 모든 parent에는 항상 가장작은 부모노드가 저장된다고 하는 부분입니다.

# union함수의 내부에는, find()함수를 a와 b를 각각 수행해서,
# 이 경우에는 전부 노드가 갱신되지만,

# 실제로 aP와 bP에 값을 새로 할당하게 되는 순간,
# parent의 값이 항상 해당 노드의 부모라는 확신이 없어집니다.
# 더 큰 부모에 작은 부모가 할당되었으니, 작은 노드쪽으로 union은 수행된 것은 맞으나,
# find()한 번 더 수행하지 않는다면, 최상단 노드만 갱신 되었기에,
# 하위 노드들 아직도, union을 수행하기 전의 노드가 최상단 부모 노드라고 기억하게 됩니다.

# 이를 위한 반례입니다.

# 5, [[1, 0, 0, 0, 1], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1]] => 1

# 꼭 한 번 직접 그림으로 그려보시고,
# find()를 마지막에 수행하지 않을 경우,
# 왜 parent의 값이 최상단 부모노드 값이 아닌지 확인해볼 수 있을겁니다.

# 이를 통해, union find 알고리즘을 완벽히 이해하실 수 있는
# 좋은 경험이 되지 않을까 싶습니다.

# 감사합니다.

def solution(n, computers):
    def find_parent(parent, x) :
        if parent[x] != x :
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union_parent(parent, a, b) :
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b :
            parent[b] = a
        else :
            parent[a] = b
        # 코드를 잘 보면 자기자신의 부모를 갱신하는 것일수도 있지만 자기 부모의 부모를 갱신하는 것일수도 있음
        # 따라서 현재 노드의 부모는 갱신되지 않을 수 있다.
        # 이게 마지막에 for문으로 갱신해줘야 하는 이유
            
    parents = [i for i in range(n)]
    for i in range(len(computers)) :
        for j in range(len(computers[i])) :
            if computers[i][j] == 1 :
                    # union 설명 참고
                    union_parent(parents, i, j)
    
    # 마지막으로 한번 더 돌면서 부모노드를 한번 더 갱신해줘야 실제 정확한 부모 노드 테이블 완성
    # 이유는 union 설명 참고
    for i in range(len(parents)) :
        find_parent(parents, i)
    return len(set(parents))
    # 여기서 실수한게 뭐냐면 parent로 갱신하면 현재노드의 부모노드의 부모를 찾는 것이 되기 때문에
    # 현재노드가 갱신이 안되고 부모노드의 부모를 갱신하는 것이 됨
    # 따라서 위의 방식으로 현재 인덱스 노드의 부모를 새로 갱신해줘야 정답
    # 아래는 잘못된 예시
    # real_parents = [find_parent(parents, parent) for parent in parents]
    # return len(set(real_parents))