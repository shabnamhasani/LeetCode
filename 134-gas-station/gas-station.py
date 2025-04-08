class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        """Track total_tank = total gas - total cost
        Track current_tank while simulating the trip
        When current_tank < 0, reset your starting station to the next one, and reset current_tank =0
        If total gas < total cost, the answer is always -1."""
        current_tank = 0
        total_gas = 0
        total_cost = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_tank += gas[i] - cost[i]
            
            if current_tank < 0:
                # Can't start from any of the previous stations
                start_index = i + 1
                current_tank = 0
        
        if total_gas < total_cost:
            return -1
        else:
            return start_index
