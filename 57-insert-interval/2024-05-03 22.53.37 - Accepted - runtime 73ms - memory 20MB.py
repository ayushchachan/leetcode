class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        i = 0
        j = 0
        if len(intervals) == 0:
            return [newInterval]
        minNumber = newInterval[0]
        maxNumber = newInterval[1]

        # calculating i
        while i < len(intervals) and intervals[i][0] <= newInterval[0]:
            i += 1

        i -= 1
        j = i
        if i > -1 and intervals[i][0] <= newInterval[0] <= intervals[i][1]:
            minNumber = min(intervals[i][0], newInterval[0])
            i -= 1

        ##calculating j
        j = max(0, j)

        while j < len(intervals) and intervals[j][0] <= newInterval[1]:
            maxNumber = max(intervals[j][1], newInterval[1])
            j += 1

        if j <= len(intervals):
            return intervals[: i + 1 :] + [[minNumber, maxNumber]] + intervals[j::]
        else:
            return intervals[: i + 1 :] + [[minNumber, maxNumber]]

