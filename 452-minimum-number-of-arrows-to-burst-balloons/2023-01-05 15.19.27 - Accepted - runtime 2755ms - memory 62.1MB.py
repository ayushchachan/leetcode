class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        count = 0

        A = sorted(points, key=lambda x : x[1])
        n = len(points)
        # now sorted by finishing points
        i = 0
        while i < n:
            count += 1
            j = i + 1
            while j < n and A[j][0] <= A[i][1]:
                j += 1
            i = j
        return count
        
