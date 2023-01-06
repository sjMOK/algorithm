def init_graph(nums):
    graph = {num: [] for num in nums}

    for i in range(len(nums)):
        for j in range(0, len(nums)):
            if i == j:
                continue

            graph[nums[j]].append(nums[i])

    return graph

def permute(nums):
    graph = init_graph(nums)

    def dfs(vertex, visited):
        visited.append(vertex)
        if len(visited) == len(graph):
            permutations.append(visited)
            return

        for w in graph[vertex]:
            if w not in visited:
                dfs(w, visited[:])

    permutations = []
    for vertex in graph.keys():
        dfs(vertex, [])

    return permutations
