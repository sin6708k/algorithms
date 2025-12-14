# 최단경로
# Gold IV
# https://www.acmicpc.net/problem/1753
import math
from heapq import heappush, heappop
from sys import stdin

V, E = map(int, stdin.readline().split())
K = int(stdin.readline())

# 인접 리스트 방식으로 그래프를 구현한다.
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

dist = [math.inf] * (V+1)
dist[K] = 0

# 본래 Dijkstra's Algorithm에는 Indexed PQ를 사용해야 하나,
# 여기서는 일반적인 우선순위 큐를 사용하겠다.
pq = [(0, K)]
included = [False] * (V+1)

while pq:
    _, u = heappop(pq)

    if included[u]:
        continue
    included[u] = True

    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heappush(pq, (dist[v], v))

for u in range(1, V+1):
    print(dist[u] if dist[u] != math.inf else 'INF')