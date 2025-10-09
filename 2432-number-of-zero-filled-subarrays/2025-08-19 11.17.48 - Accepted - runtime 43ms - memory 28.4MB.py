class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        
        N = len(nums)
        answer = 0
        i = 0
        while i < N:
            if nums[i] == 0:
                ## subarray started
                subarray_length = 1
                j = i + 1
                while j < N and nums[j] == 0:
                    subarray_length += 1
                    j += 1
                    i = j
                
                # print("subarray length =", subarray_length)
                ## subarray length noted
                answer += int((subarray_length * (subarray_length + 1))/2 )
            
            
            i += 1
        return answer
                    
            
        