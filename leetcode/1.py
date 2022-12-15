def two_sum(nums, target):
    for i, num in enumerate(nums):
        sub = target - num
        if sub in nums[i + 1:]:
            return [i, nums[i + 1:].index(sub) + i + 1]
