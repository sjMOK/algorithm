
def dfs(graph, v):
    graph[v]['visited'] = True
    for w in graph[v]['adjacent_vertexes']:
        if not graph[w]['visited']:
            dfs(graph, w)

def init_graph(grid):
    graph = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "1":
                continue

            graph[(i, j)] = {
                'visited': False,
                'adjacent_vertexes': [],
            }

            if i > 0 and grid [i - 1][j] == "1":
                graph[(i, j)]['adjacent_vertexes'].append((i - 1, j))
            
            if i < len(grid) - 1 and grid[i + 1][j] == "1":
                graph[(i, j)]['adjacent_vertexes'].append((i + 1, j))

            if j > 0 and grid[i][j - 1] == "1":
                graph[(i, j)]['adjacent_vertexes'].append((i, j - 1))

            if j < len(grid[i]) - 1 and grid[i][j + 1] == "1":
                graph[(i, j)]['adjacent_vertexes'].append((i, j + 1))

    return graph

def numIslands(grid):
    graph = init_graph(grid)
    num = 0

    for vertex in graph.keys():
        if not graph[vertex]['visited']:
            dfs(graph, vertex)
            num += 1

    return num
