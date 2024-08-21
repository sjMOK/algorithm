from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            
        original_nums = nums[left:] + nums[:left]
        pivot_idx = len(nums) - left
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target > original_nums[mid]:
                left = mid + 1
            elif target < original_nums[mid]:
                right = mid - 1
            else:
                return (mid + len(nums) - pivot_idx) % len(nums)
            
        return -1
