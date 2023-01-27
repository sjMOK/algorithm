import heapq

def find_kth_largest(nums, k):
    nums = [(-num, num) for num in nums]
    heapq.heapify(nums)

    for _ in range(k-1):
        heapq.heappop(nums)

    return heapq.heappop(nums)[1]


find_kth_largest([3,2,1,5,6,4], 2)