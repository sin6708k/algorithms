# 집합의 표현
# Gold V
# https://www.acmicpc.net/problem/1717
from sys import stdin

class DisjointSets:
    def __init__(self, parent):
        self.parent = parent
        self.size = [1] * len(parent)

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

    def connected(self, x, y):
        return self.root(x) == self.root(y)

# Union Find를 사용하여 문제를 풀 것이다.
def solution():
    N, M = map(int, stdin.readline().split())

    # 부모 노드를 자기 자신으로 초기화한다.
    sets = DisjointSets(list(range(N + 1)))

    for _ in range(M):
        op, x, y = map(int, stdin.readline().split())
        # 입력이 0이면 합집합 연산을 수행하고, 1이면 집합의 연결 여부를 출력한다.
        if op == 0:
            sets.union(x, y)
        elif op == 1:
            print('YES' if sets.connected(x, y) else 'NO')

if __name__ == '__main__':
    solution()