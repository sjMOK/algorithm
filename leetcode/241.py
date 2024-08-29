from typing import List


class Solution:
    def compute(self, left, right, operator):
        res = []
        for l in left:
            for r in right:
                res.append(eval(str(l) + operator + str(r)))
                
        return res
        
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        res = []
        for i, char in enumerate(expression):
            if char in '+*-':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                
                res.extend(self.compute(left, right, char))
                
        return res


expression = '2*3-4*5'
print(Solution().diffWaysToCompute(expression))