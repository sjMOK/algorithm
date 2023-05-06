from collections import Counter

def isAnagram(s, t):
    return len(s) == len(t) and Counter(list(s)) == Counter(list(t))


print(isAnagram('rat', 'car'))