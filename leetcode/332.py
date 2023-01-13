import collections

def init_graph(tickets):
    graph = collections.defaultdict(list)

    for departure, arrival in sorted(tickets):
        graph[departure].append(arrival)

    return graph

def find_itinerary(tickets):
    itinerary = []
    graph = init_graph(tickets)

    def dfs(v):
        while graph[v]:
            dfs(graph[v].pop())

        itinerary.append(v)

    dfs('JFK')
    return itinerary[::-1]
