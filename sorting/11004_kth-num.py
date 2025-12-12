# K번째 수
# Silver V
# https://www.acmicpc.net/problem/11004
from sys import stdin
import random

# 중복값을 효과적으로 처리하기 위해 3-way Partitioning을 사용한다.
def partition(A, low, high):
    # 배열의 첫 번째 요소를 pivot으로 두자.
    # 그리고 <pivot(pivot보다 작은 값이 모이는 곳)의 직후 인덱스를 lt라 하고,
    # >pivot(pivot보다 큰 값이 모이는 곳)의 직전 인덱스를 gt라 하자.
    pivot, i, lt, gt = A[low], low, low, high

    # 배열을 첫 번째부터 >pivot에 도착할 때까지 순회한다.
    while i <= gt:
        # A[i]가 pivot보다 작으면 <pivot으로 보내고, 크면 >pivot으로 보낸다.
        if A[i] < pivot:
            A[i], A[lt] = A[lt], A[i]
            lt += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1

    # 순회가 끝나면 <pivot과 >pivot 사이는 =pivot(pivot과 같은 값이 모이는 곳)이 된다.
    return lt, gt

# Quick Select를 사용하여 문제를 풀 것이다.
def solution():
    N, K = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))

    # pivot을 골고루 선정하기 위해 배열을 먼저 랜덤 셔플한다.
    random.shuffle(A)

    low, high = 0, N-1
    while low < high:
        lt, gt = partition(A, low, high)
        # <pivot과 >pivot 중 K번째 요소가 있는 곳만 탐색한다.
        if K-1 < lt:
            high = lt-1
        elif K-1 > gt:
            low = gt+1
        # K번째 요소가 =pivot에 있으면 답을 찾은 것이다.
        else:
            break

    # 이제 답을 출력한다.
    print(A[K-1])

if __name__ == '__main__':
    solution()