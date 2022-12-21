def product_except_self(nums):
    product = 1
    answer = []

    for num in nums:    # get accumulated left product array
        answer.append(product)
        product *= num
    
    product = 1
    for i in range(len(nums) - 1, -1, -1):  # get accumulated right product array, for O(1) space complexity
        answer[i] *= product
        product *= nums[i]

    return answer
