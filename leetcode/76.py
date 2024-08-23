import collections
import sys

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = collections.Counter(t)
        t_length = len(t)
        left = 0
        min_length = sys.maxsize
        
        for right in range(len(s)):
            if counts[s[right]] > 0:
                t_length -= 1
            counts[s[right]] -= 1
            
            while t_length == 0:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                if counts[s[left]] == 0:
                    t_length += 1
                counts[s[left]] += 1
                left += 1
                    
        return '' if min_length == sys.maxsize else s[start:start + min_length]
