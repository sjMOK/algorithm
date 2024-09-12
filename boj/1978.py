import math

def is_prime_number(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))
for i, num in enumerate(nums):
    nums[i] = is_prime_number(num)

print(sum(nums))
