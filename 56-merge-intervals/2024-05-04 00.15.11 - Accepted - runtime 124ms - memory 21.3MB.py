# @lc code=start
def sortkey(ele):
    return ele[0]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=sortkey)
        minE = intervals[0][0]
        maxE = intervals[0][1]
        i = 1
        res = []
        print(intervals)
        while i < len(intervals):
            ele = intervals[i]
            if minE <= ele[0] <= maxE:
                maxE = max(maxE, ele[1])
            else:
                res.append([minE, maxE])
                minE = ele[0]
                maxE = ele[1]
            i += 1
        print(minE, maxE)
        res.append([minE, maxE])
        return res

