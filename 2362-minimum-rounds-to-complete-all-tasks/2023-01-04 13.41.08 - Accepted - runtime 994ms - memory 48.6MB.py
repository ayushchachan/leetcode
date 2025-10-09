class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        from collections import Counter
        freq = Counter(tasks)
        numCycles = 0

        self.cycles = {2: 1, 3: 1, 4: 2}

        for key in freq.keys():
            val = freq[key]
            if (val == 1):
                return -1
            else:
                numCycles += self.cyclesRequired(val)

        return numCycles

    def cyclesRequired(self, n):
        if n in self.cycles:
            return self.cycles[n]
        self.cycles[n] = self.cyclesRequired(n - 3) + 1
        return self.cycles[n]
