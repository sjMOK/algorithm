from typing import List
import bisect


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = len(g) - 1, len(s) - 1
        n = 0
        
        while i > -1 and j > -1:
            if s[j] < g[i]:
                while i > -1 and s[j] < g[i]:
                    i -= 1
            
            if i < 0:
                break
            
            i -= 1
            j -= 1
            n += 1
            
        return n
