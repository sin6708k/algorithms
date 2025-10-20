# 볼록 껍질
# Platinum V
# https://www.acmicpc.net/problem/1708
from sys import stdin
from math import atan2

def ccw(p1, p2, p3):
    # p1 -> p2 -> p3으로 가는 선이 볼록하면 양수를, 오목하면 음수를, 일직선 상에 있으면 0을 반환한다.
    return (p3[0] - p2[0]) * (p1[1] - p2[1]) - (p1[0] - p2[0]) * (p3[1] - p2[1])

def solution():
    N = int(stdin.readline())
    points = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

    # 가장 아래에 있는 점(만약 여러 개면 그 중 가장 오른쪽에 있는 점)을 bot이라 하자.
    bot = min(points, key=lambda p: (p[1], -p[0]))

    # 모든 점을 bot과 각도 기준(만약 같으면 y값 기준)으로 오름차순 정렬한다.
    points.sort(key=lambda p: (atan2(p[1] - bot[1], p[0] - bot[0]), p[1]))

    # 기본적으로 1번째 점과 2번째 점을 볼록 껍질에 포함한다.
    convex_hull = [points[0], points[1]]

    for p3 in points[2:] + [points[0]]:
        while len(convex_hull) > 1:
            # 가장 최근에 볼록 껍질에 포함된 점을 p2, 그 다음을 p1이라 하자.
            p2, p1 = convex_hull[-1], convex_hull[-2]
            # 만약 p1 -> p2 -> p3으로 가는 선이 볼록하면 p2는 볼록 껍질에 여전히 포함된다.
            if ccw(p1, p2, p3) > 0:
                break
            # 그렇지 않으면 p2는 볼록 껍질에 사실 포함되지 않는다. 그러므로 p2를 제외한다.
            # 그리고 그 다음 p2, p1을 구해서 선이 볼록한 경우를 만날 때까지 이를 반복한다.
            else:
                convex_hull.pop()

        # 제외할 p2를 전부 제외했으면 이제 p3를 볼록 껍질에 포함한다.
        convex_hull.append(p3)

    # 마지막 점은 1번째 점과 중복이므로 제외한다.
    convex_hull.pop()

    # 이제 답을 출력한다.
    print(len(convex_hull))

if __name__ == '__main__':
    solution()