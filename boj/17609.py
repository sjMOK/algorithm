import sys

input = sys.stdin.readline


def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
        
    return True


def solution(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            if is_palindrome(s, l + 1, r) or is_palindrome(s, l, r - 1):
                return 1
            else:
                return 2
            
        l += 1
        r -= 1
        
    return 0

t = int(input())
for _ in range(t):
    s = input().strip()
    print(solution(s))
    
