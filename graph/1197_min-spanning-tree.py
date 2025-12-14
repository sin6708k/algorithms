# 최소 스패닝 트리
# Gold IV
# https://www.acmicpc.net/problem/1197
from sys import stdin

class IndexedPQ:
    def __init__(self, n: int):
        self.size = 0
        self.index = [-1] * (n+1)  # heap position -> index
        self.pos = [-1] * (n+1)    # index -> heap position (-1이면 힙에 없음)
        self.key = [None] * (n+1)  # index -> key

    def contains(self, i):
        return self.pos[i] != -1

    def key_of(self, i):
        return self.key[i]

    def insert(self, i: int, key: float):
        self.size += 1
        self.index[self.size] = i
        self.pos[i] = self.size
        self.key[i] = key
        self._swim(self.size)

    def pop(self):
        # 힙에서 첫 번째 자리에 있는 원소를 가져온다.
        i = self.index[1]
        key = self.key[i]

        # 마지막 자리에 있는 원소를 첫 번째 자리로 이동시킨다.
        # 그리고 그 원소가 제자리를 찾아가도록 한다.
        self._exchange(1, self.size)
        self.size -= 1
        self._sink(1)

        # 마지막 자리를 비운다.
        self.index[self.size+1] = -1
        self.pos[i] = -1
        self.key[i] = None
        return key

    def decrease_key(self, i, key):
        self.key[i] = key
        self._swim(self.pos[i])

    def _less(self, p: int, q: int) -> bool:
        i, j = self.index[p], self.index[q]
        return self.key[i] < self.key[j]

    def _exchange(self, p: int, q: int) -> None:
        i, j = self.index[p], self.index[q]
        self.index[p], self.index[q] = j, i
        self.pos[i], self.pos[j] = q, p

    def _swim(self, p: int) -> None:
        while p > 1 and self._less(p, p//2):
            self._exchange(p, p//2)
            p //= 2

    def _sink(self, p: int) -> None:
        while 2*p <= self.size:
            q = 2*p
            if q < self.size and self._less(q+1, q):
                q += 1
            if self._less(p, q):
                break
            self._exchange(p, q)
            p = q

def include(u, pq, graph, included):
    included[u] = True

    for v, w in graph[u]:
        if not pq.contains(v):
            pq.insert(v, (w, u, v))
        elif w < pq.key_of(v)[0]:
            pq.decrease_key(v, (w, u, v))

def solution():
    V, E = map(int, stdin.readline().split())

    # 인접 리스트 방식으로 그래프를 구현한다.
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    # Prim's Algorithm을 수행하기 위해 Indexed PQ를 사용할 것이다.
    pq = IndexedPQ(V)
    included = [False] * (V+1)

    include(1, pq, graph, included)
    edge_count = 0
    sum_weight = 0

    while edge_count < V-1:
        w, u, v = pq.pop()

        if not included[u]:
            include(u, pq, graph, included)
            edge_count += 1
            sum_weight += w
        elif not included[v]:
            include(v, pq, graph, included)
            edge_count += 1
            sum_weight += w

    print(sum_weight)

if __name__ == '__main__':
    solution()