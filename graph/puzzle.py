# 퍼즐
# Gold II
# https://www.acmicpc.net/problem/1525
from sys import stdin
from heapq import heappush, heappop
from itertools import product

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Board:
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s

    def __eq__(self, other):
        return self.s == other.s

    def __lt__(self, other):
        return self.s < other.s

    def at(self, x, y):
        return int(self.s[y*3 + x])

    def zero_point(self):
        for x, y in product(range(3), repeat=2):
            if self.at(x, y) == 0:
                return x, y
        return None

    def swap(self, x1, y1, x2, y2):
        i = y1*3 + x1
        j = y2*3 + x2
        if i > j:
            i, j = j, i
        s = self.s[:i] + self.s[j] + self.s[i+1:j] + self.s[i] + self.s[j+1:]
        return Board(s)

    def manhattan(self):
        result = 0
        for x, y in product(range(3), repeat=2):
            e = self.at(x, y)
            if e == 0:
                continue
            tx, ty = (e-1) % 3, (e-1) // 3
            result += abs(tx-x) + abs(ty-y)
        return result

    def neighbors(self):
        zx, zy = self.zero_point()
        result = []
        for i in range(4):
            nx, ny = zx+dx[i], zy+dy[i]
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            result.append(self.swap(zx, zy, nx, ny))
        return result

    def twin(self):
        zx, zy = self.zero_point()
        points = [(0, 0), (1, 0), (2, 0)]
        if (zx, zy) in points:
            points.remove((zx, zy))
        x1, y1 = points[0]
        x2, y2 = points[1]
        return self.swap(x1, y1, x2, y2)

    def goal(self):
        return self.manhattan() == 0

# 2차원 입력 데이터를 1차원 배열로 받는다.
input_data = []
for _ in range(3):
    for c in stdin.readline().split():
        input_data.append(c)

# 1차원 배열 데이터를 문자열로 변환하고 Board 클래스로 캡슐화한다.
# 원 보드와 그 트윈 중 반드시 하나만 목표에 도달할 수 있다.
first_board = Board(''.join(input_data))
twin_board = first_board.twin()

# 큐의 아이템은 (예상 움직임, 현재 보드, 현재 움직임, 트윈 여부)이다.
queue = []
heappush(queue, (0 + first_board.manhattan(), first_board, 0, False))
heappush(queue, (0 + twin_board.manhattan(), twin_board, 0, True))

visited = set()
while queue:
    pred_move, board, move, twin = heappop(queue)
    visited.add(board.s)

    # 현재 보드가 목표에 도달했으면 답을 출력하고 루프를 종료한다.
    if board.goal():
        print(move if not twin else -1)
        break

    # 현재 보드의 이웃들을 구해서 이미 방문했던 것만 제외하고 큐에 넣는다.
    for next_board in board.neighbors():
        if next_board.s in visited:
            continue
        heappush(queue, (move+1 + next_board.manhattan(), next_board, move+1, twin))