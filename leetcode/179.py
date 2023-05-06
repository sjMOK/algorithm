def to_swap(num1, num2):
    return str(num2) + str(num1) > str(num1) + str(num2)

def largestNumber(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and to_swap(nums[j - 1], nums[j]):
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
        
    return str(int(''.join(map(str, nums))))

print(largestNumber([3,30,34,5,9]))