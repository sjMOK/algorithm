def zero_one_knapsack_array(n, k, items):
    dp = [0] * (k + 1)
    for w, v in items:
        for i in range(k, w - 1, -1):
            dp[i] = max(dp[i], dp[i - w] + v)
                
    return dp[-1]

def zero_one_knapsack_matrix(n, k, items):
    dp = []
    for i in range(n + 1):
        dp.append([])
        for j in range(k + 1):
            if i == 0 or j == 0:
                dp[i].append(0)
            elif j >= items[i - 1][0]:
                dp[i].append(
                    max(
                        dp[i - 1][j],
                        items[i - 1][1] + dp[i - 1][j - items[i - 1][0]]
                    )
                )
            else:
                dp[i].append(dp[i - 1][j])

    return dp[-1][-1]

def main():
    n, k = map(int, input().split())
    items = []
    for _ in range(n):
        w, v = map(int, input().split())
        items.append((w, v))

    print(zero_one_knapsack_array(n, k, items))

if __name__ == '__main__':
    main()
