class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currGas = 0
        lastI = 0
        i = 0

        def checkIndex(i, currGas):
            index = 0
            while index < i:
                currGas += gas[index]
                currGas -= cost[index]
                index += 1
                if currGas < 0:
                    return -1
            return i

        while i < len(gas):
            currGas += gas[i]
            currGas -= cost[i]
            i += 1
            if currGas < 0:
                lastI = i
                currGas = 0

        if lastI == len(gas):
            return -1
        else:
            return checkIndex(lastI, currGas)

