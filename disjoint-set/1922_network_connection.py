# 네트워크 연결
# Gold IV
# https://www.acmicpc.net/problem/1922
from sys import stdin

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)

    def root(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        p, q = self.root(x), self.root(y)

        if p == q:
            return

        # p가 속한 트리가 q가 속한 트리보다 더 크면 q를 p의 밑에 붙인다.
        # 아니면 그 반대로 한다.
        if self.size[p] >= self.size[q]:
            self.parent[q] = p
            self.size[p] += self.size[q]
        else:
            self.parent[p] = q
            self.size[q] += self.size[p]

    def find(self, x, y):
        return self.root(x) == self.root(y)

def solution():
    N = int(stdin.readline())
    M = int(stdin.readline())

    # Kruskal's Algorithm을 수행하기 위해 간선을 오름차순 정렬한다.
    edges = [tuple(map(int, stdin.readline().split())) for _ in range(M)]
    edges.sort(key=lambda x: x[2])

    # 사이클을 판별하기 위해 Union Find를 사용할 것이다.
    uf = UnionFind(N)
    edge_count = 0
    sum_weight = 0

    for u, v, w in edges:
        if uf.find(u, v):
            continue
        uf.union(u, v)

        # 이 간선이 사이클을 만들지 않는다면 MST를 구성하는 간선으로 선택한다.
        edge_count += 1
        sum_weight += w
        if edge_count == N-1:
            break

    print(sum_weight)

if __name__ == '__main__':
    solution()