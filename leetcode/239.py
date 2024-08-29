from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        for i, v in enumerate(nums):
            if i >= k and q[0][1] == i - k:
                q.popleft()
                
            while q and v >= q[-1][0]:
                q.pop()
                
            q.append((v, i))
            if i >= k - 1:
                res.append(q[0][0])
                
        return res
