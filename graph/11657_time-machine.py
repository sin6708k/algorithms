# 타임머신
# Gold IV
# https://www.acmicpc.net/problem/11657
import math
from sys import stdin

N, M = map(int, stdin.readline().split())

# 인접 리스트 방식으로 그래프를 구현한다.
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

dist = [math.inf] * (N+1)
dist[1] = 0

# 음수 간선이 존재할 수 있으므로, Bellman-Ford Algorithm을 사용해야 한다.
for _ in range(N-1):
    for u in range(1, N+1):
        for v, w in graph[u]:
            dist[v] = min(dist[v], dist[u] + w)

# 거리를 또 업데이트해야 한다면, 음수 사이클이 존재한다는 뜻이다.
for u in range(1, N+1):
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            print(-1)
            exit()

for u in range(2, N+1):
    print(dist[u] if dist[u] != math.inf else -1)