# 쿼드트리
# Silver I
# https://www.acmicpc.net/problem/1992
from sys import stdin


def read_input():
    N = int(stdin.readline())
    all_data = [stdin.readline().rstrip()
                for _ in range(N)]
    return N, all_data


def solve(N: int, all_data: list[str]):
    def compress(data: list[str]) -> str:
        if not any('1' in row for row in data):
            return '0'
        if not any('0' in row for row in data):
            return '1'

        mid = len(data) // 2
        top = data[:mid]
        bot = data[mid:]
        return ''.join([
            '(',
            compress([row[:mid] for row in top]),
            compress([row[mid:] for row in top]),
            compress([row[:mid] for row in bot]),
            compress([row[mid:] for row in bot]),
            ')'
        ])

    # BEGIN
    return compress(all_data)


if __name__ == '__main__':
    print(solve(*read_input()))
