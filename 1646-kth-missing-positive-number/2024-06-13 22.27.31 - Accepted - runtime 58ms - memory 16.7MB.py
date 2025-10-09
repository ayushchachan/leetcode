class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        prev = 0
        i = 0
        while(i < len(arr)):
            if(count + arr[i] - prev - 1  >= k):
                break
            count += arr[i] - prev - 1
            prev = arr[i]
            i += 1
        return prev + k - count

        