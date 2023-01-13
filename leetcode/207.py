import collections

def init_graph(prerequisites):
    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        graph[b].append(a)

    return graph

def can_finish(num_courses, prerequisites):
    graph = init_graph(prerequisites)
    path = []
    visited = []

    def dfs(v):
        if v in path:
            return False

        if v in visited:
            return True        

        path.append(v)
        visited.append(v)

        for adj in graph[v]:
            if not dfs(adj):
                return False

        path.pop()

        return True

    for v in list(graph):
        if not dfs(v):
            return False

    return True
