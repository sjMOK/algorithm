def dfs(grid, i, j, visited):
    if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[i]) - 1 or \
        grid[i][j] != "1" or visited[i][j]:
        return

    visited[i][j] = True

    dfs(grid, i - 1, j, visited)
    dfs(grid, i + 1, j, visited)
    dfs(grid, i, j - 1, visited)
    dfs(grid, i, j + 1, visited)

def numIslands(grid):
    num = 0
    visited = [[False for _ in row] for row in grid]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1" and not visited[i][j]:
                dfs(grid, i, j, visited)
                num += 1
    return num
