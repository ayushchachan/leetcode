

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        i = 0;j = 1
        count = 0
        intervals.sort()
        while(i < len(intervals) and j < len(intervals)):
            ele = intervals[i]
            nextEle = intervals[j]
            if(nextEle[0] < ele[1]):
                if(nextEle[1] > ele[1]):
                    j += 1
                else:
                    i,j = j,j+1
                count += 1
            else:
                i,j = j,j+1
        return count
             

            


        
