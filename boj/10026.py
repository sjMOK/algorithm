import sys
from collections import deque


sys.setrecursionlimit(10000)


def dfs(graph, i, j, discovered=[]):
    discovered[i][j] = True
    adjs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    for w_i, w_j in adjs:
        if -1 < w_i < len(graph) and -1 < w_j < len(graph) and not discovered[w_i][w_j] and graph[i][j] == graph[w_i][w_j]:
            discovered = dfs(graph, w_i, w_j, discovered)
            
    return discovered

def main():
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(input()))


    normal_cnt = 0
    discovered = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not discovered[i][j]:
                dfs(graph, i, j, discovered)
                normal_cnt += 1

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'


    color_blind_cnt = 0
    discovered = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not discovered[i][j]:
                dfs(graph, i, j, discovered)
                color_blind_cnt += 1
                
    print(normal_cnt, color_blind_cnt)


if __name__ == '__main__':
    main()
