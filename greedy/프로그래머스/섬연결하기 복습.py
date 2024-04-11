#  최소신장트리 - 크루스칼 알고리즘 문제임


# 경로압축(Path compression) 버전 부모찾기
def find_parent(parent, x):
    # 부모 테이블 값이 자기 자신이 아닐때 자신의 부모를 찾아줌
    # 자기 자신 값일 경우는 아래의 union_parent에서 추후에 업데이트될꺼라 상관없음
    if parent[x] != x:
        # 모든 재귀가 끝나면 자기자신의 루트노드로 부모테이블이 갱신되므로
        # 다음에 찾을 때는 parent[x]에 루트노드 값을 이미 가지고 있으므로 1재귀만에 도달 가능
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 만약 a, b의 부모를 찾았는데
    # 각자 아직 자기자신의 인덱스를 부모테이블에 가지고 있거나(갱신 안된 상황)
    # 서로 부모가 다른 경우 인덱스가 낮은 쪽으로 업데이트 시켜줌(그냥 합친다는 개념)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    answer = 0
    # 초기에는 자기 자신 인덱스로 부모 테이블을 초기화
    parent = [i for i in range(n)]

    # 비용이 작은 순으로 오름차순 정렬
    sorted_costs = sorted(costs, key=lambda x: x[2])

    for edge in sorted_costs:
        a, b, cost = edge

        # 부모가 같지 않으면 같은 부모로 union하고 최소신장트리에 포함 및 answer에 비용 추가
        # 부모가 같으면 사이클이 발생한 것이라 최소신장트리에 추가하지 않고 넘어감
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

            # 최소신장트리를 만들고 싶으면 조건된edge를 추가하면 됨
            # edges.append(x)

    return answer
