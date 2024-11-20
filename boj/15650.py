import sys

input = sys.stdin.readline


def get_combinations(path, num, n, m):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    
    for i in range(num, n + 1):
        get_combinations(path + [i], i + 1, n, m)

n, m = map(int, input().split())
get_combinations([], 1, n, m)
