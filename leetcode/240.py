from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        hi = len(matrix[0]) - 1
        for i in range(len(matrix)):
            k = bisect.bisect_left(matrix[i], target, hi=hi)
            if k < len(matrix[0]) and matrix[i][k] == target:
                return True
            hi = k

        return False
