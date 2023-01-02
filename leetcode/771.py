import collections

def num_jewels_in_stones(jewels, stones):
    count = 0
    counter = collections.Counter(stones)
    for jewel in jewels:
        count += counter[jewel]

    return count
