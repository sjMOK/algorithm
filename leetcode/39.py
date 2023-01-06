def combination_sum(candidates, target):
    combinations = []
    combination = []
    candidates.sort()
    
    def dfs(elements):
        sum_of_combination = sum(combination)
        if sum_of_combination > target:
            return
        elif sum_of_combination == target:
            combinations.append(combination[:])
            return

        for i in range(len(elements)):
            combination.append(elements[i])
            dfs(elements[i:])
            combination.pop()

    dfs(candidates)
    return combinations
