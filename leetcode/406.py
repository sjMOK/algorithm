from typing import List
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        res = []
        
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))
        
        while heap:
            person = heapq.heappop(heap)
            res.insert(person[1], [-person[0], person[1]])
            
        return res
