from sys import stdin

def solution():
    T = int(stdin.readline())
    N = [int(stdin.readline()) for _ in range(T)]

    A = [(1,0),(0,1)]
    for i in range(2, max(N) + 1):
        zeros = A[i-1][0] + A[i-2][0]
        ones = A[i-1][1] + A[i-2][1]
        A.append((zeros, ones))

    for n in N:
        print(A[n][0], A[n][1])

if __name__ == '__main__':
    solution()