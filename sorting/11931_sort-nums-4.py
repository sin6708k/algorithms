# 수 정렬하기 4
# Silver V
# https://www.acmicpc.net/problem/11931
from sys import stdin

def h_sort(nums, h):
    for i in range(h, len(nums)):
        for j in range(i-h, -1, -h):
            if nums[j] > nums[j+h]:
                break
            nums[j], nums[j+h] = nums[j+h], nums[j]

# Shell Sort를 사용하여 문제를 풀 것이다.
def solution():
    N = int(stdin.readline())
    nums = [int(stdin.readline()) for _ in range(N)]

    # N을 넘지 않는 h의 최대값을 구한다.
    h = 1
    while h < N/3:
        h = 3*h + 1

    # h = ..., 13, 4, 1 순으로 h-sort를 반복한다.
    while h >= 1:
        h_sort(nums, h)
        h = h//3

    # 이제 답을 출력한다.
    for num in nums:
        print(num)

if __name__ == '__main__':
    solution()