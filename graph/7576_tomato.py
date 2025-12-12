# 토마토
# Gold V
# https://www.acmicpc.net/problem/7576
from collections import deque
from sys import stdin

M, N = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# Multi-source BFS를 수행하기 위해 익은 토마토를 전부 큐에 넣는다.
queue = deque((x, y, 0) for x in range(M) for y in range(N) if matrix[y][x] == 1)
visited = [[False] * M for _ in range(N)]

days = 0
while queue:
    x, y, t = queue.popleft()

    if x < 0 or x >= M or y < 0 or y >= N:
        continue
    if visited[y][x]:
        continue
    if matrix[y][x] == -1:
        continue

    visited[y][x] = True
    days = max(days, t)

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        queue.append((nx, ny, t+1))

if any(not visited[y][x] and matrix[y][x] == 0 for x in range(M) for y in range(N)):
    print(-1)
else:
    print(days)