# Strongly Connected Component
# Platinum V
# https://www.acmicpc.net/problem/2150
from collections import deque
from sys import stdin

def dfs(s, graph, visited):
    stack = [(s, 0)]
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
    V, E = map(int, stdin.readline().split())

    # 인접 리스트 방식으로 그래프를 구현하며, 동시에 역그래프도 구한다.
    graph = [[] for _ in range(V+1)]
    graph_reversed = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)
        graph_reversed[v].append(u)

    # 역그래프의 모든 정점에 DFS를 수행하여 Topological Order를 구한다.
    visited = [False] * (V+1)
    order = []
    for u in range(1, V+1):
        order = dfs(u, graph_reversed, visited) + order

    # 구한 순서의 반대로 원 그래프에 DFS를 수행한다.
    visited = [False] * (V+1)
    components = []
    for u in order:
        component = dfs(u, graph, visited)
        if component:
            components.append(component)

    # 구한 SCC를 정렬한다.
    for component in components:
        component.sort()
    components.sort(key=lambda x: x[0])

    # 모든 SCC를 출력한다.
    print(len(components))
    for component in components:
        print(*component, -1)

if __name__ == '__main__':
    solution()