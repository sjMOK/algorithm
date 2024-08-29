from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        start = gas_tank = 0
        for i in range(len(gas)):
            if gas_tank + gas[i] < cost[i]:
                start = i + 1
                gas_tank = 0
            else:    
                gas_tank += gas[i] - cost[i]
            
        return start
