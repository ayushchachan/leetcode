class Solution:
    def maxJump(self, stones):
        if len(stones) == 2:
            return stones[-1] - stones[0]

        i = 0       # i is current position

        n = len(stones) - 1

        j = 0

        max_jump = 0;

        while i < n:

            if i + 1 == n:
                max_jump = max(max_jump, max(stones[n] - stones[i], stones[n] - stones[j]))
                i += 1
                continue

            else:
                max_jump = max(max_jump, max(stones[i + 2] - stones[i], stones[i + 1] - stones[j]))
                j = i + 1
                i += 2
                continue
        return max_jump


                
