# 줄 세우기
# Gold III
# https://www.acmicpc.net/problem/2252
from collections import deque
from sys import stdin

def dfs(s, graph, visited):
    stack = [(s, 0)]
    order = deque()

    while stack:
        u, state = stack.pop()

        if state == 0:
            if visited[u]:
                continue
            visited[u] = True
            stack.append((u, 1))
            for v in graph[u]:
                stack.append((v, 0))
        else:
            order.appendleft(u)

    return list(order)

def solution():
    N, M = map(int, stdin.readline().split())

    # 인접 리스트 방식으로 그래프를 구현한다.
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)

    # 모든 정점에 DFS를 수행하여 Topological Order를 구한다.
    visited = [False] * (N+1)
    order = []
    for u in range(1, N+1):
        order = dfs(u, graph, visited) + order

    print(*order)

if __name__ == '__main__':
    solution()