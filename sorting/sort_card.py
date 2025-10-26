# 카드 정렬하기
# Gold IV
# https://www.acmicpc.net/problem/1715
from sys import stdin
from heapq import heappush, heappop

def solution():
    N = int(stdin.readline())

    queue = []
    for _ in range(N):
        heappush(queue, int(stdin.readline()))

    count = 0
    while len(queue) > 1:
        A, B = heappop(queue), heappop(queue)
        count += A + B
        heappush(queue, A + B)

    print(count)

if __name__ == '__main__':
    solution()