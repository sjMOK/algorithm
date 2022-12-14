import collections

def group_anagrams(strs):
    mapping = collections.defaultdict(list)

    for str in strs:
        mapping[''.join(sorted(str))].append(str)

    return mapping.values()
