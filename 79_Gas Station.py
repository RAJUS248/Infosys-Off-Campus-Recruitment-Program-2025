def canCompleteCircuit(gas, cost):

    if sum(gas) < sum(cost):
        return -1
    
    start = 0
    cur_gas = 0

    for i in range(len(gas)):
        cur_gas = cur_gas + gas[i] - cost[i]

        if cur_gas < 0:
            cur_gas = 0
        
            start = i + 1

    return start



gas = [5,1,2,3,4]
cost = [4,4,1,5,1]  
print(canCompleteCircuit(gas,cost))