class Solution:
    dp = [0, 1]

    def fib(self, n: int) -> int:
        if n <= 1:
            return self.dp[n]
        
        if n <= len(self.dp) - 1:
            return self.dp[n]
        
        self.dp.append(self.fib(n - 1) + self.fib(n - 2))
        return self.dp[n]
