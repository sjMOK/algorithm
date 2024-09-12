import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline

def dijkstra(graph, start, v_num):
    distances = {i: float('inf') for i in range(1, v_num + 1)}
    distances[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
                
    return distances

def main():
    v_num, e_num = map(int, input().split())
    start = int(input())
    graph = defaultdict(list)

    for _ in range(e_num):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        
    distances = dijkstra(graph, start, v_num)
    for i in range(1, v_num + 1):
        if distances[i] == float('inf'):
            print('INF')
        else:
            print(distances[i])

if __name__ == "__main___":
    main()
