# 최소신장트리-크루스칼 알고리즘 써야함
# 그냥 부모찾기 버전
# def find_parent(parent, x) :
#     if parent[x] != x:
#         #부모에 부모를 찾아야 할 수 있어 많은 재귀가 발생할 수 있음
#         return find_parent(parent, parent[x])
#     return x


# 경로압축(Path Compression)버전
def find_parent(parent, x):
    if parent[x] != x:
        # 모든 재귀가 끝난 뒤 자기자신의 루트노드로 parent가 모두 업데이트 되므로
        # 다음에 찾을때는 parent[x]에 루트노드 값을 이미 가지고 있으므로 1재귀만에 접근 가능
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    # 초기에는 자기 인덱스로 값 초기화
    parent = [i for i in range(n)]
    answer = 0
    # 비용이 작은 순으로 정렬
    sorted_costs = sorted(costs, key=lambda x: x[2])
    for x in sorted_costs:
        a, b, cost = x
        # 부모가 같지 않으면 같은 부모로 설정하고 최소신장트리에 포함 및 비용 추가
        # 부모가 같으면 사이클이 발생한 것이라 최소신장트리에 추가하지 않고 넘어감
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
            # 최소신장트리를 만들고 싶으면 조건된edge를 추가하면 됨
            # edges.append(x)

    return answer
