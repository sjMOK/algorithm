from typing import List


class Solution:
    def binary_search(self, num, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if num < nums[mid]:
                right = mid - 1
            elif num > nums[mid]:
                left = mid + 1
            else:
                return True
            
        return False
        
        
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        ret = set()
        
        for num in nums1:
            if self.binary_search(num, nums2):
                ret.add(num)
                
        return ret