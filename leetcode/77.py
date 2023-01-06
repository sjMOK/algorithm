def combine(n, k):
    combinations = []
    combination = []

    def dfs(elements, count):
        if count == k:
            combinations.append(combination[:])
            return

        for i, elem in enumerate(elements):
            next_elements = elements[i + 1:]
            combination.append(elem)
            dfs(next_elements, count + 1)
            combination.pop()
        
    dfs(range(1, n + 1), 0)
    return combinations

print(combine(1, 1))