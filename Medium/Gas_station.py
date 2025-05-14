class Solution:
    def canCompleteCircuit(self, gas, cost):
        total_tank =0
        curr_tank = 0
        start_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                start_station = i + 1
                curr_tank = 0

        return  start_station if total_tank >= 0 else -1
    
#Example usage
if __name__ =="__main__":
    solution = Solution()

    #Example 1
    gas = [1,2,3,4,5]
    cost = [2,3,4,5,1]
    start_station = solution.canCompleteCircuit(gas,cost)
    print(start_station) 

    #Example 2
    gas = [2,3,4]
    cost = [3,4,3]
    start_station = solution.canCompleteCircuit(gas,cost)
    print(start_station)