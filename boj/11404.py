import sys

input = sys.stdin.readline


def floyd(matrix, n):
    for v in range(1, n + 1):
        for i in range(1, n + 1):
            if i == v:
                continue

            for j in range(1, n + 1):
                matrix[i][j] = min(matrix[i][j], matrix[i][v] + matrix[v][j])
                
    return matrix


def main():
    n = int(input())
    m = int(input())
    matrix = [[float('inf') if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        matrix[a][b] = min(matrix[a][b], c)

    matrix = floyd(matrix, n)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if matrix[i][j] == float('inf'):
                print('0', end=' ')
            else:
                print(matrix[i][j], end=' ')
        print('')

    
if __name__ == '__main__':
    main()
