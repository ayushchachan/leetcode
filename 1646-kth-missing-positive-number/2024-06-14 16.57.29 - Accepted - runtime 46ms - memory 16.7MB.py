class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0;high = len(arr) - 1;
        count = 0
        while(low <= high):
            mid = (low + high)//2
            count = arr[mid] - (mid  + 1)
            if(count  >= k and (mid == 0 or arr[mid - 1] - (mid - 1 + 1) < k)):
                break
            elif(count < k ):
                low = mid + 1
            else:
                high = mid - 1
        if(low > len(arr) - 1):
            mid += 1
        
        print(mid)
        
        
        return k  + mid

