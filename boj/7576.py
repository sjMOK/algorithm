from collections import deque


class Solution:
    def __init__(self):
        self.m, self.n = map(int, input().split())
        self.arr = []
        for _ in range(self.n):
            self.arr.append(list(map(int, input().split())))
        
    def solution(self):
        queue = deque()
        for i in range(self.n):
            for j in range(self.m):
                if self.arr[i][j] == 1:
                    queue.append((i, j))
                    
        cnt = self.bfs(queue)
            
        for i in range(self.n):
            if 0 in self.arr[i]:
                return -1
            
        return cnt
    
    def bfs(self, queue):
        cnt = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for k, l in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if self.is_valid_tomato(k, l):
                        self.arr[k][l] = 1
                        queue.append((k, l))

            if queue:
                cnt += 1
                
        return cnt

    def is_valid_tomato(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m and self.arr[i][j] == 0:
            return True
        return False


print(Solution().solution())
