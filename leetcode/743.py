import heapq, collections

def init_graph(times, n):
    graph = collections.defaultdict(list)
    edges = {}

    for u, v, w in times:
        graph[u].append(v)
        edges[(u, v)] = w

    return graph, edges

def dijkstra(graph, edges, k):
    distances = {}
    heap = [(0, k)]

    while heap:
        dist, v = heapq.heappop(heap)
        if v not in distances:
            distances[v] = dist
            for adj in graph[v]:
                heapq.heappush(heap, (dist + edges[(v, adj)], adj))

    return distances

def network_delay_time(times, n, k):
    graph, edges = init_graph(times, n)
    distances = dijkstra(graph, edges, k)

    if len(distances) == n:
        return max(distances.values())

    return -1

print(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2))