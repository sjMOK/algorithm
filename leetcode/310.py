import collections

def find_min_height_trees(n, edges):
    if n <= 1:
        return [0]

    graph = collections.defaultdict(list)
    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    leaves = []
    for v in list(graph):
        if len(graph[v]) == 1:
            leaves.append(v)

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            u = graph[leaf].pop()
            graph[u].remove(leaf)
            if len(graph[u]) == 1:
                new_leaves.append(u)

        leaves = new_leaves

    return leaves


find_min_height_trees(1, [])