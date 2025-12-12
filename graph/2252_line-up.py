# 줄 세우기
# Gold III
# https://www.acmicpc.net/problem/2252
from collections import deque
from sys import stdin

def dfs(start, graph, visited):
    stack = [(start, 0)]
    order = deque()

    while stack:
        v, state = stack.pop()

        if state == 0:
            if visited[v]:
                continue
            visited[v] = True
            stack.append((v, 1))
            for w in graph[v]:
                stack.append((w, 0))
        else:
            order.appendleft(v)

    return list(order)

def solution():
    N, M = map(int, stdin.readline().split())

    # 인접 리스트 방식으로 그래프를 구현한다.
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        v, w = map(int, stdin.readline().split())
        graph[v].append(w)

    # 모든 정점에 DFS를 수행하여 Topological Order를 구한다.
    visited = [False] * (N+1)
    order = []
    for v in range(1, N+1):
        order = dfs(v, graph, visited) + order

    print(*order)

if __name__ == '__main__':
    solution()