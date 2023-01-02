import collections

def top_k_frequent(nums, k):
    counter = collections.Counter(nums)
    return [elem[0] for elem in counter.most_common(k)]
