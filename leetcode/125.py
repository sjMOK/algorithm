import collections

def is_palindrome(s):
    deque = collections.deque()
    for char in s:
        if char.isalnum():
            deque.append(char.lower())

    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False

    return True
