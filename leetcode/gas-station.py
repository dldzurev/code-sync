class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_total = 0
        start = 0
        tot_gas = 0
        tot_cost = 0
        for i in range(len(gas)):
            tot_cost += cost[i]
            tot_gas += gas[i]
            diff = gas[i] - cost[i]
            curr_total += diff            
            if curr_total < 0:
                start = i + 1
                curr_total = 0


        if (tot_gas - tot_cost) < 0:
            return -1
        return start