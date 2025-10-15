# 최소 스패닝 트리
# Gold IV
# https://www.acmicpc.net/problem/1197
from sys import stdin
from heapq import heapify, heappop


def read_input():
    V, E = map(int, stdin.readline().split())
    edges = [tuple(reversed(tuple(map(int, stdin.readline().split()))))
             for _ in range(E)]
    heapify(edges)
    return V, E, edges


class DisjointSet:
    def __init__(self, n):
        self.__roots = list(range(n))

    def find(self, v: int) -> int:
        if self.__roots[v] != v:
            self.__roots[v] = self.find(self.__roots[v])
        return self.__roots[v]

    def union(self, v: int, u: int):
        root_of_v = self.find(v)
        root_of_u = self.find(u)
        if root_of_v < root_of_u:
            self.__roots[root_of_v] = root_of_u
        else:
            self.__roots[root_of_u] = root_of_v


def solve(V: int, E: int, edges: list[tuple[int, int, int]]):
    connected = DisjointSet(V + 1)
    sum_weight = 0

    while edges:
        w, u, v = heappop(edges)
        root_of_v = connected.find(v)
        root_of_u = connected.find(u)
        if root_of_v != root_of_u:
            connected.union(root_of_v, root_of_u)
            sum_weight += w
    return sum_weight


if __name__ == '__main__':
    print(solve(*read_input()))
