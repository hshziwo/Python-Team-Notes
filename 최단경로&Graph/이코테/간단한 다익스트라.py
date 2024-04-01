import sys

input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

# 노드 수 n, 간선 수 m
n, m = map(int, input().split())
# 시작노드 입력받기
start = int(input())

# 그래프 메트릭스를 표현하기 위한 이차원 배열 선언
# 시작이 1이여서 0은 안쓸려고 n + 1 까지의 배열을 만들어줌
graph = [[] for _ in range(n + 1)]
# 이미 방문한 노드인지 체크 목적 테이블
visited = [False] * (n + 1)
# 최단 거리 테이블을 처음에 무한으로 초기화 선언
distance = [INF] * (n + 1)

# 그래프 데이터 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # 그래프 정보를 입력하는데
    # a 노드에서 b 노드로 가는 비용이 c라는 의미로
    # a 노드에 튜플 형태로 (b, c)를 넣어줌
    # a에서의 간선은 여러개일 수 있음
    # graph[a] = [( ),( ),( )]
    graph[a].append((b, c))


# 이 함수는 테이블을 한번 업데이트한 이후에 그 다음에 어떤 노드를 선택해서 또 다익스트라를 진행할 지 선택하는 함수다.
def get_smallest_node():
    min_value = INF
    index = 0  # 일단 초기값으로 0번째 노드 입력 근데 0번째 노드는 이 문제에서는 없는 값이기 때문에 index노드의 값은 항상 INF값이다.
    # 이 문제에서는 1번 노드부터 시작함.
    for i in range(1, n + 1):
        # 방문하지 않은 노드이면서 그 다음 거리 비용이 제일 싼 노드를 for문 돌면서 선택
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            # 그러한 조건의 노드를 index변수에 저장
            index = i

    # 최소 거리 노드 인덱스를 리턴
    return index


def dijkstra(start):
    # 거리 테이블에 시작 노드의 거리값을 0으로 초기화
    # 왜냐하면 자기 자신과의 거리는 0이기 때문에
    distance[start] = 0
    visited[start] = True  # 방문처리
    # 시작 노드와 연결된 노드들의 distance 값 테이블을 일단 시작꺼만 먼저 업데이트 해줌.
    # j를 간선 정보라고 보면 됨. 튜플형태 (b, c) b는 next노드고, c는 거리 비용
    for j in graph[start]:
        # distance[j[0]] == start와 연결된 노드들의 거리값을 ( = j[1]) == 실제 입력받은 시작에서 연결된 b노드의 c 거리값 일단 바꿔줌.
        # start의 거리값이 0이기 때문에 start의 거리값을 지금은 더할 필요 없음 근데 뭐 더해도 됨.
        next_node = j[0]
        next_cost = j[1]
        distance[next_node] = next_cost

    # 이제 한번 시작 노드에 대해서는 테이블이 업데이트 됐기 때문에 계속 루틴을 반복함.
    # n - 1 인 이유는 시작노드에 대해서는 위에서 했기 때문에
    # 시작노드를 제외한 전체 n-1개에 대해서 반복
    for i in range(n - 1):
        # 지금 거리테이블에서 가장 가까운 거리의 노드를 선택
        # 여기서부터 새로 시작임
        now = get_smallest_node()
        visited[now] = True  # 방문처리
        for j in graph[now]:
            next_node = j[0]
            next_cost = j[1]
            # 이미 방문한 노드면 이미 최적값임.
            if visited[next_node]:
                continue
            # 일단 현재 노드의 거리 값에서 다음 노드의 거리 비용을 일단 더함.
            cost = distance[now] + next_cost
            # 현재의 노드를 거쳐서 next_node로 가는 것이 기존에 next_node의 옵티멀값 보다 비용이 싸면 바꿔줌.
            if cost < distance[next_node]:
                distance[next_node] = cost


# 알고리즘 시작
# 함수 완료 후 distance 테이블이 모두 옵티멀 해져있을 것임
dijkstra(start)

# 요거는 시작노드에서 출발해서 모든 노드에 대해서 도착 거리 비용을 출력하는 거임
# 그냥 시작노드에서 B노드까지의 최소 거리 비용을 출력하려면 그냥 distance[b]로 하면 됨
for i in range(1, n + 1):
    # 시작노드에서 도달할 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    else:
        # 도달 할 수 있는 경우 거리 출력
        print(distance[i], end=" ")


# input값
# 6 11
# 1
# 1 2 2
# 1 4 1
# 1 3 5
# 2 4 2
# 2 3 3
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# output값
# 0 2 3 1 2 4
