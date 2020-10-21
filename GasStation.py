"""
PROBLEM

Given two integer arrays A and B of size N.
There are N gas stations along a circular route, where the amount of gas at station i is A[i].

You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i
to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the minimum starting gas station’s index if you can travel around the circuit once, otherwise return -1.

You can only travel in one direction. i to i+1, i+2, … n-1, 0, 1, 2.. Completing the circuit means starting at i and
ending up at i again.

"""


def canCompleteCircuit(gas, cost):
        n = len(gas)
        
        # Take only indices whose value of gas is greater than the cost.
        index = [i for i in range(n) if gas[i] >= cost[i]]
        start = -1
        
        # Easy for 1 clockwise movement
        g2 = gas+gas
        c2 = cost+cost
        
        while index:
            start = index[0]
            tank = gas[start]
            for j in range(start+1, len(g2)):
                tank = tank - c2[j-1] + g2[j]
                if tank < c2[j]:                                    
                    break
                elif j==start+n:
                    return start
            index.pop(0)
        return -1

	      
