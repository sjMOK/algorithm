def subsets(nums):
    answer = []

    def dfs(elements, path):
        answer.append(path[:])

        for i in range(len(elements)):
            dfs(elements[i + 1:], path + [elements[i]])

    dfs(nums, [])
    return answer
