import collections, heapq, sys

def init_graph(flights, n):
    graph = collections.defaultdict(list)
    for v, u, w in flights:
            graph[v].append((u, w))
    return graph

def find_cheapest_price(n, flights, src, dst, k):
    graph = init_graph(flights, n)
    heap = [[0, src, 0]]

    i = 0
    while heap:
        price, v, i = heapq.heappop(heap)
        
        if v == dst:
            return price

        if i <= k:
            i += 1
            for u, w in graph[v]:
                alt = price + w
                heapq.heappush(heap, [alt, u, i])

    return -1


print(find_cheapest_price(3, [[0,1,2],[1,2,1],[2,0,10]], 1, 2, 1))