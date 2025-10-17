# K번째 수
# Silver V
# https://www.acmicpc.net/problem/11004
from sys import stdin
import random

N, K = map(int, stdin.readline().split())
A = list(map(int, stdin.readline().split()))

# Quick Select는 이미 정렬된 배열이 입력으로 들어오면 엄청 느려진다.
# 따라서 이런 경우가 발생하지 않도록 배열을 셔플한다.
for i in range(1, N):
    j = random.randint(0, i)
    A[i], A[j] = A[j], A[i]

# 중복된 값을 더 효율적으로 처리하는 3-way Partitioning Quick Select를 사용한다.
def partition(low, high):
    # 배열의 첫 번째 요소를 pivot라 하자.
    # 그리고 <pivot(pivot보다 작은 값이 모이는 곳)의 직후 인덱스를 lt라 하고,
    # >pivot(pivot보다 큰 값이 모이는 곳)의 직전 인덱스를 gt라 하자.
    pivot, i, lt, gt = A[low], low, low, high

    # 배열을 첫 번째부터 >pivot에 도착할 때까지 순회한다.
    while i <= gt:
        # A[i]가 pivot보다 작으면 <pivot으로 보낸다.
        if A[i] < pivot:
            A[i], A[lt] = A[lt], A[i]
            lt += 1
        # A[i]가 pivot보다 크면 >pivot으로 보낸다.
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1

    # 순회가 끝나면 <pivot과 >pivot 사이는 =pivot(pivot과 같은 값이 모이는 곳)이 된다.
    return lt, gt

low, high = 0, N-1
while low < high:
    lt, gt = partition(low, high)
    # K번째 요소가 <pivot에 있으면 거기만 확인한다.
    if K-1 < lt:
        high = lt-1
    # K번째 요소가 >pivot에 있으면 거기만 확인한다.
    elif K-1 > gt:
        low = gt+1
    # K번째 요소가 =pivot에 있으면 답을 찾은 것이다.
    else:
        break

# 이제 답을 출력한다.
print(A[K-1])