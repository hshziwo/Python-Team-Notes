import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
# fromto 테이블
graph = [[] for i in range(n+1)]
# 최단 거리 테이블
distance = [INF] * (n+1)

for _ in range(m) :
    x, y, z = map(int, input().split())
    # x -> y 비용이 z라는 의미
    graph[x].append((y,z))

def dijkstra(start) :
        q = []
        # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q :
              # heap은 우선순위큐이므로 거리가 가장 짧은 노드 순으로 pop됨
              dist, now = heapq.heappop(q)
              if distance[now] < dist :
                    continue
              for i in graph[now]:
                    cost = dist + i[1]
                    if cost < distance[i[0]]:
                          distance[i[0]] = cost
                          heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0
for d in distance :
      # 초기값이 INF이므로 방문하지 않았다면 INF일때 넘어감
      if d != INF :
            count += 1
            max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1 출력
print(count - 1, max_distance)
